from .newenum import *
class Jobs(NewEnum):
    def __init__(self, long:str) -> None:
            self.long    = long
            return
    
    def __str__(self):
      return self.long

    #       
    opt    = 'optimisation'
    freq   = 'frequencies'
    sp     = 'single point'
    td     = 'td-dft'
    grad   = 'gradient'
    crest  = 'crest'
    casscf = 'casscf'

