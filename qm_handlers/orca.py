from ..types.job import Job
from ..types.jobs import Jobs
from ..types.job import Solvents
from ..types.job import PCM
from ..functions import evToNm

def buildORCAOpt(job:Job, xyz:list[str]) -> str:
    moinp = 'moread ' if job.mopath != '' else ''
    mostring = f'\n\n%moinp "{job.mopath}"' if job.mopath != '' else ''
    kdiisstring = 'kdiis ' if job.kdiis == True else ''
    soscfstring = 'soscf ' if job.soscf == True else 'nososcf '
    notrahstring = 'notrah ' if job.notrah == True else ''

    if (job.pcm == PCM.cpcm or job.pcm == PCM.smd or job.pcm == PCM.none):
        cpcm = f'CPCM ' if job.solv != Solvents.gas else ''
    else:
        raise Exception("Solvation type not implemented.")

    cpcmeq = 'true' if job.eq == PCM.Eq.eq else 'false'

    if job.job == Jobs.opt:
        jobLine = 'Opt tightopt'
    else:
        raise Exception(f'Job type {job.job} not implemented.')

    ORCAInput = f'! {jobLine} {job.method.orca} RIJCOSX {job.basis.orca} tightscf {cpcm}{moinp}{kdiisstring}{soscfstring}{notrahstring}'
    ORCAInput += mostring
    ORCAInput += f'\n\n%maxcore {job.mem.per_core_mb}\n\n%pal\n\tnprocs {job.procs}\nend\n\n'
    if (job.solv != 'gas' and job.pcm == PCM.smd): ORCAInput += f'%cpcm\n\tsmd true\n\tSMDSolvent "{job.solv.smd}"\nend\n\n'
    elif (job.solv != 'gas' and job.pcm == PCM.cpcm): ORCAInput += f'%cpcm\n\tepsilon {job.solv.e}\n\trefrac {job.solv.n}\nend\n\n'

    ORCAInput += job.grid.orca
    if job.scfstring != '': ORCAInput += f'%scf\n\t{job.scfstring}\nend\n\n'
    ORCAInput += f'%tddft\n\tnroots {job.nroots}\n\tIRoot {job.state.root}\n\tcpcmeq {cpcmeq}\n\ttda false\nend\n\n'
    if job.xyzpath == '':
        ORCAInput += f'* xyz {job.fluorophore.charge} {job.state.mult}\n'
        
        for line in xyz[2:]:
            if len(line.split()) > 2:
                ORCAInput += f'{line}\n'
        ORCAInput += '*\n\n'
    else:
        ORCAInput += f'* xyzfile {job.fluorophore.charge} {job.fluorophore.mult} {job.xyzpath}\n\n'
    

    return ORCAInput

def pullEnergyORCA(job:Job, out:list[str]):
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

    if complete != True:
        return
    else:
        for i in results[-nroots:]:
            excitations += [float(i.split()[5])]
            
        excitations = excitations[-nroots:]
        return excitations, evToNm(excitations)

            