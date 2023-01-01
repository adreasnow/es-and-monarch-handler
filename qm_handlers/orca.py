from ..types.job import Job, Solvents, PCM, Jobs, Orbs, TDDFT, Methods
from ..functions import evToNm

def buildORCA(job:Job, xyz:list[str]) -> str:
    multiJob = False
    moinp = 'moread ' if job.mopath != '' else ''
    mostring = f'\n\n%moinp "{job.mopath}"' if job.mopath != '' else ''
    kdiisstring = 'kdiis ' if job.kdiis == True else ''
    soscfstring = 'soscf ' if job.soscf == True else 'nososcf '
    notrahstring = 'notrah ' if job.notrah == True else ''

    if job.method in [Methods.casscf, Methods.caspt2, Methods.nevpt2]:
        multiJob = True

    if job.pcm in [PCM.cpcm, PCM.smd, PCM.none]:
        cpcm = f'CPCM ' if (job.solv != Solvents.gas) or (job.pcm != PCM.none) else ''
    else:
        raise Exception("Solvation type not implemented.")

    cpcmeq = 'true' if job.eq == PCM.Eq.eq else 'false'

    if job.job == Jobs.opt:
        jobLine = 'Opt tightopt'
    elif job.job in [Jobs.nevpt2, Jobs.caspt2, Jobs.casscf, Jobs.mp2Natorb]:
        jobLine = ''
        jobLine2 = ''
    elif job.job == Jobs.casscfOpt:
        jobLine = ''
        jobLine2 = 'Opt tightopt'
    elif job.job == Jobs.freq:
        jobLine = 'Freq'
    else:
        raise Exception(f'Job type {job.job} not implemented.')

    riString = 'RIJCOSX ' if job.method not in [Methods.casscf, Methods.mp2, Methods.nevpt2, Methods.caspt2] else ''
    method = job.method.orca if job.method not in [Methods.casscf, Methods.caspt2, Methods.nevpt2] else 'RI-MP2 nofrozencore'

    if job.job in [Jobs.mp2Natorb, Jobs.casscfOpt] :
        riBasis1 = f'{job.basis.orca}/C '
        riBasis2 = f''
    elif job.job in [Jobs.nevpt2, Jobs.caspt2, Jobs.casscf]:
        riBasis1 = f'{job.basis.orca}/C '
        riBasis2 = f'{job.basis.orca}/C '
    else:
        riBasis1 = f''
        riBasis2 = f''

    ORCAInput = f'! {jobLine} {method} {riString}{job.basis.orca} {riBasis1}tightscf {cpcm}{moinp}{kdiisstring}{soscfstring}{notrahstring}'
    ORCAInput += mostring
    ORCAInput += '\n\n'
    ORCAInput += f'%maxcore {job.mem.per_core_mb}\n'
    ORCAInput +=  '\n%pal\n'
    ORCAInput += f'\tnprocs {job.procs}\n'
    ORCAInput +=  'end\n\n'
    
    if (job.solv != 'gas' and job.pcm == PCM.smd): 
        ORCAInput +=  '%cpcm\n'
        ORCAInput +=  '\tsmd true\n'
        ORCAInput += f'\tSMDSolvent "{job.solv.smd}"\n'
        ORCAInput +=  'end\n\n'

    elif (job.solv != 'gas' and job.pcm == PCM.cpcm): 
        ORCAInput +=  '%cpcm\n'
        ORCAInput += f'\tepsilon {job.solv.e}\n'
        ORCAInput += f'\trefrac {job.solv.n}\n'
        ORCAInput +=  'end\n\n'

    ORCAInput += job.grid.orca

    if job.scfstring != '': 
        ORCAInput +=  '%scf\n'
        ORCAInput += f'\t{job.scfstring}\n'
        ORCAInput +=  'end\n\n'

    if method == 'RI-MP2 nofrozencore':
        ORCAInput +=  '%base "mp2"\n\n'
        ORCAInput +=  '%mp2\n'
        ORCAInput +=  '\tNatOrbs true\n'
        ORCAInput +=  '\tDensity relaxed\n'
        ORCAInput +=  'end\n\n'


    if job.tddft == TDDFT.tddft: 
        if job.tda == TDDFT.TDA.off:
             tdaLine = '\n\ttda false'
        ORCAInput +=  '%tddft\n'
        ORCAInput += f'\tnroots {job.nroots}\n'
        ORCAInput += f'\tIRoot {job.state.root}\n'
        ORCAInput += f'\tcpcmeq {cpcmeq}{tdaLine}\n'
        ORCAInput +=  'end\n\n'

    if job.xyzpath == '':
        ORCAInput += f'* xyz {job.fluorophore.charge} {job.state.mult}\n'
        
        for line in xyz[2:]:
            if len(line.split()) > 2:
                ORCAInput += f'{line}\n'
        ORCAInput += '*\n\n'
    else:
        ORCAInput += f'* xyzfile {job.fluorophore.charge} {job.fluorophore.mult} {job.xyzpath}\n\n'

    if multiJob:
        ORCAInput +=  '$new_job\n\n'

        ORCAInput += f'! {jobLine2} {job.method.orca} {riString}{job.basis.orca} {riBasis2}tightscf {cpcm} MOREAD {kdiisstring}{soscfstring}{notrahstring}'
        ORCAInput += '\n\n'

        if (job.solv != 'gas' and job.pcm == PCM.smd): 
            ORCAInput +=  '%cpcm\n'
            ORCAInput +=  '\tsmd true\n'
            ORCAInput += f'\tSMDSolvent "{job.solv.smd}"\n'
            ORCAInput +=  'end\n\n'

        elif (job.solv != 'gas' and job.pcm == PCM.cpcm): 
            ORCAInput +=  '%cpcm\n'
            ORCAInput += f'\tepsilon {job.solv.e}\n'
            ORCAInput += f'\trefrac {job.solv.n}\n'
            ORCAInput +=  'end\n\n'

        if job.method in [Methods.casscf, Methods.caspt2, Methods.nevpt2]:
            nelec, norbs = job.casscf
            weights = ['0' for i in range(0, job.nroots)]
            weights[job.state.root] = '1'
            weightsString = ','.join(weights)

            perturbedString = weights = ['0' for i in range(0, job.nroots)]
            for i in range(0, job.perturbedRoots):
                perturbedString[i] = '1'
            perturbedString = ','.join(weights)

            ORCAInput +=  '%moinp "mp2.gbw"\n\n'
            ORCAInput +=  '%casscf\n'
            ORCAInput += f'\tnroots {job.nroots}\n'
            ORCAInput += f'\tnel {nelec}\n'
            ORCAInput += f'\tnorb {norbs}\n'
            ORCAInput += f'\tmult {job.state.mult}\n'
            ORCAInput +=  '\tMaxIter 500\n'
            ORCAInput += f'\tweights[0] = {weightsString}\n'
            if job.method == Methods.nevpt2:
                ORCAInput +=  '\tPTMethod sc_nevpt2\n'
            if job.method in [Methods.nevpt2, Methods.caspt2]:
                ORCAInput +=  '\t\tPTSettings\n'
                ORCAInput += f'\t\tselectedRoots[0] = {perturbedString}\n'
                if job.method == Methods.nevpt2:
                    ORCAInput +=  'QDType QD_VanVleck\n'
                ORCAInput +=  '\tend\n'
            ORCAInput +=  'end\n\n'

            if job.xyzpath == '':
                ORCAInput += f'* xyz {job.fluorophore.charge} {job.state.mult}\n'
                
                for line in xyz[2:]:
                    if len(line.split()) > 2:
                        ORCAInput += f'{line}\n'
                ORCAInput += '*\n\n'
            else:
                ORCAInput += f'* xyzfile {job.fluorophore.charge} {job.fluorophore.mult} {job.xyzpath}\n\n'

    return ORCAInput

def pullORCA(job:Job, out:list[str]):
    if job.job in [Jobs.freq]:
        return pullORCA_Freq(job, out)
    elif job.job in [Jobs.ex, Jobs.em, Jobs.td, Jobs.casscf, Jobs.casscfOpt, Jobs.opt]:
        return pullORCA_En(job, out)
    else:
        raise Exception(f'Job type {job.software} {job.job} not implemented')

def pullORCA_En(job:Job, out:list[str]) -> tuple[float, 
                                                 list[float], 
                                                 list[float], 
                                                 tuple[float, float, float]
                                                ]:
    e_trans = []
    f = []
    t = []
    e = 0
    nroots = job.nroots
    stateList = []

    if job.job == Jobs.opt:
        for count, line in enumerate(out):
            if 'THE OPTIMIZATION HAS CONVERGED ' in line:
                split = count
    out = out[split:-1]
    
    for state in range(1, nroots+1):
        stateList += [f'STATE{state:3}:  E=  ']

    for count, line in enumerate(out):
        if 'FINAL SINGLE POINT ENERGY' in line:
            e = float(line.split()[4])
        elif 'ABSORPTION SPECTRUM VIA TRANSITION ELECTRIC DIPOLE MOMENTS' in line:
            startList = count+5
        for stateCheck in stateList:
            if stateCheck in line:
                e_trans += [float(line.split()[5])]
    
    for line in out[startList:startList+nroots]:
        f += [float(line.split()[3])]
        tx = float(line.split()[4])
        ty = float(line.split()[5])
        tz = float(line.split()[6])
        t += [(tx, ty, tz)]

    return e, e_trans, f, t

def pullORCA_Freq(job:Job, out:list[str]) -> tuple[float, float, float]:
    neg = 0
    e = 0
    zpve = 0
    for line in out:
        if '***imaginary mode***' in line:
            neg += 1
        elif 'Zero point energy' in line:
            zpve = float(line.split()[4])
        elif 'Electronic energy' in line:
            e = float(line.split()[3])
    return e, zpve, neg