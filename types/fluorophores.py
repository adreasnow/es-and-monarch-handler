from .newenum import *
from .states import States

class Fluorophores(NewEnum):
    def __init__(self, fluorophore:str, smiles:str, active:tuple[int,int], test:bool, revised:bool=False, charge:int=0, root:States=States.s1) -> None:
            self.fluorophore = fluorophore
            self.smiles      = smiles
            self.charge      = charge
            self.root        = root
            self.test        = test
            self.revised     = revised
            self.active      = active
            return
    
    def __str__(self):
        return self.name

    def __int__(self):
        return self.charge

    def __bool__(self):
        return self.revised

    # From the dataset
    r6g       = 'Rhodamine 6G',                               'CC1=CC(C(C2=CC=CC=C2C(OCC)=O)=C3C=C/4C)=C(C=C1NCC)OC3=CC4=[NH+]\\CC',                                                 (0,0),   True,  False, +1
    r123      = 'Rhodamine 123',                              '[NH2+]=C1C=C2OC3=C(C=CC(N)=C3)C(C4=CC=CC=C4C(OC)=O)=C2C=C1',                                                          (0,0),   True,  False, +1
    af532     = 'AlexaFluor 532',                             'CC1C(C2=C(N1)C(=C3C(=C2)C(=C4C=C5C(=NC(C5(C)C)C)C(=C4O3)S(=O)(=O)O)C6=CC=C(C=C6)C(=O)ON7C(=O)CCC7=O)S(=O)(=O)O)(C)C', (0,0),   True
    ndi       = 'Naphthalene diimide',                        'none',                                                                                                                (0,0),   False
    nda       = 'Naphthalamide',                              'none',                                                                                                                (0,0),   False
    pro       = 'Prodan',                                     'CCC(=O)C1=CC2=C(C=C1)C=C(C=C2)N(C)C',                                                                                 (12,12), True,  True
    anap      = 'l-ANAP',                                     'N[C@@H](CNC1=CC=C2C=C(C(C)=O)C=CC2=C1)C(O)=O',                                                                        (0,0),   False
    ld        = 'Laurdan',                                    'CCCCCCCCCCCC(=O)c1ccc2cc(ccc2c1)N(C)C',                                                                               (0,0),   False
    fitc5     = 'FITC',                                       'c1cc2c(cc1N=C=S)C3(c4ccc(cc4Oc5c3ccc(c5)O)O)OC2=O',                                                                   (0,0),   True
    c519p     = 'Protonated coumarin 343/519',                'C1CC2=C3C(=C4C(=C2)C=C(C(=O)O4)C(=O)O)CCCN3C1',                                                                       (0,0),   True
    c519d     = 'Deprotonated coumarin 343/519',              'C1CC2=C3C(=C4C(=C2)C=C(C(=O)O4)C(=O)[O-])CCCN3C1',                                                                    (0,0),   True,  False, -1
    tr        = 'Texas Red',                                  'C1Cc2cc3c(c4c2N(C1)CCC4)O[C]1C2=C4N(CCC2)CCCC4=CC1=C3c1c(cc(cc1)S(=O)(=O)Cl)S([O])([O])[O]',                          (0,0),   True
    nr        = 'Nile Red',                                   'O=C1C=C2OC(C=C(N(CC)CC)C=C3)=C3N=C2C4=C1C=CC=C4',                                                                     (0,0),   True,  True
    bod493    = 'BODIPY 493/503',                             'Cc1c2N(c(C)c1)[B-](F)(F)[N+]1c([C]2C)c(cc1C)C',                                                                       (8,8),   True,  True
    mca       = 'Merocyanine 540',                            'CCCCN1C(=O)C(=C/C=C/C=C\\2/N(c3ccccc3O2)CCCS(=O)(=O)[O-])C(=O)N(C1=O)CCCC',                                           (0,0),   True,  False, -1
    dah       = 'Dansyl hydrazine',                           'CN(C)C1=CC=CC2=C1C=CC=C2S(=O)(=O)NN',                                                                                 (0,0),   True
    daa       = 'Dansyl amide',                               'CN(C)C1=CC=CC2=C1C=CC=C2S(=O)(=O)N',                                                                                  (4,4),   True,  True
    dac       = 'Dansyl chloride',                            'CN(C)C1=CC=CC2=C1C=CC=C2S(=O)(=O)Cl',                                                                                 (0,0),   True
    az        = 'Azulene',                                    'c1cccc2cccc2c1',                                                                                                      (10,10),   True,  True,   0, States.s2 
    icm       = 'Indigo carmine',                             '[O-]S(=O)(=O)c3cc4C(=O)\\C(=C2\\C(=O)c1cc(ccc1N2)S([O-])(=O)=O)Nc4cc3',                                               (0,0),   True,  True,  -2
    fl        = 'Fluorescein',                                'c1ccc2c(c1)C(=O)OC23c4ccc(cc4Oc5c3ccc(c5)O)O',                                                                        (0,0),   False
    cb        = 'Cascade blue',                               'O=S(C1=C(C2=C34)C=CC4=C(OC)C=C(S(=O)([O-])=O)C3=CC=C2C(S(=O)([O-])=O)=C1)([O-])=O',                                   (0,0),   True,  False, -3

    # New
    aaq       = '1-Aminoanthraquinone',                       'C1=CC=C2C(=C1)C(=O)C3=C(C2=O)C(=CC=C3)N',                                                                             (0,0),   False, True
    ai        = '7-Azaindole',                                'C1=CC2=C(NC=C2)N=C1',                                                                                                 (8,8),   False, True

    # possible?
    c120      = 'Coumarin 120?',                              'CC1=CC(=O)OC2=C1C=CC(=C2)N',                                                                                          (10,10), False, True
    dapi      = 'DAPI?',                                      'N=C(C1=CC2=C(C=C1)C=C(C3=CC=C(C(N)=N)C=C3)N2)N',                                                                      (0,0),   True,  True
    r800      = 'Rhodamine 800?',                             'N#CC1=C2C=C(CCC3)C4=[N+]3CCCC4=C2OC5=C1C=C6CCCN7C6=C5CCC7',                                                           (0,0),   False, True,  +1



    # Legacy
    tmb       = 'Tetramethyl BODIPY',                         'C1(C)C=C(C)N([b-]3(F)(F))C=1C=C2[N+]3=C(C)C=C(C)2',                                                                   (0,0),   False
    nta_dmnld = 'Napthalamide DMN-LD',                        'O=C(N(CCC)C1=O)C2=CC(OC)=C(OC)C3=C2C1=CC=C3',                                                                         (0,0),   False
    _7h4mcp   = 'Protonated 7-hydroxy-4-methylcoumarin',      'O=C1OC2=C(C=CC(O)=C2)C(C)=C1',                                                                                        (0,0),   False
    _7h4mcd   = 'Deprotonated 7-hydroxy-4-methylcoumarin',    'O=C1OC2=C(C=CC([O-])=C2)C(C)=C1',                                                                                     (0,0),   False, False, -1
    rb        = 'Rhodamine B',                                'CC\/[N+](CC)=C1C=CC2=C(C3=CC=CC=C3C(O)=O)C4=C(C=C(N(CC)CC)C=C4)OC2=C\\1',                                             (0,0),   False, False, +1
    c6        = 'Coumarin 6',                                 'O=C1OC(C=C(N(CC)CC)C=C2)=C2C=C1C3=NC(C=CC=C4)=C4S3',                                                                  (0,0),   False
    oaz1      = 'Oxazine 1',                                  'CC\/[N+](CC)=C1C=C2OC3=CC(N(CC)CC)=CC=C3N=C2C=C\\1',                                                                  (0,0),   False, False, +1