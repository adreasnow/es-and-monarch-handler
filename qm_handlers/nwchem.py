from ..types.job import Job, Jobs, PCM, TDDFT


def buildNW(job: Job, xyz: list[str]) -> str:
    NWInput = 'echo\n'
    NWInput += f'memory total {job.mem/job.procs} gb\n\n'
    NWInput += 'start molecule\n'
    NWInput += f'charge {job.fluorophore.charge}\n'
    NWInput += 'geometry print xyz\n'
    NWInput += 'symmetry group c1\n'
    for line in xyz[2:]:
        if len(line.split()) > 2:
            NWInput += f'{line}\n'
    NWInput += 'end\n\n'
    NWInput += 'basis "ao basis" spherical\n'
    NWInput += f'  * library {job.basis.nwchem}\n'
    NWInput += 'end\n\n'
    NWInput += 'basis "cd basis" spherical\n'
    NWInput += '  * library "Ahlrichs Coulomb Fitting"\n'
    NWInput += 'end\n\n'
    NWInput += 'dft\n'
    NWInput += f'  xc {job.method.nwchem}\n'
    NWInput += f'  grid {job.grid.nwchem}\n'
    NWInput += 'end\n\n'

    ############### TD-DFT Section ###############
    if job.tddft == TDDFT.tddft:
        NWInput += 'tddft\n'
        NWInput += '  rpa\n'
        NWInput += '  algorithm 1\n'
        NWInput += f'  nroots {job.nroots}\n'
        if job.triplets == TDDFT.Triplets.off:
            NWInput += '  notriplet\n'
        NWInput += '  targetsym a\n'
        NWInput += f'  target {job.state.root}\n'
        NWInput += '  civec\n'
        NWInput += '  grad\n'
        NWInput += f'    root {job.state.root}\n'
        NWInput += '  end\n'
        NWInput += 'end\n'

    ################ OPT Section ################
    if job.job == Jobs.opt:
        NWInput += 'driver\n'
        NWInput += '  xyz geom\n'
        NWInput += 'end\n\n'

    if job.pcm in [PCM.vem, PCM.smd, PCM.smssp]:
        NWInput += 'cosmo\n'
        NWInput += '  minbem 3\n'
        NWInput += '  ificos 1\n'
        NWInput += '  do_gasphase false\n'
        if job.pcm in [PCM.smd, PCM.smssp]:
            NWInput += '  do_cosmo_smd true\n'
            NWInput += f'  solvent {job.solv.nwchem}\n'
        if job.pcm in [PCM.vem, PCM.smssp]:
            if job.job == Jobs.ex:
                NWInput += '  do_cosmo_vem 1\n'
            if job.job == Jobs.em:
                NWInput += '  do_cosmo_vem 2\n'
            if job.pcm == PCM.smssp:
                NWInput += f'  polgs_cosmo_vem {job.gspol}\n'
                NWInput += f'  poles_cosmo_vem {job.espol}\n'
                NWInput += 'end\n\n'

    ############### TD-DFT Jobs ###############
    if job.job == Jobs.opt and job.tddft == TDDFT.tddft:
        NWInput += 'task tddft optimize\n'
    elif job.job == Jobs.freq and job.tddft == TDDFT.tddft:
        NWInput += 'task tddft freq\n'
    elif job.job == Jobs.ex and job.tddft == TDDFT.tddft:
        NWInput += 'task tddft gradient\n'
    elif job.job == Jobs.em and job.tddft == TDDFT.tddft:
        NWInput += 'task tddft energy\n'

    ################ DFT Jobs @###############
    elif job.job == Jobs.opt and job.tddft == TDDFT.none:
        NWInput += 'task dft optimize\n'
    elif job.job == Jobs.freq and job.tddft == TDDFT.none:
        NWInput += 'task dft freq\n'

    return NWInput
