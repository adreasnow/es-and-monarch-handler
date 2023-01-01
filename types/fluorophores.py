from .newenum import *
from .states import States
from .solvents import Solvents

class Fluorophores(NewEnum):
    def __init__(self, fluorophore:str, smiles:str, active:tuple[int,int], extinction:int, extinctionSolv:Solvents, extinctionLambda:int, qy:float, qySolvent:Solvents, qyLambda:int, lifetime:float, lifetimeSolvent:Solvents, ref:bool, revised:bool=False, gas:bool=False, charge:int=0, root:States=States.s1) -> None:
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
            self.lifetime          = lifetime
            self.lifetimeSolvent   = lifetimeSolvent
            self.revised           = revised
            self.active            = active
            self.gas               = gas
            return
    
    def __str__(self):
        return self.name

    def __int__(self):
        return self.charge

    def __bool__(self):
        return self.revised

    #index         name                                                     SMILES                                                         Active space   ε         ε solvent      ελ       Φ         Φ Solvent     Φλ     τ     τ Solvent       ref  revised   Gas         q   root
    #                                                                                                                                                                                                                     S1 -> S0 is 2ps  10.1016/0047-2670(80)80022-0
    #                                                                                                                                                                                     10.1016/0009-2614(72)85047-4    10.1016/0009-2614(72)85047-4
    az        = 'Azulene',                                    'c1cccc2cccc2c1',                                                                  (10,10), 0,      Solvents.none,   000,   0.24,    Solvents.meoh,  347,   5,     Solvents.meoh,  False, True,  True,    0, States.s2 
    #                                                                                                                                                     10.1016/j.jlumin.2012.08.017    10.1016/j.jlumin.2012.08.017    10.1016/j.jlumin.2012.08.017
    r800      = 'Rhodamine 800',                              'C1CC2=CC3=C(C4=C2N(C1)CCC4)OC5=C6CCC[N+]7=C6C(=CC5=C3C#N)CCC7',                   (16,16), 113302, Solvents.etoh,   682,   0.25,    Solvents.etoh,  623,   1.93,  Solvents.etoh,  False, True,  False,  +1
    #                                                                                                                                                     10.1002/marc.201900234 (SI)     10.1002/marc.201900234 (SI)     10.1016/1010-6030(92)85181-S
    aaq       = '1-Aminoanthraquinone',                       'C1=CC=C2C(=C1)C(=O)C3=C(C2=O)C(=CC=C3)N',                                         (8,8),   7380,   Solvents.acn,    465,   0.031,   Solvents.chcl3, 300,   2.10,  Solvents.none,  False, True,  False
    #                                                                                                                                                                                                                     Multiexponential fit also had 30% 1.27 ns
    #                                                                                                                                                                                     10.1021/ac101329h               10.1063/1.3276680
    c153      = 'Coumarin 153',                               'C1CC2=CC3=C(C4=C2N(C1)CCC4)OC(=O)C=C3C(F)(F)F',                                   (6,6),   0,      Solvents.none,   000,   0.54,    Solvents.dcm,   402,   0.12,  Solvents.acn,   False, True,  True    
    #                                                                                                                                                     10.1021/ac60235a020             10.1021/jo061369v               10.1117/1.JBO.20.9.096002
    nr        = 'Nile Red',                                   'O=C1C=C2OC(C=C(N(CC)CC)C=C3)=C3N=C2C4=C1C=CC=C4',                                 (16,16), 38000,  Solvents.dox,    519,   0.38,    Solvents.meoh,  553,   3.656, Solvents.etoh,  False, True,  False
    #                                                                                                                                                                                     0.93 toluene
    #                       `                                                                                                           `                 10.1021/acs.joc.5b00691         10.1007/s43630-022-00250-y      10.1021/jp0525078
    bod493    = 'BODIPY 493/503',                             'Cc1c2N(c(C)c1)[B-](F)(F)[N+]1c([C]2C)c(cc1C)C',                                   (8,8),   97100,  Solvents.tol,    500,   0.968,   Solvents.tol,   500,   5.6,   Solvents.tol,   False, True,  False
    #                                                                                                                                                  10.1016/j.dyepig.2015.11.007 (SI)  10.1016/j.dyepig.2015.11.007 (SI)   
    nda       = 'Naphthalamide',                              'O=C1C=2C=CC=C3C(O)=CC=C(C(=O)N1CCC)C32',                                          (12,12), 10000,  Solvents.dmso,   378,   0.77,    Solvents.dmso,  554,   0.00,  Solvents.none,  False, True,  False
    #                                                                                                                                                                                                                             Multiexponential fit also had small contribution of 0.19 ns
    #                                                                                                                                                     10.1016/0307-4412(94)90083-3    10.1111/j.1751-1097.1990.tb01686.x 10.  1016/0304-4165(89)90160-8
    dapi      = 'DAPI',                                       'N=C(C1=CC2=C(C=C1)C=C(C3=CC=C(C(N)=N)C=C3)N2)N',                                  (10,10), 27000,  Solvents.dmso,   333,   0.58,    Solvents.dmso,  310,   2.81,  Solvents.h2o,   False, True,  False  
    #                                                                                                                                                                                     10.1016/0003-2697(92)90003-P   10.1016/0003-2697(92)90003-P
    daa       = 'Dansyl amide',                               'CN(C)C1=CC=CC2=C1C=CC=C2S(=O)(=O)N',                                              (8,8),   0,      Solvents.none,   000,   0.39,    Solvents.etoh,  000,  17.1,   Solvents.etoh,  False, True,  False
    #                                                                                                                                                     10.1021/ja980508q               10.1021/ja980508q               10.1021/ja980508q
    bsc       = 'Boron Subphthalocyanine Chloride',           'B1(N2C3=C4C=CC=CC4=C2N=C5N1C(=NC6=NC(=N3)C7=CC=CC=C76)C8=CC=CC=C85)Cl',           (16,16), 63000,  Solvents.tol,    569,   0.25,    Solvents.tol,   000,   3.3,   Solvents.tol,   False, True,  False
    #                                                                                                                                                                                     10.1039/c4cc09206f              10.1039/c4cc09206f
    asp       = 'α-Sexithiophene',                            'c1csc(c1)-c2ccc(s2)-c3ccc(s3)-c4ccc(s4)-c5ccc(s5)-c6cccs6',                       (16,16), 0,      Solvents.none,   000,   0.41,    Solvents.dcm,   436,   1.0,   Solvents.dcm,   False, True,  False



    # Gas DS
    r575      = 'Rhodamine 575',                              'CCNc1cc2OC3=CC(=[N+]/CC)\C(C)=CC3=C(c2cc1C)c4ccccc4C([O-])=O',                    (0,0),   0,      Solvents.none,   000,   0.00,    Solvents.none,  000,   0.00,  Solvents.none,  False, False, True,    1
    fl        = 'Fluorescein',                                'c1ccc2c(c1)C(=O)OC23c4ccc(cc4Oc5c3ccc(c5)O)O',                                    (0,0),   0,      Solvents.none,   000,   0.00,    Solvents.none,  000,   0.00,  Solvents.none,  False, False, True,   -1
    bod8m     = '8-methoxy BODIPY',                           'c1c2N(cc1)[B-](F)(F)[N+]1c([C]2(OC))c(cc1)',                                      (8,8),   0,      Solvents.none,   000,   0.00,    Solvents.none,  000,   0.00,  Solvents.none,  False, False, True


    # ref
    #                                                                                                                                https://omlc.org/spectra/PhotochemCAD/html/083.html  10.1351/PAC-REP-10-09-31
    r6g       = 'Rhodamine 6G',                               'CC1=CC(C(C2=CC=CC=C2C(OCC)=O)=C3C=C/4C)=C(C=C1NCC)OC3=CC4=[NH+]\\CC',             (0,0),   116000, Solvents.etoh,   530,   0.94,    Solvents.etoh,  488,   0.00,  Solvents.none,  True,  False, False,  +1
    #                                                                                                                                https://omlc.org/spectra/PhotochemCAD/html/009.html  10.1351/PAC-REP-10-09-31
    rb        = 'Rhodamine B',                                'CC/[N+](CC)=C1C=CC2=C(C3=CC=CC=C3C(O)=O)C4=C(C=C(N(CC)CC)C=C4)OC2=C\\1',          (0,0),   106000, Solvents.etoh,   543,   0.70,    Solvents.meoh,  348,   0.00,  Solvents.none,  True,  False, False,  +1
    #                                                                                                                                                     10.1021/ac101329h               https://iss.com/resources/reference/data_tables/FL_QuantumYieldStandards.html
    cv        = 'Cresyl Violet',                              'N=1c4c(OC=3C=1c2ccccc2\C(=[NH2+])\C=3)cc(c(c4)C)N(C)C',                           (0,0),   63574,  Solvents.etoh,   611,   0.53,    Solvents.meoh,  580,   0.00,  Solvents.none,  True,  False, False,  +1
