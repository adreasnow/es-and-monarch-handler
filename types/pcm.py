from .newenum import NewEnum, skip


class PCM(NewEnum):

    @skip
    class Eq(NewEnum):
        def __init__(self, string: str) -> None:
            self.string   = string
            return

        def __str__(self):
            return self.string

        eq     = 'eq'
        neq    = 'neq'
        eq_neq = 'eq_neq'
        none   = 'None'

    @skip
    class Radii(NewEnum):
        uff      = 'uff'
        smd      = 'smd'
        bondi    = 'bondi'
        arlinger = 'arlinger'
        ff       = 'from_ff'
        read     = 'from_file'
        default  = 'default'

    @skip
    class Cavity(NewEnum):
        sas        = 'sas'
        ses        = 'ses'
        isodensity = 'iso'
        spherical  = 'spherical'
        default    = 'default'

    @skip
    class Discretisation(NewEnum):
        lebedev  = 'lebedev'
        tesserae = 'tesserae'
        swig     = 'swig'
        iswig    = 'iswig'
        default  = 'default'

    @skip
    class ExcitedModel(NewEnum):
        none  = 'none'
        vem   = 'vem'
        clr   = 'clr'
        lr    = 'lr'
        ibsf  = 'ibsf'

    @skip
    class NonEl(NewEnum):
        smssp = 'smssp'
        smd   = 'smd'

    @skip
    class Formalism(NewEnum):
        def __init__(self, string: str) -> None:
            self.string   = string
            return

        def __str__(self):
            return self.string

        cpcm    = 'CPCM'
        iefpcm  = 'IEF-PCM'
        ssvpe   = 'SS(V)PE'
        cosmo   = 'COSMO'
        pb      = 'Poisson-Boltzmann'
        none    = 'none'

    cpcm  = 'cpcm'
    smd   = 'smd'
    lrpcm = 'lrpcm'
    sspcm = 'sspcm'
    vem   = 'vem'
    smssp = 'smssp'
    alpb  = 'alpb'
    none  = 'none'
