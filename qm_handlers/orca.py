from ..types.job import Job, Solvents, PCM, Jobs, Orbs, TDDFT, Methods
import numpy as np

def buildORCA(job:Job, xyz:list[str]) -> str:
    multiJob = False
    moinp = 'moread ' if job.mopath != '' else ''
    mostring = f'\n\n%moinp "{job.mopath}"' if job.mopath != '' else ''
    kdiisstring = 'kdiis ' if job.kdiis == True else ''
    soscfstring = 'soscf ' if job.soscf == True else 'nososcf '
    notrahstring = 'notrah ' if job.notrah == True else ''

    if job.method in [Methods.caspt2, Methods.nevpt2]:
        multiJob = True

    if job.pcm in [PCM.cpcm, PCM.smd, PCM.none]:
        cpcm = f'CPCM ' if (job.solv != Solvents.gas) or (job.pcm != PCM.none) else ''
    else:
        raise Exception("Solvation type not implemented.")

    cpcmeq = 'true' if job.eq == PCM.Eq.eq else 'false'

    if job.job in [Jobs.opt, Jobs.casscfOpt]:
        jobLine = 'Opt'
        if job.verytightopt: jobLine += ' verytightopt'
        else: jobLine += ' tightopt'
    elif job.job in [Jobs.casscf, Jobs.mp2Natorb, Jobs.sp]:
        jobLine = ''
    elif job.job in [Jobs.nevpt2, Jobs.caspt2]:
        jobLine = ''
        jobLine2 = ''
    elif job.job == Jobs.freq and job.pcm == PCM.smd:
        jobLine = 'NumFreq'
    elif job.job in [Jobs.freq, Jobs.casscfFreq]:
        jobLine = 'Freq'   
    else:
        raise Exception(f'Job type {job.job} not implemented.')

    riString = 'RIJCOSX ' if job.method not in [Methods.casscf, Methods.mp2, Methods.nevpt2, Methods.caspt2] else ''
    method = job.method.orca if job.method not in [Methods.casscf, Methods.caspt2] else 'CASSCF'

    if job.job in [Jobs.mp2Natorb, Jobs.nevpt2, Jobs.caspt2, Jobs.casscf, Jobs.casscfFreq]:
        riBasis = f'{job.basis.orca}/C '
    else:
        riBasis = f''

    ORCAInput = f'! {jobLine} {method} {riString}{job.basis.orca} {riBasis}tightscf {cpcm}{moinp}{kdiisstring}{soscfstring}{notrahstring}'
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

    if job.job == Jobs.opt and job.refJob.job == Jobs.freq:
        ORCAInput +=  '%geom\n'
        ORCAInput +=  '\tInHess Read\n'
        ORCAInput += f'\tInHessName "{job.refJob.path}/{job.refJob.name}/{job.refJob.name}.hess"\n'
        ORCAInput +=  'end\n\n'

    if job.job == Jobs.freq and job.restart:
        ORCAInput +=  '%freq\n'
        ORCAInput +=  '\trestart true\n'
        ORCAInput +=  'end\n\n'

    if job.scfstring != '': 
        ORCAInput +=  '%scf\n'
        ORCAInput += f'\t{job.scfstring}\n'
        ORCAInput +=  'end\n\n'

    if job.job == Jobs.mp2Natorb:
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

    if job.method in [Methods.casscf, Methods.caspt2, Methods.nevpt2]:
        nelec, norbs = job.casscf
        weights = ['0' for i in range(0, job.nroots)]
        weights[job.state.root] = '1'
        weightsString = ','.join(weights)

        if job.method in [Methods.caspt2, Methods.nevpt2]:
            ORCAInput +=  '%base "casscf"\n\n'
        ORCAInput +=  '%casscf\n'
        ORCAInput += f'\tnroots {job.nroots}\n'
        ORCAInput += f'\tnel {nelec}\n'
        ORCAInput += f'\tnorb {norbs}\n'
        ORCAInput += f'\tmult {job.state.mult}\n'
        ORCAInput +=  '\tMaxIter 500\n'
        ORCAInput += f'\tweights[0] = {weightsString}\n'
        if job.method == Methods.casscf and job.orbstep != 'SuperCI_PT (default)':
            ORCAInput += f'\tOrbStep {job.orbstep}\n'
        if job.method == Methods.casscf and job.switchstep != 'SuperCI_PT (default)':
            ORCAInput += f'\tSwitchStep {job.switchstep}\n'
        if job.method == Methods.casscf and job.switchconv != 0.03:
            ORCAInput += f'\tSwitchConv {job.switchconv:.2g}\n'
        if job.job != Jobs.casscfOpt: 
            ORCAInput +=  '\ttrafostep ri\n'
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

        ORCAInput += f'! {jobLine2} {job.method.orca} {riString}{job.basis.orca} {riBasis}verytightscf {cpcm} MOREAD noiter'
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

        if job.method in [Methods.caspt2, Methods.nevpt2]:
            ORCAInput +=  '%moinp "casscf.gbw"\n\n'
            ORCAInput +=  '%casscf\n'
            ORCAInput += f'\tnroots {job.nroots}\n'
            ORCAInput += f'\tnel {nelec}\n'
            ORCAInput += f'\tnorb {norbs}\n'
            ORCAInput += f'\tmult {job.state.mult}\n'
            ORCAInput +=  '\tMaxIter 500\n'
            # ORCAInput += f'\tweights[0] = {weightsString}\n'
            if job.job != Jobs.casscfOpt:
                ORCAInput +=  '\ttrafostep ri\n'
            if job.method == Methods.nevpt2:
                ORCAInput +=  '\tPTMethod sc_nevpt2\n'
            if job.method in [Methods.nevpt2, Methods.caspt2]:
                ORCAInput +=  '\t\tPTSettings\n'
                ORCAInput +=  '\t\tMaxIter 200\n'
                ORCAInput +=  '\t\tD4TPre 1e-14\n'
                # ORCAInput += f'\t\tselectedRoots[0] = {perturbedString}\n'
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

    splitPoint = 0
    startList = 0
    if job.job == Jobs.opt:
        for count, line in enumerate(out):
            if 'THE OPTIMIZATION HAS CONVERGED ' in line:
                splitPoint = count
    out = out[splitPoint:]
    
    for state in range(1, nroots+1):
        if job.job not in [Jobs.casscf, Jobs.casscfOpt, Jobs.caspt2, Jobs.nevpt2]:
            stateList += [f'STATE{state:3}:  E=  ']
        else:
            stateList += [f'ROOT{state:4}:  E=  ']
    for count, line in enumerate(out):
        if 'FINAL SINGLE POINT ENERGY' in line:
            e = float(line.split()[4])
        elif 'ABSORPTION SPECTRUM VIA TRANSITION ELECTRIC DIPOLE MOMENTS' in line:
            startList = count+5
        elif 'ABSORPTION SPECTRUM' in line and job.job in [Jobs.casscf, Jobs.casscfOpt, Jobs.caspt2, Jobs.nevpt2]:
            startList = count+5
        for stateCheck in stateList:
            if stateCheck in line:
                e_trans += [float(line.split()[5])]
    for line in out[startList:startList+nroots-1]:
        f += [float(line.split()[7])]
        tx = float(line.split()[9])
        ty = float(line.split()[10])
        tz = float(line.split()[11])
        t += [(tx, ty, tz)]
    electrons = extract_electrons(out)
    occ = extract_occ(out)
    ref = build_ref(electrons, occ, job.state.root)
    m = m_diag(ref, occ)

    return e, e_trans, f, t, m

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

def m_diag(occ_ref:list[float]|np.ndarray, occ_no:list[float]|np.ndarray) -> float:
    if type(occ_ref) == list: occ_ref = np.array(occ_ref)
    if type(occ_no) == list: occ_no = np.array(occ_no)

    docc = occ_no[np.equal(occ_ref, 2.)].tolist()
    socc = occ_no[np.equal(occ_ref, 1.)].tolist()
    uocc = occ_no[np.equal(occ_ref, 0.)].tolist()
    soccm1 = np.abs(np.subtract(socc, 1))
    m = 0.5*(2-min(docc)+np.sum(soccm1)+max(uocc))
    return round(m, 3)


def build_ref(electrons:int, occ:list[float], state:int) -> list[float]:
    ref = []
    while electrons > 0:
        if electrons >= 2:
            ref += [2.]
            electrons -= 2
        else:
            ref += [1.]
            electrons -= 1
    for i in range(len(occ)-len(ref)):
        ref += [0.]

    if state == 1:
        homo = 0
        for count, occ in enumerate(ref):
            if occ < 1.:
                lumo = count
                homo = count-1
                break
        ref[homo] -= 1.
        ref[lumo] += 1.
    return ref

def extract_occ(lines:list[str]) -> list[float]:
    for count, line in enumerate(lines):
        if '  NO   OCC          E(Eh)            E(eV) ' in line:
            start = count+1
            occs = []
            for orbs in lines[start:]:
                try:
                    occs += [float(orbs.split()[1])]
                except IndexError:
                    break
    return occs

def extract_electrons(lines:list[str]) -> int:
    for line in lines:
        if 'Total number of electrons' in line:
            return int(line.split()[5])