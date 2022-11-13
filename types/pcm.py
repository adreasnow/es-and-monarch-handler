from .newenum import *
from .software import Software

class PCM(NewEnum):
    @skip
    class Eq(NewEnum):
        def __init__(self, string:str) -> None:
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
        uff      = auto()
        smd      = auto()
        bondi    = auto()
        arlinger = auto()
    
    @skip
    class Cavity(NewEnum):
        gepol      = auto()
        sas        = auto()
        ses        = auto()
        isodensity = auto()
        spherical  = auto()
    
    @skip
    class Switching(NewEnum):
        swig  = auto()
        iswig = auto()
        none  = auto()
    
    @skip
    class Discretisation(NewEnum):
        lebedev  = auto()
        tesserae = auto()
    
    @skip
    class ExcitedModel(NewEnum):
        vem   = auto()
        clr   = auto()
        lr    = auto()
        ibsf  = auto()
    
    @skip
    class NonEl(NewEnum):
        smssp = auto()
        smd   = auto()

    @skip
    class Formalism(NewEnum):
        def __init__(self, string:str) -> None:
            self.string   = string
            return

        def __str__(self):
            return self.string

        cpcm    = 'CPCM'
        iefpcm  = 'IEF-PCM'
        ssvpe   = 'SS(V)PE'
        cosmo   = 'COSMO'

    cpcm  = auto()
    smd   = auto()
    vem   = auto()
    smssp = auto()
    alpb  = auto()
    none  = auto()
