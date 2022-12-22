from .newenum import *


class TDDFT(NewEnum):    
    @skip
    class TDA(NewEnum):
        on  = 'on'
        off = 'off'
        fitting = 'fitting'

    none   =  'none'
    tddft  =  'tddft'