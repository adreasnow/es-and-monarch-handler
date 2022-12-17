from .newenum import *
class Jobs(NewEnum):
    def __init__(self, long:str) -> None:
            self.long    = long
            return
    
    def __str__(self):
      return self.long

    #       
    opt       = 'optimisation'
    freq      = 'frequencies'
    sp        = 'single_point'
    td        = 'td-dft'
    grad      = 'gradient'
    crest     = 'crest'
    casscf    = 'casscf_single_point'
    casscfOpt = 'casscf_optimisation'
    mp2Natorb = 'mp2-natural-orbitals'

