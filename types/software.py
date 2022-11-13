from .newenum import *
class Software(NewEnum):
    def __init__(self, short:str, long:str, ext:str) -> None:
            self.short   = short
            self.long    = long
            self.ext     = ext
            return
    
    def __str__(self):
      return self.short

    #       
    orca       = 'or',    'Orca',      '.inp'
    nwchem     = 'nw',    'NWChem',    '.nw'
    psi4       = 'p4',    'Psi4',      '.in'
    psi4Script = 'p4',    'Psi4',      '.py'
    qchem      = 'qc',    'QChem',     '.inp'
    crest      = 'cr',    'CREST',     '.slm'
    gaussian   = 'ga',    'Gaussian',  '.gjf'
    pyscf      = 'ps',    'PySCF',     '.py'

