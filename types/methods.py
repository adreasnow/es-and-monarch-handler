from .newenum import *
class Methods(NewEnum):
    class Rank(Enum):
        lda          = auto()
        gga          = auto()
        meta         = auto()
        hybrid       = auto()
        hybridMeta   = auto()
        doubleHybrid = auto()
        none         = auto()

    class Dispersion(Enum):
        none = auto()
        d3   = auto()
        vv10 = auto()

    class Spin_Scaling(Enum):
        none = auto()
        sos = auto()
        srs = auto()
        sns = auto()

    def __init__(self, method:str, orca:str, nwchem:str, qchem:str, psi4:str, pyscf:str,
                 rank:Rank, range_separated:bool, dispersion:Dispersion, spin_scaling:Spin_Scaling, used:bool) -> None:
            self.method          = method
            self.orca            = orca
            self.qchem           = qchem
            self.nwchem          = nwchem
            self.psi4            = psi4
            self.pyscf           = pyscf
            self.range_separated = range_separated
            self.rank            = rank
            self.dispersion      = dispersion
            self.spin_scaling    = spin_scaling
            self.used            = used
            return

    def __str__(self):
        return self.name

    def __bool__(self):
        return self.used

    #              Method               orca               nwchem                            qchem         psi4         pyscf         rank              ω        dispersion         spin scaling         used
    b3lyp       = 'B3LYP',            'B3LYP',           'B3LYP',                           'B3LYP',     'b3LYP',     'b3LYP',      Rank.hybrid,       False,   Dispersion.none,   Spin_Scaling.none,   False
    cb3lyp      = 'CAM-B3LYP',        'CAM-B3LYP',       'hyb_gga_xc_cam_b3lyp',            'cam-b3lyp', 'cam-b3lyp', 'camb3lyp',   Rank.hybrid,       True,    Dispersion.none,   Spin_Scaling.none,   False
    bmk         = 'BMK',               None,             'GGA_C_BMK  HYB_MGGA_X_BMK',       'bmk',       'bmk',       'bmk',        Rank.hybridMeta,   False,   Dispersion.none,   Spin_Scaling.none,   False
    wb97xd      = 'ωB97X-D3',         'wb97x-d3',        'hyb_gga_xc_wb97x_D3',             'wb97x-d3',  'wb97x-d',   'wb97xd',     Rank.hybrid,       True,    Dispersion.d3,     Spin_Scaling.none,   True
    wb97mv      = 'ωB97M-V',          'wb97m-v',          None,                             'wb97m-v',   'wb97m-v',   'wb97mv',     Rank.hybridMeta,   True,    Dispersion.vv10,   Spin_Scaling.none,   False
    m062x       = 'M06-2X',           'm06-2x',          'MGGA_C_M06_2X HYB_MGGA_X_M06_2X', 'm06-2x',    'm06-2x',    'm062x',      Rank.hybridMeta,   False,   Dispersion.none,   Spin_Scaling.none,   False
    sospbeqidh  = 'SOS-PBE-QIDH',     'ri-sos-pbe-qidh',  None,                              None,        None,        None,        Rank.doubleHybrid, False,   Dispersion.none,   Spin_Scaling.sos,    False
    soswpbepp86 = 'SOS-PBE-ωPBEPP86', 'ri-sos-wpbepp86',  None,                              None,        None,        None,        Rank.doubleHybrid, True,    Dispersion.none,   Spin_Scaling.sos,    False
    crest       = None,                None,              None,                              None,        None,        None,        Rank.none,         False,   Dispersion.none,   Spin_Scaling.none,   False   
    casscf      = None,                None,              None,                              None,        'casscf',    'casscf',    Rank.none,         False,   Dispersion.none,   Spin_Scaling.none,   False
    mp2         = 'MP2',               'RI-MP2',          None,                              None,        None,        None,        Rank.none,         False,   Dispersion.none,   Spin_Scaling.none,   False 
