from ..types.job import Job, PCM, Jobs, TDDFT

def buildQChemOpt(job:Job, xyz:list[str]) -> str:
    jobDict = {Jobs.opt:  'OPT', 
               Jobs.freq: 'FREQ', 
               Jobs.sp:   'SP',
               Jobs.ex:   'SP',
               Jobs.em:   'SP',
               Jobs.grad: 'GRADIENT'}
    try:
        jobType = jobDict[job.job]
    except KeyError:
        raise Exception("Job type not implemented")

    #################### TDDFT Params ###################
    triplets = 0 if job.triplets == TDDFT.Triplets.off else 1
    rpa = 0 if job.tda == TDDFT.TDA.on else 1 if job.tda == TDDFT.TDA.fitting else 2

    ##################### PCM Params ####################
    if job.pcm in [PCM.cpcm, PCM.lrpcm, PCM.sspcm]: 
        pcm = 'PCM'
    elif job.pcm == PCM.smd: 
        pcm = 'SMD'
    elif job.pcm == PCM.none:
        pcm = ''
    else:
        raise Exception("Solvation type not implemented.")

    PCMFiller = ''
    
    # Formalism
    formalismDict = {PCM.Formalism.cpcm:   'CPCM', 
                     PCM.Formalism.cosmo:  'COSMO', 
                     PCM.Formalism.iefpcm: 'IEFPCM',
                     PCM.Formalism.ssvpe:  'SSVPE'}
    try:
        pcmFormalism = formalismDict[job.pcm_form]
    except KeyError:
        raise Exception("PCM formalism not implemented")

    # Radii
    radiiDict = {PCM.Radii.uff:     'UFF', 
                 PCM.Radii.bondi:   'BONDI', 
                 PCM.Radii.default: ''}
    try:
        if job.pcm_radii != PCM.Radii.default:
            PCMFiller += f'    Radii                  {radiiDict[job.pcm_radii]}\n'
    except KeyError:
        raise Exception("PCM Radii not implemented")

    # VDWScale
    if job.pcm_VDWScale != 1.2:
        PCMFiller += f'    vdwScale               {job.pcm_VDWScale}\n'
    
    # Probe Radii
    if job.pcm_probe_radii != 0.0:
        PCMFiller += f'    SASradius              {job.pcm_probe_radii}\n'
    # Cavity
    cavityDict = {PCM.Cavity.sas:     'VDW_SAS', 
                  PCM.Cavity.ses:     'SES', 
                  PCM.Cavity.default: ''}
    try:
        if job.pcm_surfaceType != PCM.Cavity.default:
            PCMFiller += f'    SurfaceType            {cavityDict[job.pcm_surfaceType]}\n'
    except KeyError:
        raise Exception("Cavity Type not implemented")
    
    #####################################################
    ######################## Job 1 ######################
    #####################################################

    QChemInput =   '$molecule\n'
    QChemInput += f'{job.fluorophore.charge} {job.state.mult}\n'
    for line in xyz[2:]:
        if len(line.split()) > 2:
            QChemInput += f'{line}\n'
    QChemInput +=  '$end\n\n'

    remBlock =  '$rem\n'
    remBlock += f'    MEM_TOTAL             {job.mem.total_mb}\n'
    remBlock +=  '    GUI                   2\n'
    if jobType != 'SP': 
        remBlock += f'    JOBTYPE               {jobType}\n'
    remBlock += f'    EXCHANGE              {job.method.qchem}\n'
    remBlock += f'    BASIS                 {job.basis.qchem}\n'
    remBlock += f'    XC_GRID               {job.grid.qchem}\n'
    remBlock +=  '    SYMMETRY              false\n'
    if job.tddft == TDDFT.tddft:
        remBlock += f'    CIS_N_ROOTS           {job.nroots}\n'
        remBlock += f'    RPA                   {rpa}\n'
        remBlock += f'    CIS_TRIPLETS          {triplets}\n'
        remBlock +=  '    CIS_RELAXED_DENSITY   TRUE\n'
        remBlock +=  '    CIS_MAX_CYCLES        100\n'
        if job.job in [Jobs.freq, Jobs.grad, Jobs.opt]:
            remBlock += f'    CIS_STATE_DERIV       {job.state.root}\n'
    if pcm != '':
        remBlock += f'    SOLVENT_METHOD        {pcm}\n'
    QChemInput +=  remBlock
    QChemInput +=  '$end\n\n'

    if pcm != '':
        if job.solv in [PCM.smd]:
            solventBlock  =  '$smx\n'
            solventBlock += f'    solvent           {job.solv.smd}\n'
            solventBlock +=  '    print             2\n'
            solventBlock +=  '$end\n\n'


        if job.pcm in [PCM.cpcm, PCM.lrpcm, PCM.sspcm]:
            solventBlock  =  '$solvent\n'
            solventBlock += f'    Dielectric             {job.solv.e:.4f}\n'
            solventBlock += f'    OpticalDielectric      {job.solv.n**2:.4f}\n'
            solventBlock +=  '$end\n\n'

            # For cLR sxitation
            if job.pcm == PCM.sspcm and job.job == Jobs.ex:
                QChemInput +=  '$pcm\n'
                QChemInput += f'    Theory                {pcmFormalism}\n'
                QChemInput +=  '    ChargeSeparation      Marcus\n'
                QChemInput +=  '    StateSpecific         Perturb\n'
                QChemInput +=  PCMFiller
                QChemInput +=  '$end\n\n'

            # For cLR emission
            if job.pcm == PCM.sspcm and job.job == Jobs.em:
                QChemInput +=  '$pcm\n'
                QChemInput += f'    Theory                {pcmFormalism}\n'
                QChemInput +=  '    ChargeSeparation      Excited\n'
                QChemInput += f'    StateSpecific         {job.state.root}\n'
                QChemInput +=  PCMFiller
                QChemInput +=  '$end\n\n'

        # For LR-PCM, no $pcm block is needed

        QChemInput += solventBlock

    #####################################################
    ######################## Job 2 ######################
    #####################################################

    if (job.job == Jobs.em) and (pcm != ''):
        QChemInput +=  '@@@\n\n'

        QChemInput +=  '$molecule\n'
        QChemInput +=  '    READ\n'
        QChemInput +=  '$end\n\n'

        QChemInput +=  remBlock
        QChemInput +=  '    SCF_GUESS             READ\n'
        QChemInput +=  '$end\n\n'


        QChemInput +=  '$pcm\n'
        QChemInput += f'    Theory                {pcmFormalism}\n'
        QChemInput +=  '    StateSpecific         Marcus\n'
        QChemInput +=  PCMFiller
        QChemInput +=  '$end\n\n'

        QChemInput += solventBlock

    return QChemInput
