from ..types.job import Job, Solvents, PCM, Jobs, Orbs, TDDFT, Methods, States, Fluorophores, MetaJobs
from ..functions import nmToEv
import numpy as np


def buildORCA(job: Job, xyz: list[str]) -> str:
    multiJob = False
    moinp = 'moread ' if job.mopath != '' else ''
    mostring = f'\n\n%moinp "{job.mopath}"' if job.mopath != '' else ''
    kdiisstring = 'kdiis ' if job.kdiis else ''
    soscfstring = 'soscf ' if job.soscf else 'nososcf '
    notrahstring = 'notrah ' if job.notrah else ''
    frozencore = 'nofrozencore ' if job.fluorophore in [Fluorophores.bpa] else ''

    # Not currently used since no multi-job runs are needed

    # if job.method in []:
    #     multiJob = True

    if job.pcm in [PCM.cpcm, PCM.smd, PCM.none]:
        cpcm = 'CPCM ' if (job.solv != Solvents.gas) or (job.pcm != PCM.none) else ''
    else:
        raise Exception("Solvation type not implemented.")

    cpcmeq = 'true' if job.eq == PCM.Eq.eq else 'false'

    if job.job in [Jobs.opt, Jobs.casscfOpt]:
        jobLine = 'Opt'
        if job.verytightopt:
            jobLine += ' verytightopt'
        else:
            jobLine += ' tightopt'
    elif job.job in [Jobs.casscf, Jobs.mp2Natorb, Jobs.sp, Jobs.nevpt2, Jobs.caspt2, Jobs.pol]:
        jobLine = ''
    elif job.job in [Jobs.freq] and job.pcm == PCM.smd:
        jobLine = 'NumFreq'
    elif job.job in [Jobs.freq, Jobs.casscfFreq]:
        jobLine = 'Freq'
    elif job.job in [Jobs.esd]:
        if job.state == States.s0:
            jobLine = 'ESD(ABS)'
        else:
            jobLine = 'ESD(FLUOR)'
    else:
        raise Exception(f'Job type {job.job} not implemented.')

    riString = 'RIJCOSX ' if job.method not in [Methods.casscf, Methods.mp2, Methods.nevpt2, Methods.caspt2] else ''

    # exception only needed for setting the fist job in multijob
    method = job.method.orca if job.method not in [] else 'CASSCF'

    if job.job in [Jobs.mp2Natorb, Jobs.nevpt2, Jobs.caspt2, Jobs.casscf, Jobs.casscfFreq]:
        riBasis = f'{job.basis.orca}/C '
    else:
        riBasis = ''

    ORCAInput = f'! {jobLine}{" " if jobLine != "" else ""}{method} {riString}{job.basis.orca} {riBasis}tightscf {cpcm}{moinp}{kdiisstring}{soscfstring}{notrahstring}{frozencore}'
    ORCAInput += mostring
    ORCAInput += '\n\n'
    ORCAInput += f'%maxcore {job.mem.per_core_mb}\n'
    ORCAInput += '\n%pal\n'
    ORCAInput += f'\tnprocs {job.procs}\n'
    ORCAInput += 'end\n\n'

    if (job.solv != 'gas' and job.pcm == PCM.smd):
        ORCAInput += '%cpcm\n'
        ORCAInput += '\tsmd true\n'
        ORCAInput += f'\tSMDSolvent "{job.solv.smd}"\n'
        ORCAInput += 'end\n\n'

    elif (job.solv != 'gas' and job.pcm == PCM.cpcm):
        ORCAInput += '%cpcm\n'
        ORCAInput += f'\tepsilon {job.solv.e}\n'
        ORCAInput += f'\trefrac {job.solv.n}\n'
        ORCAInput += 'end\n\n'

    ORCAInput += job.grid.orca

    ################ Job type blocks ################
    if job.job in [Jobs.opt, Jobs.casscfOpt]:
        ORCAInput += '%geom\n'
        if job.inhess:
            ORCAInput += '\tInHess Read\n'
            ORCAInput += f'\tInHessName "{job.refJob.path}/{job.refJob.name}/{job.refJob.name}.hess"\n'
        if job.calchess:
            ORCAInput += '\tCalc_Hess True\n'
        if job.recalchess > 0:
            ORCAInput += f'\tRecalc_Hess {job.recalchess}\n'
        if (job.calchess or job.recalchess) and job.pcm == PCM.smd:
            ORCAInput += '\tNumHess True\n'
        ORCAInput += 'end\n\n'

    if job.job == Jobs.mp2Natorb:
        ORCAInput += '%mp2\n'
        ORCAInput += '\tNatOrbs true\n'
        ORCAInput += '\tDensity relaxed\n'
        ORCAInput += 'end\n\n'

    if job.job in [Jobs.freq, Jobs.casscfFreq] and job.restart:
        ORCAInput += '%freq\n'
        ORCAInput += '\trestart true\n'
        ORCAInput += 'end\n\n'

    if job.scfstring != '':
        ORCAInput += '%scf\n'
        ORCAInput += f'\t{job.scfstring}\n'
        ORCAInput += 'end\n\n'

    if job.job == Jobs.pol:
        ORCAInput += '%elprop\n'
        ORCAInput += '\tPolar 1\n'
        ORCAInput += 'end\n\n'

    if job.job == Jobs.esd:
        ORCAInput += '%esd\n'
        ORCAInput += f'\tgshessian "{job.esdLowerJob.path}/{job.esdLowerJob.name}/{job.esdLowerJob.name}.hess"\n'
        ORCAInput += f'\teshessian "{job.esdHigherJob.path}/{job.esdHigherJob.name}/{job.esdHigherJob.name}.hess"\n'
        # ORCAInput += '\tdoht true\n'
        ORCAInput += '\tlines delta\n'
        ORCAInput += '\tunit ev\n'
        # ORCAInput += '\tusej true\n'
        ORCAInput += '\tprintlevel high\n'
        ORCAInput += 'end\n\n'

    ################ Method type blocks ################
    if (job.tddft == TDDFT.tddft and job.state != States.s0) or job.job == Jobs.esd:
        if job.tda == TDDFT.TDA.off:
            tdaLine = '\ttda false'
        ORCAInput += '%tddft\n'
        ORCAInput += f'\tnroots {job.nroots}\n'
        ORCAInput += f'\tcpcmeq {cpcmeq}\n'
        ORCAInput += f'{tdaLine}\n'
        if (job.job == Jobs.esd and job.state == States.s0):
            ORCAInput += f'\tiroot {job.esdState.root}\n'
        else:
            ORCAInput += f'\tiroot {job.state.root}\n'
        ORCAInput += 'end\n\n'

    if job.method in [Methods.casscf, Methods.caspt2, Methods.nevpt2]:
        nelec, norbs = job.casscf
        weights = ['0' for i in range(0, job.nroots)]
        weights[job.state.root] = '1'
        weightsString = ','.join(weights)

        ORCAInput += '%casscf\n'
        ORCAInput += f'\tnroots {job.nroots}\n'
        ORCAInput += f'\tnel {nelec}\n'
        ORCAInput += f'\tnorb {norbs}\n'
        ORCAInput += f'\tmult {job.state.mult}\n'
        ORCAInput += '\tMaxIter 500\n'
        ORCAInput += '\tSwitchIter 500\n'
        if not job.sa:
            ORCAInput += f'\tweights[0] = {weightsString}\n' # CASPT methods I think need a SA inpur wavefn
        if job.orbstep != 'SuperCI_PT (default)':
            ORCAInput += f'\tOrbStep {job.orbstep}\n'
        if job.switchstep != 'SuperCI_PT (default)':
            ORCAInput += f'\tSwitchStep {job.switchstep}\n'
        if job.switchconv != 0.03:
            ORCAInput += f'\tSwitchConv {job.switchconv:.2g}\n'
        if job.job != Jobs.casscfOpt:
            ORCAInput += '\ttrafostep ri\n'
        if job.method == Methods.nevpt2:
            ORCAInput += '\tPTMethod sc_nevpt2\n'
        elif job.method == Methods.caspt2:
            ORCAInput += '\tPTMethod fic_caspt2k\n'
        if job.method in [Methods.nevpt2, Methods.caspt2]:
            ORCAInput += '\tPTSettings\n'
            if job.metajob == MetaJobs.qdnevpt2:
                ORCAInput += '\t\tQDType QD_VanVleck\n'
            ORCAInput += '\t\tMaxIter 200\n'
            ORCAInput += '\t\tD4TPre 1e-14\n'
            ORCAInput += '\tend\n'
        ORCAInput += 'end\n\n'

    if job.xyzpath == '':
        ORCAInput += f'* xyz {job.fluorophore.charge} {job.state.mult}\n'

        for line in xyz[2:]:
            if len(line.split()) > 2:
                ORCAInput += f'{line}\n'
        ORCAInput += '*\n\n'
    else:
        ORCAInput += f'* xyzfile {job.fluorophore.charge} {job.fluorophore.mult} {job.xyzpath}\n\n'

    # Not currently used since no multi-job runs are needed

    # if multiJob:
    #     ORCAInput += '$new_job\n\n'
    #     ORCAInput += f'! {jobLine2} {job.method.orca} {riString}{job.basis.orca} {riBasis}verytightscf {cpcm} MOREAD noiter'
    #     ORCAInput += '\n\n'

    #     if (job.solv != 'gas' and job.pcm == PCM.smd):
    #         ORCAInput += '%cpcm\n'
    #         ORCAInput += '\tsmd true\n'
    #         ORCAInput += f'\tSMDSolvent "{job.solv.smd}"\n'
    #         ORCAInput += 'end\n\n'

    #     elif (job.solv != 'gas' and job.pcm == PCM.cpcm):
    #         ORCAInput += '%cpcm\n'
    #         ORCAInput += f'\tepsilon {job.solv.e}\n'
    #         ORCAInput += f'\trefrac {job.solv.n}\n'
    #         ORCAInput += 'end\n\n'

    #     if job.xyzpath == '':
    #         ORCAInput += f'* xyz {job.fluorophore.charge} {job.state.mult}\n'

    #         for line in xyz[2:]:
    #             if len(line.split()) > 2:
    #                 ORCAInput += f'{line}\n'
    #         ORCAInput += '*\n\n'
    #     else:
    #         ORCAInput += f'* xyzfile {job.fluorophore.charge} {job.fluorophore.mult} {job.xyzpath}\n\n'

    return ORCAInput


def pullORCA(job: Job, out: list[str]):
    if job.job in [Jobs.freq, Jobs.casscfFreq]:
        return pullORCA_Freq(job, out)
    elif job.job in [Jobs.ex, Jobs.em, Jobs.td, Jobs.casscf, Jobs.casscfOpt, Jobs.opt, Jobs.caspt2, Jobs.nevpt2]:
        return pullORCA_En(job, out)
    elif job.job in [Jobs.pol]:
        return pullORCA_Pol(job, out)
    else:
        raise Exception(f'Job type {job.software} {job.job} not implemented')


def pullORCA_En(job: Job, out: list[str]) -> tuple[float, list[float], list[float], tuple[float, float, float]]:
    e_trans = []
    f = []
    t = []
    e = 0
    nroots = job.nroots
    stateList = []

    splitPoint = 0
    startList = 0
    if job.job == Jobs.opt:
        for count, line in enumerate(out):
            if 'THE OPTIMIZATION HAS CONVERGED ' in line:
                splitPoint = count
    out = out[splitPoint:]

    for state in range(1, nroots):
        if job.job not in [Jobs.casscf, Jobs.casscfOpt, Jobs.caspt2, Jobs.nevpt2]:
            stateList += [f'STATE{state:3}:  E=  ']
            e_trans += [0.0]
        else:
            stateList += [f'ROOT{state:4}:  E=  ']
            e_trans += [0.0]
    for count, line in enumerate(out):
        if 'FINAL SINGLE POINT ENERGY' in line:
            e = float(line.split()[4])
        elif 'ABSORPTION SPECTRUM VIA TRANSITION ELECTRIC DIPOLE MOMENTS' in line:
            startList = count + 5
            e_trans = []
        elif 'ABSORPTION SPECTRUM' in line and job.job in [Jobs.casscf, Jobs.casscfOpt, Jobs.caspt2, Jobs.nevpt2]:
            startList = count + 5

        for count, stateCheck in enumerate(stateList):
            if stateCheck in line:
                e_trans[count] = float(line.split()[5])

    if job.job in [Jobs.caspt2, Jobs.nevpt2]:
        e_trans = []
    for line in out[startList:startList + nroots - 1]:
        if job.job in [Jobs.caspt2, Jobs.nevpt2]:
            e_trans += [nmToEv(float(line.split()[6]))]
        f += [float(line.split()[7])]
        tx = float(line.split()[9])
        ty = float(line.split()[10])
        tz = float(line.split()[11])
        t += [(tx, ty, tz)]
    m, weights, configurations, occupations = m_diag(out, job.state.root)

    return e, e_trans, f, t, m


def pullORCA_Freq(job: Job, out: list[str]) -> tuple[float, float, float]:
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


def pullORCA_Pol(job: Job, out: list[str]) -> tuple[float, list[float], np.array]:
    pol = []
    iso = 0
    diag = []
    tensorLine = 0
    diagLine = 0
    for count, line in enumerate(out):
        if 'The raw cartesian tensor' in line:
            tensorLine = count + 1
        if 'diagonalized tensor:' in line:
            diagLine = count + 1
        elif 'Isotropic polarizability' in line:
            iso = float(line.split()[3])

    if tensorLine == 0 or diagLine == 0:
        raise Exception('Pol job not completed!')

    split = out[diagLine].split()
    diag = [float(split[0]), float(split[1]), float(split[2])]

    for line in out[tensorLine:tensorLine + 3]:
        split = line.split()
        pol += [[float(split[0]), float(split[1]), float(split[2])]]

    return iso, diag, pol

def extract_occ(lines: list[str], root: int) -> list[float]:
    for line in lines:
        nevpt2 = False
        if 'nevpt2' in line:
            nevpt2 = True
            break
        
    if nevpt2:
        searchline = f'Reading QDVector (MULT=  1, ROOT=  {root})'
    else:
        searchline = f'ROOT   {root}:'

    startline = 0
    for count, line in enumerate(lines):
        if searchline in line:
            startline = count+1
            if nevpt2:
                break
    
    configurations = []
    weights = []
    for line in lines[startline:]:
        if line.split()[1] == '[':
            weights += [float(line.split()[0])]
            configurations += [[int(i) for i in list((line.split()[3]))]]
        else:
            break
    weights_np = np.array(weights).reshape(len(weights), 1)
    configurations_np = np.array(configurations)
    occupations = np.einsum('ij, ik->j', configurations_np, weights_np)
    return weights, configurations, occupations

        
def m_diag(out: list[str], root: int) -> int:
    weights, configurations, occupations = extract_occ(out, root)
    base_occ = configurations[0]
    DONO = occupations[np.equal(base_occ, 2.)]
    SONO = occupations[np.equal(base_occ, 1.)]
    DUNO = occupations[np.equal(base_occ, 0.)]
    MCDONO = min(DONO)
    MCDUNO = max(DUNO)
    M = (2 - MCDONO + np.sum(np.absolute(np.subtract(1, SONO))) + MCDUNO)/2
    return round(M, 3), weights, configurations, occupations