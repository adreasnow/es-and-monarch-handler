from .newenum import *
class Solvents(NewEnum):
    def __init__(self, solvent:str, xtb:str, smd:str, nwchem:str, e:float, n:float, a:float, b:float, g:float, p:float, s:float, ds:bool=True) -> None:
            self.solvent = solvent
            self.e       = e
            self.n       = n
            self.a       = a
            self.b       = b
            self.g       = g
            self.p       = p
            self.s       = s
            self.ds      = ds
            self.xtb     = xtb
            self.smd     = smd
            self.nwchem  = nwchem
            return

    def __str__(self):
        return self.name

    def __float__(self):
        return self.e

    def __bool__(self):
        return self.ds

    #        Name           XTB              SMD                NWChem            ε     n       α     β      γ     φ     ψ     used
    gas    = 'Gas',         None,           None,              None,              1.00, 1.0000, 0.00, 0.00,  0.00, 0.00, 0.00, False
    nhex   = 'Hexane',     'hexane',       'n-hexane',        'hexane'  ,         1.88, 1.3749, 0.00, 0.00, 25.75, 0.00, 0.00, False
    nhep   = 'Heptane',    'hexane',       'n-heptane',       'heptane',          1.91, 1.3878, 0.00, 0.00, 28.28, 0.00, 0.00, False
    tol    = 'Toluene',    'toluene',      'toluene',         'toluene',          2.37, 1.4969, 0.00, 0.14, 40.21, 0.86, 0.00
    ans    = 'Anisole',    'ether',        'anisole',         'anisole',          4.22, 1.5170, 0.00, 0.29, 50.90, 0.75, 0.00
    ether  = 'Ether',      'ether',        'diethyl ether',   'ether',            4.24, 1.3473, 0.00, 0.41, 24.68, 0.00, 0.00
    chcl3  = 'Chloroform', 'chcl3',        'chloroform',      'chcl3',            4.71, 1.4458, 0.15, 0.02, 39.00, 0.00, 0.50
    thf    = 'THF',        'thf',          'thf',             'thf',              7.43, 1.4072, 0.00, 0.48, 39.39, 0.00, 0.00
    dcm    = 'DCM',        'ch2cl2',       'dichloromethane', 'dcm',              8.93, 1.4241, 0.10, 0.05, 40.06, 0.00, 0.67
    c8oh   = 'Octanol',    'octanol',      '1-octanol',       'octanol',          9.86, 1.4300, 0.37, 0.48, 37.44, 0.00, 0.00
    etoh   = 'Ethanol',    'dmf',          'ethanol',         'ethanol',         24.85, 1.3614, 0.37, 0.48, 32.06, 0.00, 0.00
    acn    = 'ACN',        'acetonitrile', 'mecn',            'acetntrl',        35.69, 1.3441, 0.07, 0.32, 40.82, 0.00, 0.00
    dmf    = 'DMF',        'dmf',          'dmf',             'dmf',             37.22, 1.4305, 0.00, 0.74, 52.85, 0.00, 0.00
    dmso   = 'DMSO',       'dmso',         'dmso',            'dmso',            46.83, 1.4793, 0.00, 0.88, 62.40, 0.00, 0.00
    h2o    = 'water',      'water',        'water',           'water',           78.40, 1.3330, 0.82, 0.00,  0.00, 0.00, 0.00, False
