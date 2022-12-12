from .newenum import *
from .states import States
from .solvents import Solvents

class Fluorophores(NewEnum):
    def __init__(self, fluorophore:str, smiles:str, active:tuple[int,int], extinction:int, extinctionSolv:Solvents, extinctionLambda:int, qy:float, qySolvent:Solvents, qyLambda:int, ref:bool, revised:bool=False, charge:int=0, root:States=States.s1) -> None:
            self.fluorophore       = fluorophore
            self.smiles            = smiles
            self.charge            = charge
            self.root              = root
            self.ref               = ref
            self.extinction        = extinction
            self.extinctionSolvent = extinctionSolv
            self.extinctionLambda  = extinctionLambda
            self.qy                = qy
            self.qysolvent         = qySolvent
            self.qyLambda          = qyLambda
            self.revised           = revised
            self.active            = active
            return
    
    def __str__(self):
        return self.name

    def __int__(self):
        return self.charge

    def __bool__(self):
        return self.revised

    #index         name                                                     SMILES                                                         Active space   ε         ε solvent      ελ       Φ         Φ Solvent     Φλ    ref  revised q   root
    #                                                                                                                                                                                     10.1016/0009-2614(72)85047-4
    az        = 'Azulene',                                    'c1cccc2cccc2c1',                                                                  (10,10), 0,      Solvents.none,   000,   0.24,    Solvents.meoh,  347,   False, True,    0, States.s2 
    #                                                                                                                                                     0.1016/j.jlumin.2012.08.017     0.1016/j.jlumin.2012.08.017
    r800      = 'Rhodamine 800',                              'C1CC2=CC3=C(C4=C2N(C1)CCC4)OC5=C6CCC[N+]7=C6C(=CC5=C3C#N)CCC7',                   (0,0),   113302, Solvents.etoh,   682,   0.25,    Solvents.etoh,  623,   False, True,   +1
    #                                                                                                                                                     10.1002/marc.201900234 (SI)     10.1002/marc.201900234 (SI)
    aaq       = '1-Aminoanthraquinone',                       'C1=CC=C2C(=C1)C(=O)C3=C(C2=O)C(=CC=C3)N',                                         (0,0),   7380,   Solvents.acn,    465,   0.031,   Solvents.chcl3, 300,   False, True
    #                                                                                                                                                                                     10.1021/ac101329h
    c120      = 'Coumarin 153',                               'C1CC2=CC3=C(C4=C2N(C1)CCC4)OC(=O)C=C3C(F)(F)F',                                   (0,0),   0,      Solvents.none,   000,   0.54,    Solvents.dcm,   402,   False, True    
    #                                                                                                                                                     10.1021/ac60235a020             10.1021/jo061369v
    nr        = 'Nile Red',                                   'O=C1C=C2OC(C=C(N(CC)CC)C=C3)=C3N=C2C4=C1C=CC=C4',                                 (0,0),   38000,  Solvents.dox,    519,   0.38,    Solvents.meoh,  553,   False, True
    #                       `                                                                                                           `                                                 10.1007/s43630-022-00250-y
    bod493    = 'BODIPY 493/503',                             'Cc1c2N(c(C)c1)[B-](F)(F)[N+]1c([C]2C)c(cc1C)C',                                   (0,0),   0,      Solvents.none,   000,   0.968,   Solvents.tol,   500,   False, True
    #
    ndi       = 'Naphthalene diimide',                        'none',                                                                            (0,0),   0,      Solvents.none,   000,   0.00,    Solvents.none,  000,   False, 
    #
    nda       = 'Naphthalamide',                              'none',                                                                            (0,0),   0,      Solvents.none,   000,   0.00,    Solvents.none,  000,   False, 
    #
    pro       = 'Prodan',                                     'CCC(=O)C1=CC2=C(C=C1)C=C(C=C2)N(C)C',                                             (0,0),   0,      Solvents.none,   000,   0.00,    Solvents.none,  000,   False,
    #
    daa       = 'Dansyl amide',                               'CN(C)C1=CC=CC2=C1C=CC=C2S(=O)(=O)N',                                              (0,0),   0,      Solvents.none,   000,   0.00,    Solvents.none,  000,   False,  

    #                                                                                                                                                     10.1016/0307-4412(94)90083-3    10.1111/j.1751-1097.1990.tb01686.x
    dapi      = 'DAPI',                                       'N=C(C1=CC2=C(C=C1)C=C(C3=CC=C(C(N)=N)C=C3)N2)N',                                  (0,0),   27000,  Solvents.dmso,   333,   0.58,    Solvents.dmso,  310,   False,  

    
    # ref
    #                                                                                                                                https://omlc.org/spectra/PhotochemCAD/html/083.html  10.1351/PAC-REP-10-09-31
    r6g       = 'Rhodamine 6G',                               'CC1=CC(C(C2=CC=CC=C2C(OCC)=O)=C3C=C/4C)=C(C=C1NCC)OC3=CC4=[NH+]\\CC',             (0,0),   116000, Solvents.etoh,   530,   0.94,    Solvents.etoh,  488,   True,  False,  +1
    #                                                                                                                                https://omlc.org/spectra/PhotochemCAD/html/009.html  10.1351/PAC-REP-10-09-31
    rb        = 'Rhodamine B',                                'CC/[N+](CC)=C1C=CC2=C(C3=CC=CC=C3C(O)=O)C4=C(C=C(N(CC)CC)C=C4)OC2=C\\1',          (0,0),   106000, Solvents.etoh,   543,   0.70,    Solvents.meoh,  348,   True,  False,  +1
    #                                                                                                                                                     10.1021/ac101329h               https://iss.com/resources/reference/data_tables/FL_QuantumYieldStandards.html
    cv        = 'Cresyl Violet',                              '[Cl-].N=1c4c(OC=3C=1c2ccccc2\C(=[NH2+])\C=3)cc(c(c4)C)N(C)C',                     (0,0),   63574,  Solvents.etoh,   611,   0.53,    Solvents.meoh,  580,   True,  False,  +1






    # r123      = 'Rhodamine 123',                              '[NH2+]=C1C=C2OC3=C(C=CC(N)=C3)C(C4=CC=CC=C4C(OC)=O)=C2C=C1',                      (0,0),   85700,  Solvents.etoh,   000,   0.86,    Solvents.etoh,  000,   True,  False, +1
    # mca       = 'Merocyanine 540',                            'CCCCN1C(=O)C(=C/C=C/C=C\\2/N(c3ccccc3O2)CCCS(=O)(=O)[O-])C(=O)N(C1=O)CCCC',       (0,0),   0,      Solvents.none,   000,   0.00,    Solvents.none,  000,   True,  False, -1



    # Legacy
    # icm       = 'Indigo carmine',                             '[O-]S(=O)(=O)c3cc4C(=O)\\C(=C2\\C(=O)c1cc(ccc1N2)S([O-])(=O)=O)Nc4cc3',           (0,0),   0,      Solvents.none,   000,   0.00,    Solvents.none,  000,   False, False,  -2
    # c519p     = 'Protonated coumarin 343/519',                'C1CC2=C3C(=C4C(=C2)C=C(C(=O)O4)C(=O)O)CCCN3C1',                                   (0,0),   0,      Solvents.none,   000,   0.00,    Solvents.none,  000,   True
    # c519d     = 'Deprotonated coumarin 343/519',              'C1CC2=C3C(=C4C(=C2)C=C(C(=O)O4)C(=O)[O-])CCCN3C1',                                (0,0),   0,      Solvents.none,   000,   0.00,    Solvents.none,  000,   True,  False, -1
    # fitc5     = 'FITC',                                       'c1cc2c(cc1N=C=S)C3(c4ccc(cc4Oc5c3ccc(c5)O)O)OC2=O',                               (0,0),   0,      Solvents.none,   000,   0.00,    Solvents.none,  000,   True
    # dah       = 'Dansyl hydrazine',                           'CN(C)C1=CC=CC2=C1C=CC=C2S(=O)(=O)NN',                                             (0,0),   0,      Solvents.none,   000,   0.00,    Solvents.none,  000,   True
    # dac       = 'Dansyl chloride',                            'CN(C)C1=CC=CC2=C1C=CC=C2S(=O)(=O)Cl',                                             (0,0),   0,      Solvents.none,   000,   0.00,    Solvents.none,  000,   True
    # ai        = '7-Azaindole',                                'C1=CC2=C(NC=C2)N=C1',                                                             (0,0),   0,      Solvents.none,   000,   0.00,    Solvents.none,  000,   False, True
    # ld        = 'Laurdan',                                    'CCCCCCCCCCCC(=O)c1ccc2cc(ccc2c1)N(C)C',                                           (0,0),   0,      Solvents.none,   000,   0.00,    Solvents.none,  000,   False
    # anap      = 'l-ANAP',                                     'N[C@@H](CNC1=CC=C2C=C(C(C)=O)C=CC2=C1)C(O)=O',                                    (0,0),   0,      Solvents.none,   000,   0.00,    Solvents.none,  000,   False
    # fl        = 'Fluorescein',                                'c1ccc2c(c1)C(=O)OC23c4ccc(cc4Oc5c3ccc(c5)O)O',                                    (0,0),   0,      Solvents.none,   000,   0.00,    Solvents.none,  000,   False
    # tmb       = 'Tetramethyl BODIPY',                         'C1(C)C=C(C)N([b-]3(F)(F))C=1C=C2[N+]3=C(C)C=C(C)2',                               (0,0),   0,      Solvents.none,   000,   0.00,    Solvents.none,  000,   False
    # nta_dmnld = 'Napthalamide DMN-LD',                        'O=C(N(CCC)C1=O)C2=CC(OC)=C(OC)C3=C2C1=CC=C3',                                     (0,0),   0,      Solvents.none,   000,   0.00,    Solvents.none,  000,   False
    # _7h4mcp   = 'Protonated 7-hydroxy-4-methylcoumarin',      'O=C1OC2=C(C=CC(O)=C2)C(C)=C1',                                                    (0,0),   0,      Solvents.none,   000,   0.00,    Solvents.none,  000,   False
    # _7h4mcd   = 'Deprotonated 7-hydroxy-4-methylcoumarin',    'O=C1OC2=C(C=CC([O-])=C2)C(C)=C1',                                                 (0,0),   0,      Solvents.none,   000,   0.00,    Solvents.none,  000,   False, False, -1
    # c6        = 'Coumarin 6',                                 'O=C1OC(C=C(N(CC)CC)C=C2)=C2C=C1C3=NC(C=CC=C4)=C4S3',                              (0,0),   0,      Solvents.none,   000,   0.00,    Solvents.none,  000,   False
    # oaz1      = 'Oxazine 1',                                  'CC\/[N+](CC)=C1C=C2OC3=CC(N(CC)CC)=CC=C3N=C2C=C\\1',                              (0,0),   0,      Solvents.none,   000,   0.00,    Solvents.none,  000,   False, False, +1