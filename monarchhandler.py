from .functions import smiles2xyz
# from .types.solvents import Solvents
# from .types.fluorophores import Fluorophores
# from .types.states import States
# from .types.basis import Basis
# from .types.methods import Methods
from .types.software import Software
# from .types.pcm import PCM
from .types.jobs import Jobs
from .types.status import Status
# from .types.grids import Grids
from .types.job import Job
from .types.slurmJob import slurmJob, slurmStatus
from .qm_handlers.crest import buildCRESTOpt
from .qm_handlers.orca import buildORCAOpt
from .qm_handlers.psi4 import psi4CasscfScan
from .qm_handlers.pyscf import pyscfCasscfScan, pyscfCasscfOpt, pyscfMP2Natorbs
from time import time

class monarchHandler:
    from paramiko import SSHClient, AutoAddPolicy
    def __init__(self, host:str="monarch.erc.monash.edu", user:str="asnow", jobid:str="job_id_done", jobkey:str="eEvfCdvzr4jy_SX51JYjKhAILZjPa53n8MFcQd1FErB") -> None:
        self.host = host
        self.user = user
        self.jobid = jobid
        self.jobkey = jobkey
        self.slurmTime = 0
        self.slurmFreq = 60 # seconds
        self.TOTime = 0
        self.TOFreq = 60 # seconds
        return

    def __enter__(self):
        self._openSSH()
        return self

    def __exit__(self, a, b, c) -> None:
        self._closeSSH()
        return

    def _checkSLURM(self, job:Job | None = None ) -> slurmStatus:
        if self.slurmTime == 0 or (time() - self.slurmTime) > 60:
            self.jobdict = {}
            scratchFolders = []
            self.slurmTime = time()
            statusDict = {"PENDING": slurmStatus.PENDING,
                         "RUNNING": slurmStatus.RUNNING, 
                         "COMPLETING": slurmStatus.COMPLETING, 
                         "FAILED": slurmStatus.FAILED}

            out, err = self.run('squeue -o\'%.18i %u %.100j %.8T\' --sort=\'-T,j\' | grep asnow')
            for line in out:
                if line != '':
                    splitline = line.split()
                    self.jobdict[splitline[2].split('.')[0]] = slurmJob(splitline[0], splitline[2].split('.')[0], statusDict[splitline[3]])
            out, err = self.run('ls -lah ~/scratch/')
            for line in out:
                try:
                    scratchFolder = line.split()[8] 
                    if scratchFolder not in ['.', '..']:
                        scratchFolders += [scratchFolder]
                except:
                    pass

            for scratch in scratchFolders:
                try:
                    self.jobdict[scratch]
                except KeyError:
                    self.jobdict[scratch] = slurmJob(0, scratch, slurmStatus.TIMED_OUT) 
            self.slurmTime = time()

        if job != None:
            try:
                return self.jobdict[job.name].status
            except KeyError:
                return slurmStatus.NONE
        else:
            return slurmStatus.NONE

    def timed_out(self, printJobs=True) -> list[str]:
        self._checkSLURM()
        jobs = [i for i in self.jobdict if self.jobdict[i].status == slurmStatus.TIMED_OUT]
        if printJobs:
            for job in jobs:
                if job != 'qchem': print(job)
        return jobs

    def _openSSH(self) -> None:
        '''Opens up the SSH tunnel'''
        try:
            transport = self.ssh.get_transport()
            transport.send_ignore()
        except:
            self.ssh = self.SSHClient()
            self.ssh.set_missing_host_key_policy(self.AutoAddPolicy())
            self.ssh.connect(self.host, username=self.user)
            self.sftp = self.ssh.open_sftp()
        return

    def _closeSSH(self) -> None:
        '''Closes the SSH tunnel'''
        global ssh
        try:
            self.ssh.close()
        except:
            pass
        return

    def writeFile(self, content: str, filename: str) -> None:
        '''Writes a file, given a string of contents to put in the file, and the filepath'''
        self._openSSH()
        print(filename)
        with self.sftp.file(filename, "w+", -1) as f:
            f.write(content)
        return

    def readFile(self, filename: str) -> list[str]:
        '''Opens an SSH connection and reads a file given an input path'''
        self._openSSH()
        with self.sftp.file(filename, "r", -1) as f:
            lines = f.readlines()
        return lines

    def run(self, command: str) -> tuple[list[str], list[str]]:
        self._openSSH()
        stdin, stdout, stderr = self.ssh.exec_command(command)
        out = stdout.read().decode().split('\n')
        err = stderr.read().decode().split('\n')
        return out, err

    def fetchXYZGeom(self, job:Job) -> str: 
        if job.software not in [Software.orca, Software.crest]:
            raise Exception('Software not implemented')

        if job.software  == Software.orca:
            lines = self.readFile(job.xyzfile)
            xyz = ''.join(lines[2:])

        if job.software  == Software.crest:
            lines = self.readFile(job.xyzfile)
            xyz = ''.join(lines[2:])
        return xyz

    def sbatch(self, job:Job) -> None:
        if job.software in [Software.crest]:
            out, err = self.run(f'cd {job.path} && /opt/slurm-latest/bin/sbatch {job.infile}')
        elif job.software in [Software.psi4Script, Software.pyscf]:
            out, err = self.run(f'cd {job.path} && /opt/slurm-latest/bin/sbatch {job.path}/{job.name}.slm')
        return out, err

    def submitFiles(self, flags: str, files: str|list[str]) -> None:
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


    def pullJobEnergy(self, job:Job) -> Status:
        if job.software == Software.orca:
            out, err = self.run(f'cat {job.outfile} | grep \'Number of roots to be determined\\|:  E=  \\|****ORCA TERMINATED NORMALLY****\'')
            status = self.pullEnergyORCA(job, out)
        else:
            raise Exception(f'Job type {job.software} not implemented')
        return status

    def checkJobStatus(self, job:Job) -> Status:
        slurm = self._checkSLURM(job)
        slurmTo = {slurmStatus.RUNNING: Status.running,
                           slurmStatus.PENDING: Status.queued,
                           slurmStatus.TIMED_OUT: Status.timed_out}
        try:
            status = slurmTo[slurm]
        except KeyError:
            if job.software == Software.orca:
                status = self.checkOrcaStatus(job)

            elif job.software == Software.crest:
                status = self.checkCrestStatus(job)

            elif job.software == Software.psi4Script and job.job == Jobs.casscf:
                status = self.checkPsi4Status(job)

            elif job.software == Software.pyscf and job.job in [Jobs.casscf, Jobs.casscfOpt, Jobs.mp2Natorb]:
                status = self.checkPyscfStatus(job)
            else:
                raise Exception(f'Job type {job.software} not implemented')
        return status

    def buildJob(self, job:Job) -> None:
        if job.software not in [Software.orca, Software.crest, Software.psi4Script, Software.pyscf]:
            raise Exception(f'Job type {job.software} not implemented')

        self.run(f'mkdir -p {job.path}')

        if job.software == Software.psi4Script and job.job == Jobs.casscf:
            lines, err = self.run(f'cat "{job.catxyzpath}"')
            py, slm = psi4CasscfScan(job, lines[2:])
            self.writeFile(py, job.infile)
            self.writeFile(slm, f'{job.path}/{job.name}.slm')
        
        if job.software == Software.pyscf:
            if job.job == Jobs.casscf:
                lines, err = self.run(f'cat "{job.catxyzpath}"')
                py, slm = pyscfCasscfScan(job, lines[2:])
                self.writeFile(py, job.infile)
                self.writeFile(slm, f'{job.path}/{job.name}.slm')
            if job.job == Jobs.mp2Natorb:
                lines, err = self.run(f'cat "{job.catxyzpath}"')
                py, slm = pyscfMP2Natorbs(job, lines[2:])
                self.writeFile(py, job.infile)
                self.writeFile(slm, f'{job.path}/{job.name}.slm')

        if job.software == Software.pyscf and job.job == Jobs.casscfOpt:
            lines, err = self.run(f'cat "{job.catxyzpath}"')
            py, slm = pyscfCasscfOpt(job, lines[2:])
            self.writeFile(py, job.infile)
            self.writeFile(slm, f'{job.path}/{job.name}.slm')
    
        if job.software == Software.orca:
            lines, err = self.run(f'cat "{job.catxyzpath}"')
            self.writeFile(buildORCAOpt(job, lines), job.infile)

        elif job.software == Software.crest:
            self.writeFile(smiles2xyz(job.fluorophore.smiles), f'{job.path}/{job.fluorophore.name}.xyz')
            self.writeFile(buildCRESTOpt(job), job.infile)

        # submit block
        if job.submit == True and job.software in [Software.orca]:
            if job.partner == False:
                job.submitFlags += 'o'
            if job.time != 24:
                job.submitFlags += f' -H {time}'
            self.submitFiles(job.submitFlags, job.infile)
        elif job.submit == True and job.software in [Software.crest, Software.psi4Script, Software.pyscf]:
            out, err = self.sbatch(job)
            if err != ['']:
                print(err)
            else:
                print(job.fluorophore.name)
                print(out[0])
        return

    def checkCrestStatus(self, job:Job) -> Status:
        out, err = self.run(f'ls -lah {job.path}')
        started = False
        finished = False
        failed = False
        for line in out:
            if '.CHRG' in line:
                started = True

        if started == True:
            out, err = self.run(f'tail -n 100 {job.path}/slurm*.out')

        for line in out:
            if 'CREST terminated normally.' in line:
                finished = True
            elif 'Error termination.' in line:
                failed = True

        if started == False: return Status.queued
        elif finished == True: return Status.finished
        elif failed == True: return Status.failed
        elif started == True and finished == False: return Status.running

    def checkPsi4Status(self, job:Job) -> Status | None:
        out, err = self.run(f'ls -lah {job.path}')
        started = False
        finished = False
        failed = False
        queued = False
        none = True   
        for line in out:
            if f'{job.name}.py' in line:
                none = False
                queued = True
            if f'{job.name}.out' in line:
                started = True

        if started == True:
            out, err = self.run(f'tail -n 100 {job.path}/{job.name}.out')
            for line in out:
                if 'Exit status:' in line:
                    if 'Exit status: 0' in line:
                        finished = True
                    else: 
                        failed = True
        if none == True: return None
        elif failed == True: return Status.failed
        elif finished == True: return Status.finished
        elif started == True: return Status.running
        elif queued == True: return Status.queued
        
    def checkPyscfStatus(self, job:Job) -> Status | None:
        if job.job == Jobs.mp2Natorb:
            out, err = self.run(f'ls {job.path} | grep \'.molden.input\'')
            for line in out:
                if '.molden.input' in line:
                    return Status.finished

        out, err = self.run(f'ls {job.path} | grep slurm | tail -n 1')
        slurmOut = []
        for line in out: 
            if 'slurm' in line:
                slurmOut, err = self.run(f'tail -n 100 {job.path}/{line}')
        for slurmLine in slurmOut:
            if 'oom-kill event(s) in StepId=' in slurmLine:
                if job.job == Jobs.mp2Natorb: return Status.failed
                else: return Status.failed
            if 'DUE TO TIME LIMIT ***' in slurmLine:
                if job.job == Jobs.mp2Natorb: return Status.timed_out
                else: return Status.timed_out

        out, err = self.run(f'tail -n 100 {job.path}/{job.name}.out')
        if 'No such file or directory' in err[0]:
            return None
        else:
            out, err = self.run(f'tail -n 100 {job.path}/{job.name}.out')
            for line in out:
                if '	Exit status: ' in line:
                    if line.split()[2] == '0':

                        if job.job == Jobs.mp2Natorb: return Status.finished
                        else: return Status.finished
                    else:
                        if job.job == Jobs.mp2Natorb: return Status.failed
                        else: return Status.failed

    def checkOrcaStatus(self, job:Job) -> Status | None:
        out, err = self.run(f'tail -n 100 {job.path}/{job.name}/{job.name}.out')
        if 'No such file or directory' in err[0]:
            return None
        for line in out:
            if '****ORCA TERMINATED NORMALLY****' in line:
                return Status.finished
        return Status.failed


