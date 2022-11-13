from .newenum import *
class States(NewEnum):
    def __init__(self, root:int, mult:int, spin:int, latex:str) -> None:
            self.root   = root
            self.mult   = mult
            self.spin   = spin
            self.latex  = latex
            return
    
    def __str__(self):
      return self.name

    def __int__(self):
      return self.root

    #       root  mutl  spin   latex   
    s0   =   0,    1,    0,    's_0'
    s1   =   1,    1,    0,    's_1'
    s2   =   2,    1,    0,    's_2'
    s3   =   3,    1,    0,    's_3'
    s4   =   4,    1,    0,    's_4'
    s5   =   5,    1,    0,    's_5'
    s6   =   6,    1,    0,    's_6'
    s7   =   7,    1,    0,    's_7'
    s8   =   8,    1,    0,    's_8'
    s9   =   9,    1,    0,    's_9'
    s10  =   10,   1,    0,    's_10'
    t0   =   0,    2,    1,    't_0'
    t1   =   1,    2,    1,    't_1'
    t2   =   2,    2,    1,    't_2'
    t3   =   3,    2,    1,    't_3'
