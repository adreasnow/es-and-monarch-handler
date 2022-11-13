from ..types.job import Job
from ..types.jobs import Jobs
from ..types.job import Solvents
from ..types.job import PCM

def psi4CasscfScan(job:Job, xyz:str) -> tuple[str, str]:
    psi4String = 'import numpy as np\n'
    psi4String += 'import psi4\n'
    psi4String += f'psi4.set_num_threads({job.procs})\n'
    psi4String += f'psi4.set_memory("{job.mem.total_gb}GB")\n'
    psi4String += f'psi4.core.set_output_file("{job.outfile}", True)\n'
    psi4String += 'psi4_io = psi4.core.IOManager.shared_object()\n'
    psi4String += f'psi4_io.set_default_path("/home/asnow/scratch/{job.name}/")\n\n'


    psi4String += f'with open("{job.path}/occupations.csv", "w+") as f:\n'
    psi4String += '    f.write("Level,Root,Energy\\n")\n'
    psi4String += f'with open("{job.path}/occupations", "w+") as f:\n'
    psi4String += '    f.write("")\n'
    psi4String += f'with open("{job.outfile}", "w+") as f:\n'
    psi4String += '    f.write("")\n\n'

    psi4String += f'mol = psi4.geometry("""\n{job.fluorophore.charge} {job.state.mult}'
    for line in xyz:
        psi4String += f'\n{line}'
    psi4String += '\nsymmetry c1\n""")\n\n'

    psi4String += 'def calculateOccupations(wfn, activeSpace):\n'
    psi4String += '    occuptions = np.diag(wfn.Da_subset("MO").np).real.tolist()\n'
    psi4String += '    start = int(wfn.nalpha()-(activeSpace/2))\n'
    psi4String += '    end = int(wfn.nalpha()+(activeSpace/2))\n'
    psi4String += '    return occuptions[start:end]\n\n'

    psi4String += 'def writeOccupations(string):\n'
    psi4String += f'    with open("{job.path}/occupations", "a") as f:\n'
    psi4String += '        f.write(f"{string}\\n")\n\n'

    psi4String += 'def writeToFile(string):\n'
    psi4String += f'    with open("{job.path}/occupations.csv", "a") as f:\n'
    psi4String += '        f.write(f"{string}\\n")\n\n'

    psi4String += 'psi4.set_options({\n'
    psi4String += f'    "basis":                   "{job.basis.psi4}",\n'
    psi4String += '    "mcscf_type":              "df",\n'
    psi4String += '    "scf_type":                "df",\n'
    psi4String += f'    "roots_per_irrep":         [{job.nroots}],\n'
    psi4String += f'    "num_roots":               {job.nroots},\n'
    psi4String += '    "nat_orbs":                True,\n'
    psi4String += '    "mcscf_maxiter":           1000,\n'
    psi4String += '    "follow_root":             0,\n'
    psi4String += '    "mcscf_diis_start":        3\n'
    psi4String += '})\n\n'

    psi4String += 'e, wfn = psi4.optimize("wb97x-d3", return_wfn=True)\n'
    psi4String += 'e, wfn = psi4.energy("scf", return_wfn=True)\n'
    psi4String += 'writeToFile(f"SCF,0,{e}")\n'
    psi4String += f'active_elec, active_orbs = (2,2)\n'
    psi4String += 'restricted = int(wfn.nalpha() - (active_elec/2))\n'
    psi4String += 'psi4.core.clean()\n\n'

    psi4String += 'psi4.set_options({"follow_root": 0,"active": [active_orbs+2], "restricted_docc": [restricted-1]})\n'
    psi4String += 'e, wfn = psi4.energy("casscf", return_wfn=True)\n'
    psi4String += 'writeToFile(f"4-4,0,{e}")\n'
    psi4String += 'writeOccupations(str(calculateOccupations(wfn, active_orbs+2)))\n'
    if   job.state.root == 1: psi4String += 'psi4.set_options({"follow_root": 1})\n'
    elif job.state.root == 2: psi4String += 'psi4.set_options({"follow_root": 2})\n'
    psi4String += 'e, wfn = psi4.energy("casscf", return_wfn=True)\n'
    if   job.state.root == 1: psi4String += 'writeToFile(f"4-4,1,{e}")\n'
    elif job.state.root == 2: psi4String += 'writeToFile(f"4-4,2,{e}")\n'
    psi4String += 'writeOccupations(str(calculateOccupations(wfn, active_orbs+2)))\n'
    psi4String += 'psi4.core.clean()\n\n'

    psi4String += 'psi4.set_options({"follow_root": 0,"active": [active_orbs+4], "restricted_docc": [restricted-2]})\n'
    psi4String += 'e, wfn = psi4.energy("casscf", return_wfn=True)\n'
    psi4String += 'writeToFile(f"6-6,0,{e}")\n'
    psi4String += 'writeOccupations(str(calculateOccupations(wfn, active_orbs+4)))\n'
    if   job.state.root == 1: psi4String += 'psi4.set_options({"follow_root": 1})\n'
    elif job.state.root == 2: psi4String += 'psi4.set_options({"follow_root": 2})\n'
    psi4String += 'e, wfn = psi4.energy("casscf", return_wfn=True)\n'
    if   job.state.root == 1: psi4String += 'writeToFile(f"6-6,1,{e}")\n'
    elif job.state.root == 2: psi4String += 'writeToFile(f"6-6,2,{e}")\n'
    psi4String += 'writeOccupations(str(calculateOccupations(wfn, active_orbs+4)))\n'
    psi4String += 'psi4.core.clean()\n\n'

    psi4String += 'psi4.set_options({"follow_root": 0,"active": [active_orbs+6], "restricted_docc": [restricted-3]})\n'
    psi4String += 'e, wfn = psi4.energy("casscf", return_wfn=True)\n'
    psi4String += 'writeToFile(f"8-8,0,{e}")\n'
    psi4String += 'writeOccupations(str(calculateOccupations(wfn, active_orbs+6)))\n'
    if   job.state.root == 1: psi4String += 'psi4.set_options({"follow_root": 1})\n'
    elif job.state.root == 2: psi4String += 'psi4.set_options({"follow_root": 2})\n'
    psi4String += 'e, wfn = psi4.energy("casscf", return_wfn=True)\n'
    if   job.state.root == 1: psi4String += 'writeToFile(f"8-8,1,{e}")\n'
    elif job.state.root == 2: psi4String += 'writeToFile(f"8-8,2,{e}")\n'
    psi4String += 'writeOccupations(str(calculateOccupations(wfn, active_orbs+6)))\n'
    psi4String += 'psi4.core.clean()\n\n'

    psi4String += 'psi4.set_options({"follow_root": 0,"active": [active_orbs+8], "restricted_docc": [restricted-4]})\n'
    psi4String += 'e, wfn = psi4.energy("casscf", return_wfn=True)\n'
    psi4String += 'writeToFile(f"10-10,0,{e}")\n'
    psi4String += 'writeOccupations(str(calculateOccupations(wfn, active_orbs+8)))\n'
    if   job.state.root == 1: psi4String += 'psi4.set_options({"follow_root": 1})\n'
    elif job.state.root == 2: psi4String += 'psi4.set_options({"follow_root": 2})\n'
    psi4String += 'e, wfn = psi4.energy("casscf", return_wfn=True)\n'
    if   job.state.root == 1: psi4String += 'writeToFile(f"10-10,1,{e}")\n'
    elif job.state.root == 2: psi4String += 'writeToFile(f"10-10,2,{e}")\n'
    psi4String += 'writeOccupations(str(calculateOccupations(wfn, active_orbs+8)))\n'
    psi4String += 'psi4.core.clean()\n\n'


    psi4SlmString = '#!/bin/bash\n'
    psi4SlmString += '#SBATCH --time=72:00:00\n'
    psi4SlmString += f'#SBATCH --ntasks={job.procs}\n'
    psi4SlmString += '#SBATCH --cpus-per-task=1\n'
    psi4SlmString += f'#SBATCH --ntasks-per-node={job.procs}\n'
    psi4SlmString += f'#SBATCH --mem={job.mem.total_gb}GB\n'
    if job.partner == True: psi4SlmString += '#SBATCH --qos=partner\n'
    psi4SlmString += '#SBATCH --partition=comp\n\n'

    psi4SlmString += 'export PROJECT="p2015120004"\n\n'

    psi4SlmString += 'source /mnt/lustre/projects/p2015120004/apps/psi4-1.6/activate_psi4_job.sh\n'
    psi4SlmString += f'cd {job.path}\n\n'
    psi4SlmString += f'mkdir /home/asnow/scratch/{job.name}\n'
    psi4SlmString += 'ulimit -s unlimited\n'
    psi4SlmString += f'/usr/bin/time -v python {job.name}.py\n'
    psi4SlmString += f'rm -rf /home/asnow/scratch/{job.name}\n\n'


    return psi4String, psi4SlmString

   
    # def pullEnergyPsi4(self, file: str, state: int=0, roots: int=0) -> Union[None, tuple[Union[float, List[float]], Union[float, List[float]]]]:
    #     # e.g. /home/asnow/p2015120004/asnow/fluorophore-small/geoms/rb0-chcl3/orca-opt/rb0-chcl3-opt/rb0-chcl3-opt.out
    #     out, err = self.run(f'cat {file} | grep \'State   (eV)    (cm^-1)    (nm)     (au)              (l,au)   (v,au)     (s^-1)\' -A 20')
    #     out2, err = self.run(f'cat {file} | grep \'*** Psi4 exiting successfully. Buy a developer a beer!\'')
    #     out3, err = self.run(f'cat {file} | grep -i \'roots_per_irrep\' | tail -n 1')

    #     excitations = []
    #     λs = []
    #     complete = False
    #     for line in out:
    #         splitLine = line.split()
    #         if len(splitLine) == 10:
    #             try:
    #                 excitations += [float(splitLine[2])]
    #                 λs          += [float(splitLine[4])]
    #             except:
    #                 pass

    #     for line in out2:
    #         if '*** Psi4 exiting successfully.' in line:
    #             complete = True

    #     for line in out3:
    #         if 'roots_per_irrep' in line.lower():
    #             nroots = int(line.split()[1][1])

    #     excitations = excitations[-nroots:]

    #     if roots != 0:
    #         excitations = excitations[-roots:]
    #         λs = λs[-roots:]

    #     if state != 0:
    #         excitations = excitations[state-1]
    #         λs = λs[state-1]
    #     if complete == True:
    #         return excitations, λs
    #     else:
    #         return


    # def buildPsi4EOMCCSDOpt(self, key: str, basis: str, charge: int, nroots: int=1, finalNRoots: int=4,
    #                         root: int=0, mult: int=1, cores: int=16, xyzpath: str='', memory: int=320) -> str:
    #     name = stripIllegal(f'{key}-psi4-opt-eomccsd-{basis}-r{root}')
    #     filename = f'/home/asnow/p2015120004/asnow/fluorophore-small/geoms/{key}/{name}.in'
    #     Psi4Input = f'set_num_threads({cores})\nmemory {memory}GB\n\n'
    #     Psi4Input += 'molecule {\n'
    #     Psi4Input += f'{int(charge)} {int(mult)}\n'
    #     lines, err = self.run(f'cat {xyzpath}')
    #     for line in lines[2:]:
    #         if len(line.split()) > 2:
    #             Psi4Input += f'{line}\n'
    #     Psi4Input += '}\n\n'
    #     Psi4Input +=  'set {\n'
    #     Psi4Input +=  '    reference                   rhf\n'
    #     Psi4Input +=  '    scf_type                    df\n'
    #     if root > 0: 
    #         Psi4Input += f'    roots_per_irrep             [{nroots}]\n'
    #         Psi4Input += f'    follow_root                 {root}\n'
    #         Psi4Input += f'    prop_root                   {root}\n'
    #     Psi4Input +=  '    print_trajectory_xyz_file   True\n'
    #     Psi4Input +=  '    cachelevel                  0\n'
    #     Psi4Input +=  '}\n\n'
    #     Psi4Input +=  'set cceom {\n'
    #     Psi4Input +=  '    r_convergence               1e-3\n'
    #     Psi4Input +=  '    e_convergence               1e-5\n'
    #     Psi4Input +=  '    cachelevel                  0\n'
    #     Psi4Input +=  '}\n\n'
    #     Psi4Input +=  'set cclambda {\n'
    #     Psi4Input +=  '    r_convergence               1e-3\n'
    #     Psi4Input +=  '}\n\n'
    #     Psi4Input += f'optimize(\'wb97x-d3/{basis}\')\n\n'
    #     if root > 0: 
    #         Psi4Input += f'optimize(\'eom-ccsd/{basis}\')\n\n'
    #         Psi4Input +=  'set {\n'
    #         Psi4Input +=  '    freeze_core                 true\n'
    #         Psi4Input += f'    roots_per_irrep             [{finalNRoots}]\n'
    #         Psi4Input +=  '}\n\n'
    #         Psi4Input += f'properties(\'eom-ccsd/{basis}\', properties=[\'oscillator_strength\'])\n\n'
    #     else:
    #         Psi4Input += f'optimize(\'ccsd/{basis}\')\n\n'
    #         Psi4Input +=  'set {\n'
    #         Psi4Input +=  '    freeze_core                 true\n'
    #         Psi4Input += f'    roots_per_irrep             [{finalNRoots}]\n'
    #         Psi4Input += f'    prop_root                   {root}\n'
    #         Psi4Input +=  '}\n\n'
    #         Psi4Input += f'properties(\'eom-ccsd/{basis}\', properties=[\'oscillator_strength\'])\n\n'

    #     self.run(f'mkdir -p /home/asnow/p2015120004/asnow/fluorophore-small/geoms/{key}')
    #     self.writeFile(Psi4Input, filename)
    #     return filename