import numpy as np
from openbabel.pybel import readstring as pbreadstring

def evToNm(eV, error=0):
    def ev2nm(eV):
        h = 4.135667e-15
        c = 2.99792e8
        return np.divide(np.multiply(h,c), np.multiply(eV,1e-9))
    
    if type(eV) == float:
        nm = ev2nm([eV, eV+error, eV-error])
        if   error == 0:
            return nm[0]
        elif error != 0:
            return (nm[0], nm[1], nm[2])

    else:
        nm = ev2nm(eV)
        return nm

def nmToEv(nm, error = 0):
    return evToNm(nm, error)

def stripIllegal(string):
    chars = '(),'
    for char in chars:
        string = string.replace(char, '')
    return string

def smiles2xyz(smiles):
    mol = pbreadstring('smi', smiles)
    mol.make3D()
    return mol.write('xyz')

def rmsd(expectation, predictedList):
    rmsd = np.sqrt(np.divide(np.sum(np.square(np.subtract(predictedList, expectation))),np.shape(predictedList)[0]))
    return rmsd

class dfLoad(object):
    import pandas as pd
    def __init__(self, withPath=False, df='/Users/adrea/gdrive/Notebooks/Excited States/resources/databases/fluorophores-small.json', monCSV=True):
        self.dfPath = df
        self.monCSV = monCSV
        self.withPath = withPath
        
    def __enter__(self):
        self.df = self.pd.read_json(self.dfPath)
        if self.withPath == True:
            return self.df, self.dfPath
        else:
            return self.df
  
    def __exit__(self, a, b, c):
        self.df.to_json(self.dfPath, indent=2)
        if self.monCSV == True:
            with monarchHandler() as mon:
                mon.writeCSV(self.df)

class monarchHandler:
    from paramiko import SSHClient, AutoAddPolicy
    def __init__(self, host="monarch.erc.monash.edu", user="asnow", jobid="job_id_done", jobkey="eEvfCdvzr4jy_SX51JYjKhAILZjPa53n8MFcQd1FErB"):
        self.host = host
        self.user = user
        self.jobid = jobid
        self.jobkey = jobkey
        
    def __enter__(self):
        self.openSSH()
        return self

    def __exit__(self, a, b, c):
        self.closeSSH()


    def openSSH(self):
        try:
            transport = self.ssh.get_transport()
            transport.send_ignore()
        except:
            self.ssh = self.SSHClient()
            self.ssh.set_missing_host_key_policy(self.AutoAddPolicy())
            self.ssh.connect(self.host, username=self.user)
            self.sftp = self.ssh.open_sftp()
        return

    def closeSSH(self):
        global ssh
        try:
            self.ssh.close()
        except:
            pass

    def writeCSV(self, df, filename="/home/asnow/p2015120004/asnow/fluorophore-small/data.csv"):
        self.writeFile(df.to_csv(), filename)
        return

    def writeFile(self, content, filename):
        self.openSSH()

        with self.sftp.file(filename, "w+", -1 ) as f:
            f.write(content)
        return

    def readFile(self, filename):
        self.openSSH()

        with self.sftp.file(filename, "r", -1 ) as f:
            lines = f.readlines()
        return lines

    def run(self, command):
        self.openSSH()
        stdin, stdout, stderr = self.ssh.exec_command(command)
        out = stdout.read().decode().split('\n')
        err = stderr.read().decode().split('\n')
        return out, err

    def timedOut(self, printJobs=False):
        scratchFolders = []
        jobNames = []
        out = []
        out, err = self.run('ls -lah ~/scratch/')
        for line in out:
            try:
                scratchFolder = line.split()[8] 
                if scratchFolder not in ['.', '..']:
                    scratchFolders += [scratchFolder]
            except:
                pass
        
        out, err = self.run('squeue -o\'%.50j\' -u asnow --sort=\'-T,j\'')
        for line in out:
            try:
                jobName = line.split('.')[0].strip()
                if jobName not in ['NAME']:
                    jobNames += [jobName]
            except:
                pass

        for scratch in scratchFolders:
            if scratch not in jobNames:
                out += [scratch]
                if printJobs == True: print(scratch)

        return out

    def pullEnergyORCA(self, file, state=0, roots=0):
        # e.g. /home/asnow/p2015120004/asnow/fluorophore-small/geoms/rb0-chcl3/orca-opt/rb0-chcl3-opt/rb0-chcl3-opt.out
        out, err = self.run(f'cat {file} | grep \'Number of roots to be determined\\|:  E=  \\|****ORCA TERMINATED NORMALLY****\'')
        results = []
        excitations = []
        complete = False
        for line in out:
            if 'Number of roots to be determined               ...' in line:   
                nroots = int(line.split()[7])
            elif f'STATE  'in line and ':  E=  ' in line:
                results += [line]
            elif '****ORCA TERMINATED NORMALLY****' in line:
                complete = True

        for i in results[-nroots:]:
            excitations += [float(i.split()[5])]

        excitations = excitations[-nroots:]

        if roots != 0:
            excitations = excitations[-roots:]

        if state != 0:
            excitations = excitations[(state-1)]
        if complete == True:
            return excitations, evToNm(excitations)
        else:
            return

    def pullEnergyPsi4(self, file, state=0, roots=0):
        # e.g. /home/asnow/p2015120004/asnow/fluorophore-small/geoms/rb0-chcl3/orca-opt/rb0-chcl3-opt/rb0-chcl3-opt.out
        out, err = self.run(f'cat {file} | grep \'State   (eV)    (cm^-1)    (nm)     (au)              (l,au)   (v,au)     (s^-1)\' -A 20')
        out2, err = self.run(f'cat {file} | grep \'*** Psi4 exiting successfully. Buy a developer a beer!\'')
        out3, err = self.run(f'cat {file} | grep -i \'roots_per_irrep\' | tail -n 1')
        
        excitations = []
        λs = []
        complete = False
        for line in out:
            splitLine = line.split()
            if len(splitLine) == 10:
                try:
                    excitations += [float(splitLine[2])]
                    λs          += [float(splitLine[4])]
                except:
                    pass

        for line in out2:
            if '*** Psi4 exiting successfully.' in line:
                complete = True

        for line in out3:
            if 'roots_per_irrep' in line.lower():
                nroots = int(line.split()[1][1])

        excitations = excitations[-nroots:]

        if roots != 0:
            excitations = excitations[-roots:]
            λs = λs[-roots:]
        

        if state != 0:
            excitations = excitations[state-1]
            λs = λs[state-1]
        if complete == True:
            return excitations, λs
        else:
            return

    def pullEnergyQChem(self, file, state=0, roots=0):
        # e.g. /home/asnow/p2015120004/asnow/fluorophore-small/geoms/rb0-chcl3/orca-opt/rb0-chcl3-opt/rb0-chcl3-opt.out
        out, err = self.run(f'cat {file} | grep \'CIS_N_ROOTS\\|: excitation energy (eV) =\\|END OF GEOMETRY OPTIMIZER USING LIBOPT3\'')
        results = []
        excitations = []
        complete = False
        for line in out:
            if 'CIS_N_ROOTS' in line:   
                nroots = int(line.split()[1])
            elif ': excitation energy (eV) =' in line:
                results += [line]
            elif 'END OF GEOMETRY OPTIMIZER USING LIBOPT3' in line:
                complete = True

        for i in results[-nroots:]:
            excitations += [float(i.split()[7])]

        excitations = excitations[-nroots:]

        if roots != 0:
            excitations = excitations[-roots:]

        if state != 0:
            excitations = excitations[(state-1)]

        if complete == True:
            return excitations, evToNm(excitations)
        else:
            return


    def buildCRESTOpt(self, key, smiles, charge, solvent, mult=1, partner=True):
        uhfString = '' if mult == 1 else ' --uhf 1'
        fileDir = f'/home/asnow/p2015120004/asnow/fluorophore-small/geoms/{key}/crest'

        self.run(f'mkdir -p {fileDir}')
        self.writeFile(smiles2xyz(smiles), f'{fileDir}/{key}.xyz')

        slmString = '#!/bin/bash\n' 
        slmString += '#SBATCH --time=24:00:00\n'
        slmString += '#SBATCH --ntasks=16\n'
        slmString += '#SBATCH --cpus-per-task=1\n'
        slmString += '#SBATCH --ntasks-per-node=16\n'
        slmString += '#SBATCH --mem=32GB\n'
        slmString += '#SBATCH --partition=comp,short\n'
    
        if partner == True: slmString += '#SBATCH --qos=partner\n\n'

        slmString += 'curl -s -X POST -H "Content-Type: application/json" -d \'{"value1": "CREST opt "' + key + '" , "value2": "started", "value3": ""}\' https://maker.ifttt.com/trigger/$JOBID/with/key/$JOBKEY > /dev/null\n'

        slmString += '__conda_setup="$(\'/home/asnow/miniconda3/bin/conda\' \'shell.bash\' \'hook\' 2> /dev/null)"\n'
        slmString += 'if [ $? -eq 0 ]; then\n'
        slmString += '    eval "$__conda_setup"\n'
        slmString += 'else\n    if [ -f "/home/asnow/miniconda3/etc/profile.d/conda.sh" ]; then\n'
        slmString += '        . "/home/asnow/miniconda3/etc/profile.d/conda.sh"\n'
        slmString += '    else\n        export PATH="/home/asnow/miniconda3/bin:$PATH"\n    fi\nfi\n'
        slmString += 'unset __conda_setup\n\n'
        slmString += 'ulimit -s unlimited\n'
        slmString += 'export OMP_STACKSIZE=4G\n'
        slmString += 'export OMP_NUM_THREADS=16,1\n'
        slmString += 'export OMP_THREAD_LIMIT=16\n'
        slmString += 'export OMP_MAX_ACTIVE_LEVELS=1\n'
        slmString += 'export MKL_NUM_THREADS=16\n'

        slmString += f'cd {fileDir}\n'
        slmString += f'/usr/bin/time -v crest {key}.xyz --chrg {charge} --alpb {solvent} {uhfString}\n\n'
        slmString += 'curl -s -X POST -H "Content-Type: application/json" -d \'{"value1": "CREST opt "' + key + '" , "value2": "finished", "value3": ""}\' https://maker.ifttt.com/trigger/$JOBID/with/key/$JOBKEY > /dev/null\n\n'

        self.writeFile(slmString, f'{fileDir}/{key}-crest.slm')


        out, err = self.run(f'cd {fileDir} && /opt/slurm-latest/bin/sbatch {key}-crest.slm')
        if err != ['']:
            print(err)
        else:
            print(key)
            print(out[0])
        return


    def buildORCAOpt(self, key, method, basis, charge, solvent, 
                     nroots=4, root=0, mult=1, mopath='', xyzpath='', catxyzpath='', 
                     kdiis=False, soscf=True, notrah=False, scfstring=''):
        orcamethod = 'cam-b3lyp' if method == 'cb3lyp' else method
        moinp = 'moread ' if mopath != '' else ''
        mostring = f'\n\n%moinp "{mopath}"' if mopath != '' else ''
        kdiisstring = 'kdiis ' if kdiis == True else ''
        soscfstring = 'soscf ' if soscf == True else 'nososcf '
        notrahstring = 'notrah ' if notrah == True else ''

        name = stripIllegal(f'{key}-orca-opt-{method}-{basis}-r{root}')
        cpcm = 'CPCM ' if solvent != 'gas' else ''
        filename = f'/home/asnow/p2015120004/asnow/fluorophore-small/geoms/{key}/{name}.inp'
        ORCAInput = f'! Opt {orcamethod} defgrid3 RIJCOSX {basis} tightopt tightscf {cpcm}{moinp}{kdiisstring}{soscfstring}{notrahstring}'
        ORCAInput += mostring
        ORCAInput += '\n\n%maxcore 4096\n\n%pal\n\tnprocs 16\nend\n\n'
        if solvent != 'gas': ORCAInput += f'%cpcm\n\tsmd true\n\tSMDSolvent "{solvent}"\nend\n\n'
        if scfstring != '': ORCAInput += f'%scf\n\t{scfstring}\nend\n\n'
        ORCAInput += f'%tddft\n\tnroots {nroots}\n\tIRoot {root}\n\tcpcmeq true\n\ttda false\nend\n\n'
        if xyzpath == '':
            ORCAInput += f'* xyz {int(charge)} {int(mult)}\n'
            
            if catxyzpath != '':
                lines, err = self.run(f'cat "{catxyzpath}"')
            else:
                lines, err = self.run(f'cat "/home/asnow/p2015120004/asnow/fluorophore-small/geoms/{key}/crest/crest_best.xyz"')
            for line in lines[2:]:
                if len(line.split()) > 2:
                    ORCAInput += f'{line}\n'
            ORCAInput += '*\n\n'
        else:
            ORCAInput += f'* xyzfile {int(charge)} {int(mult)} {xyzpath}\n\n'
        
        self.writeFile(ORCAInput, filename)
        return filename

    def buildPsi4EOMCCSDOpt(self, key, basis, charge, nroots=1, finalNRoots=4, root=0, mult=1, cores=16, xyzpath='', memory=320):
        name = stripIllegal(f'{key}-psi4-opt-eomccsd-{basis}-r{root}')
        filename = f'/home/asnow/p2015120004/asnow/fluorophore-small/geoms/{key}/{name}.in'
        Psi4Input = f'set_num_threads({cores})\nmemory {memory}GB\n\n'
        Psi4Input += 'molecule {\n'
        Psi4Input += f'{int(charge)} {int(mult)}\n'
        lines, err = self.run(f'cat {xyzpath}')
        for line in lines[2:]:
            if len(line.split()) > 2:
                Psi4Input += f'{line}\n'
        Psi4Input += '}\n\n'
        Psi4Input +=  'set {\n'
        Psi4Input +=  '    reference                   rhf\n'
        Psi4Input +=  '    scf_type                    df\n'
        if root > 0: 
            Psi4Input += f'    roots_per_irrep             [{nroots}]\n'
            Psi4Input += f'    follow_root                 {root}\n'
            Psi4Input += f'    prop_root                   {root}\n'
        Psi4Input +=  '    print_trajectory_xyz_file   True\n'
        Psi4Input +=  '    cachelevel                  0\n'
        Psi4Input +=  '}\n\n'
        Psi4Input +=  'set cceom {\n'
        Psi4Input +=  '    r_convergence               1e-3\n'
        Psi4Input +=  '    e_convergence               1e-5\n'
        Psi4Input +=  '    cachelevel                  0\n'
        Psi4Input +=  '}\n\n'
        Psi4Input +=  'set cclambda {\n'
        Psi4Input +=  '    r_convergence               1e-3\n'
        Psi4Input +=  '}\n\n'
        Psi4Input += f'optimize(\'wb97x-d3/{basis}\')\n\n'
        if root > 0: 
            Psi4Input += f'optimize(\'eom-ccsd/{basis}\')\n\n'
            Psi4Input +=  'set {\n'
            Psi4Input +=  '    freeze_core                 true\n'
            Psi4Input += f'    roots_per_irrep             [{finalNRoots}]\n'
            Psi4Input +=  '}\n\n'
            Psi4Input += f'properties(\'eom-ccsd/{basis}\', properties=[\'oscillator_strength\'])\n\n'
        else:
            Psi4Input += f'optimize(\'ccsd/{basis}\')\n\n'
            Psi4Input +=  'set {\n'
            Psi4Input +=  '    freeze_core                 true\n'
            Psi4Input += f'    roots_per_irrep             [{finalNRoots}]\n'
            Psi4Input += f'    prop_root                   {root}\n'
            Psi4Input +=  '}\n\n'
            Psi4Input += f'properties(\'eom-ccsd/{basis}\', properties=[\'oscillator_strength\'])\n\n'

        self.run(f'mkdir -p /home/asnow/p2015120004/asnow/fluorophore-small/geoms/{key}')
        self.writeFile(Psi4Input, filename)
        return filename

    def buildQChemOptSMD(self, key, method, basis, charge, solvent, 
                         nroots=4, root=0, mult=1, singlets=True, 
                         triplets=False):
        qchemmethod = 'CAM-B3LYP' if method == 'cb3lyp' else 'WB97XD' if method == 'wb97x-d3' else method
        solvent = 'trichloromethane' if solvent == 'chloroform' else solvent[2:] if solvent[0:2] == 'n-' else solvent
        name = stripIllegal(f'{key}-qchem-smd-opt-{method}-{basis}-r{root}')

        QChemInput = f'$molecule\n'
        QChemInput += f'{charge} {1}\n'
        lines, err = self.run(f'cat "/home/asnow/p2015120004/asnow/fluorophore-small/geoms/{key}/crest/crest_best.xyz"')
        for line in lines[2:]:
            if len(line.split()) > 2:
                QChemInput += f'{line}\n'
        QChemInput +=  '$end\n\n'
        QChemInput +=  '$rem\n'
        QChemInput +=  '\tMEM_TOTAL          32768\n'
        QChemInput +=  '\tJOBTYPE            opt\n'
        QChemInput += f'\tMETHOD             {qchemmethod}\n'
        QChemInput += f'\tBASIS              {basis}\n'
        QChemInput +=  '\tGUI                2\n'
        if root != 0:
            QChemInput += f'\tCIS_N_ROOTS        {nroots}\n'
            QChemInput += f'\tCIS_SINGLETS       {singlets}\n'
            QChemInput += f'\tCIS_TRIPLETS       {triplets}\n'
            QChemInput += f'\tCIS_STATE_DERIV    {root}\n'
            QChemInput +=  '\tRPA                2\n'
        QChemInput +=  '\tXC_GRID            3\n'
        QChemInput +=  '\tSOLVENT_METHOD     SMD\n'
        QChemInput +=  '$end\n\n'
        QChemInput +=  '$smx\n'
        QChemInput += f'\tSOLVENT            {solvent}\n'
        QChemInput +=  '\tprint              2\n'
        QChemInput +=  '$end\n\n'

        if root == 0:
            QChemInput += '@@@\n\n'
            QChemInput +=  '$molecule\n'
            QChemInput +=  '   read\n'
            QChemInput +=  '$end\n\n'
            QChemInput +=  '$rem\n'
            QChemInput +=  '\tJOBTYPE            sp\n'
            QChemInput += f'\tMETHOD             {qchemmethod}\n'
            QChemInput += f'\tBASIS              {basis}\n'
            QChemInput +=  '\tGUI                2\n'
            QChemInput += f'\tCIS_N_ROOTS        {nroots}\n'
            QChemInput += f'\tCIS_SINGLETS       {singlets}\n'
            QChemInput += f'\tCIS_TRIPLETS       {triplets}\n'
            QChemInput +=  '\tRPA                2\n'
            QChemInput +=  '\tXC_GRID            3\n'
            QChemInput +=  '\tSOLVENT_METHOD     SMD\n'
            QChemInput +=  '$end\n\n'
            QChemInput +=  '$smx\n'
            QChemInput += f'\tSOLVENT            {solvent}\n'
            QChemInput +=  '\tprint              2\n'
            QChemInput +=  '$end\n\n'

        
        filename = f'/home/asnow/p2015120004/asnow/fluorophore-small/geoms/{key}/{name}.inp'.replace('()', '')

        self.writeFile(QChemInput, filename)
        return filename

    def submitFiles(self, flags, files):
        keys = f'export JOBID="{self.jobid}"; export JOBKEY="{self.jobkey}"; '
        if type(files) == str:
            out, err = self.run(f'{keys} /home/asnow/miniconda3/bin/python3 /home/asnow/p2015120004/asnow/bin/slmUtilities/2slm.py {flags} "{files}"')
            if err != ['']:
                print(err)
            else:
                print(out[0])
                print(out[1])
        elif type(files) == list:
            for file in files:
                out, err = self.run(f'{keys} /home/asnow/miniconda3/bin/python3 /home/asnow/p2015120004/asnow/bin/slmUtilities/2slm.py {flags} "{files}"')
                if err != ['']:
                    print(err)
                else:
                    print(out[0])
                    print(out[1])
        return
