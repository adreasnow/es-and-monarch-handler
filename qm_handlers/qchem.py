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
        pcm_radii = radiiDict[job.pcm_radii]
        PCMFiller += f'\tRadii                  {pcm_radii}\n'
    except KeyError:
        raise Exception("PCM Radii not implemented")

    # VDWScale
    if job.pcm_VDWScale != 1.2:
        PCMFiller += f'\tvdwScale               {job.pcm_VDWScale}\n'
    
    # Probe Radii
    if job.pcm_probe_radii != 0.0:
        PCMFiller += f'\tSASradius              {job.pcm_probe_radii}\n'
    # Cavity
    cavityDict = {PCM.Cavity.sas:     'VDW_SAS', 
                  PCM.Cavity.ses:     'SES', 
                  PCM.Cavity.default: ''}
    try:
        PCMFiller += f'\tSurfaceType            {cavityDict[job.pcm_surfaceType]}\n'
    except KeyError:
        raise Exception("Cavity Type not implemented")
    
    #####################################################
    ######################## Job 1 ######################
    #####################################################

    QChemInput =  '$molecule\n'
    for line in xyz[2:]:
        if len(line.split()) > 2:
            QChemInput += f'{line}\n'
    QChemInput +=  '$end\n\n'

    remBlock =  '$rem\n'
    remBlock += f'\tMEM_TOTAL             {job.mem.total_mb}\n'
    remBlock +=  '\tGUI                   2\n'
    if jobType != 'SP': 
        remBlock += f'\tJOBTYPE               {jobType}\n'
    remBlock += f'\tEXCHANGE              {job.method.qchem}\n'
    remBlock += f'\tBASIS                 {job.basis.qchem}\n'
    remBlock += f'\tXC_GRID               {job.grid.qchem}\n'
    remBlock +=  '\tSYMMETRY              false\n'
    if job.tddft == TDDFT.tddft:
        remBlock += f'\tCIS_N_ROOTS           {job.nroots}\n'
        remBlock += f'\tRPA                   {rpa}\n'
        remBlock += f'\tCIS_TRIPLETS          {triplets}\n'
        remBlock +=  '\tCIS_RELAXED_DENSITY   TRUE\n'
        if job.job in [Jobs.freq, Jobs.grad, Jobs.opt]:
            remBlock += f'\tCIS_STATE_DERIV       {job.state.root}\n'
    if pcm != '':
        remBlock += f'\tSOLVENT_METHOD        {pcm}\n'
    QChemInput +=  remBlock
    QChemInput +=  '$rem\n\n'

    if pcm != '':
        if job.solv in [PCM.smd]:
            solventBlock  =  '$smx\n'
            solventBlock += f'\tsolvent           {job.solv.smd}\n'
            solventBlock +=  '\tprint             2\n'
            solventBlock +=  '$end\n\n'


        if job.pcm in [PCM.cpcm, PCM.lrpcm, PCM.sspcm]:
            solventBlock  =  '$solvent\n'
            solventBlock += f'\tDielectric             {job.solv.e:.4f}\n'
            solventBlock += f'\tOpticalDielectric      {job.solv.n**2:.4f}\n'
            solventBlock +=  '$end\n\n'

            # For cLR emission
            if job.pcm == PCM.sspcm and job.job == Jobs.em:
                QChemInput +=  '$pcm\n'
                QChemInput += f'\tTheory                {pcmFormalism}\n'
                QChemInput +=  '\tChargeSeparation      Marcus\n'
                QChemInput +=  '\tStateSpecific         Perturb\n'
                QChemInput +=  PCMFiller
                QChemInput +=  '$end\n\n'

            # For cLR excitations
            if job.pcm == PCM.sspcm and job.job == Jobs.em:
                QChemInput +=  '$pcm\n'
                QChemInput += f'\tTheory                {pcmFormalism}\n'
                QChemInput +=  '\tChargeSeparation      Excited\n'
                QChemInput += f'\tStateSpecific         {job.state.root}\n'
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
        QChemInput +=  '\tREAD\n'
        QChemInput +=  '$end\n\n'

        QChemInput +=  remBlock
        QChemInput +=  '\tSCF_GUESS             READ\n'
        QChemInput +=  '$rem\n\n'


        QChemInput +=  '$pcm\n'
        QChemInput += f'\tTheory                {pcmFormalism}\n'
        QChemInput +=  '\tStateSpecific         Marcus\n'
        QChemInput +=  PCMFiller
        QChemInput +=  '$end\n\n'

        QChemInput += solventBlock

    return QChemInput
