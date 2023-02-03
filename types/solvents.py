from .newenum import *
class Solvents(NewEnum):
    def __init__(self, solvent:str, xtb:str, smd:str, nwchem:str, e:float, n:float, a:float, b:float, g:float, p:float, s:float, eta:float, ds:bool=True) -> None:
            self.solvent = solvent
            self.e       = e
            self.n       = n
            self.a       = a
            self.b       = b
            self.g       = g
            self.p       = p
            self.s       = s
            self.eta     = eta
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

    def __repr__(self):
        return self.solvent

    #        Name           XTB              SMD                NWChem            ε     n       α     β     γ      φ     ψ     η     used
    nhex   = 'N-Hexane',   'hexane',       'n-hexane',        'hexane',           1.88, 1.3749, 0.00, 0.00, 26.41, 0.00, 0.00, 0.30
    tol    = 'Toluene',    'toluene',      'toluene',         'toluene',          2.37, 1.4969, 0.00, 0.14, 40.21, 0.86, 0.00, 0.55
    ans    = 'Anisole',    'ether',        'anisole',         'anisole',          4.22, 1.5170, 0.00, 0.29, 50.90, 0.75, 0.00, 0.98
    ether  = 'Ether',      'ether',        'diethyl ether',   'ether',            4.24, 1.3473, 0.00, 0.41, 24.68, 0.00, 0.00, 0.22
    chcl3  = 'Chloroform', 'chcl3',        'chloroform',      'chcl3',            4.71, 1.4458, 0.15, 0.02, 39.00, 0.00, 0.50, 0.54
    thf    = 'THF',        'thf',          'thf',             'thf',              7.43, 1.4072, 0.00, 0.48, 39.39, 0.00, 0.00, 0.46
    dcm    = 'DCM',        'ch2cl2',       'dichloromethane', 'dcm',              8.93, 1.4241, 0.10, 0.05, 40.06, 0.00, 0.67, 0.41
    c8oh   = 'Octanol',    'octanol',      '1-octanol',       'octanol',          9.86, 1.4300, 0.37, 0.48, 37.44, 0.00, 0.00, 7.36
    etoh   = 'Ethanol',    'dmf',          'ethanol',         'ethanol',         24.85, 1.3614, 0.37, 0.48, 32.06, 0.00, 0.00, 1.08
    acn    = 'ACN',        'acetonitrile', 'mecn',            'acetntrl',        35.69, 1.3441, 0.07, 0.32, 40.82, 0.00, 0.00, 0.34
    dmf    = 'DMF',        'dmf',          'dmf',             'dmf',             37.22, 1.4305, 0.00, 0.74, 52.85, 0.00, 0.00, 0.92
    dmso   = 'DMSO',       'dmso',         'dmso',            'dmso',            46.83, 1.4793, 0.00, 0.88, 62.40, 0.00, 0.00, 2.00

    gas    = 'Gas',         None,           None,              None,              1.00, 1.0000, 0.00, 0.00,  0.00, 0.00, 0.00,  0.00, False
    # nhex   = 'Hexane',     'hexane',       'n-hexane',        'hexane'  ,         1.88, 1.3749, 0.00, 0.00, 25.75, 0.00, 0.00, False
    # nhep   = 'Heptane',    'hexane',       'n-heptane',       'heptane',          1.91, 1.3878, 0.00, 0.00, 28.28, 0.00, 0.00, False
    chex   = 'c-Hexane',   'c-hexane',     'c-hexane',        'c-hexane',         2.02, 1.4269, 0.00, 0.00, 26.41, 0.00, 0.00,  0.30, False
    dox    = 'Dioxane',     None,           None,              None,              2.25, 1.4224, 0.00, 0.00,  0.00, 0.00, 0.00,  0.00, False
    meoh   = 'Methanol',   'methanol',     'methanol',        'methanol',        32.70, 1.3270, 0.37, 0.48, 22.50, 0.00, 0.00,  0.00, False
    h2o    = 'water',      'water',        'water',           'water',           78.40, 1.3330, 0.82, 0.00,  0.00, 0.00, 0.00,  0.00, False
    h2so4  = 'h2so4',      'h2so4',        'h2so4',           'h2so4',           78.40, 1.3330, 0.82, 0.00,  0.00, 0.00, 0.00,  0.00, False
    naoh   = 'naoh',       'naoh',         'naoh',            'naoh',            78.40, 1.3330, 0.82, 0.00,  0.00, 0.00, 0.00,  0.00, False

    none   = 'None',        None,           None,              None,              0.00, 0.0000, 0.00, 0.00,  0.00, 0.00, 0.00,  0.00, False