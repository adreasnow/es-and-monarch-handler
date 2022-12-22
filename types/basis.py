from .newenum import *
from .software import Software
class Basis(NewEnum):
    class Family(Enum):
        dunning   = 'dunning'
        pople     = 'pople'
        jensen    = 'jensen'
        karlsruhe = 'karlsruhe'
        none      = 'none'

    def __init__(self, basis:str, orca:str, qchem:str, nwchem:str, psi4:str, pyscf:str, zeta:int, augmented:bool, diffuse:bool, family:Family) -> None:
            self.basis     = basis
            self.orca      = orca
            self.pyscf     = pyscf
            self.qchem     = qchem
            self.nwchem    = nwchem
            self.psi4      = psi4
            self.zeta      = zeta
            self.family    = family
            self.augmented = augmented
            self.diffuse   = diffuse
            return

    def __str__(self):
      return self.basis

    def __repr__(self):
      return self.basis

    #               basis               orca               qchem             nwchem              psi4               pyscf           𝜁  Polar  Diff         Family
    none         = 'None',             None,              None,              None,              None,              None,            0, False, False,  Family.none
    ccpvdz       = 'cc-pVDZ',         'cc-pvdz',         'cc-pvdz',         'cc-pvdz',         'cc-pvdz',         'cc-pvdz',        2, True,  False,  Family.dunning
    ccpvtz       = 'cc-pVTZ',         'cc-pvtz',         'cc-pvtz',         'cc-pvtz',         'cc-pvtz',         'cc-pvtz',        3, True,  False,  Family.dunning
    ccpvqz       = 'cc-pVQZ',         'cc-pvqz',         'cc-pvqz',         'cc-pvqz',         'cc-pvqz',         'cc-pvqz',        4, True,  False,  Family.dunning
    augccpvdz    = 'aug-cc-pVDZ',     'aug-cc-pvdz',     'aug-cc-pvdz',     'aug-cc-pvdz',     'aug-cc-pvdz',     'aug-cc-pvdz',    2, True,  True,   Family.dunning
    augccpvtz    = 'aug-cc-pVTZ',     'aug-cc-pvtz',     'aug-cc-pvtz',     'aug-cc-pvtz',     'aug-cc-pvtz',     'aug-cc-pvtz',    3, True,  True,   Family.dunning
    augccpvqz    = 'aug-cc-pVQZ',     'aug-cc-pvqz',     'aug-cc-pvqz',     'aug-cc-pvqz',     'aug-cc-pvqz',     'aug-cc-pvqz',    4, True,  True,   Family.dunning
    def2svp      = 'Def2-SVP',        'def2-svp',        'def2-svp',        'def2-svp',        'def2-svp',        'def2-svp',       1, True,  False,  Family.karlsruhe
    def2tzvp     = 'Def2-TZVP',       'def2-tzvp',       'def2-tzvp',       'def2-tzvp',       'def2-tzvp',       'def2-tzvp',      3, True,  False,  Family.karlsruhe
    def2qzvp     = 'Def2-QZVP',       'def2-qzvp',       'def2-qzvp',       'def2-qzvp',       'def2-qzvp',       'def2-qzvp',      4, True,  False,  Family.karlsruhe
    def2svpd     = 'Def2-SVPD',       'def2-svpd',       'def2-svpd',       'def2-svpd',       'def2-svpd',       'def2-svpd',      1, True,  True,   Family.karlsruhe
    def2tzvpd    = 'Def2-TZVPD',      'def2-tzvpd',      'def2-tzvpd',      'def2-tzvpd',      'def2-tzvpd',      'def2-tzvpd',     3, True,  True,   Family.karlsruhe
    def2qzvpd    = 'Def2-QZVPD',      'def2-qzvpd',      'def2-qzvpd',      'def2-qzvpd',      'def2-qzvpd',      'def2-qzvpd',     4, True,  True,   Family.karlsruhe
    def2tzvppd   = 'Def2-TZVPPD',     'def2-tzvppd',     'def2-tzvppd',     'def2-tzvppd',      None,              None,            3, True,  True,   Family.karlsruhe
    def2qzvppd   = 'Def2-QZVPPD',     'def2-qzvppd',     'def2-qzvppd',     'def2-qzvppd',      None,              None,            4, True,  True,   Family.karlsruhe
    madef2svp    = 'ma-Def2-SVP',     'ma-def2-svp',      None,              None,              None,              None,            1, True,  True,   Family.karlsruhe
    madef2tzvp   = 'ma-Def2-TZVP',    'ma-def2-tzvp',     None,              None,              None,              None,            3, True,  True,   Family.karlsruhe
    madef2qzvp   = 'ma-Def2-QZVP',    'ma-def2-qzvp',     None,              None,              None,              None,            4, True,  True,   Family.karlsruhe
    madef2tzvpp  = 'ma-Def2-TZVPP',   'ma-def2-tzvpp',    None,              None,              None,              None,            3, True,  True,   Family.karlsruhe
    madef2qzvpp  = 'ma-Def2-QZVPP',   'ma-def2-qzvpp',    None,              None,              None,              None,            4, True,  True,   Family.karlsruhe
    pc0          = 'pc-0',            'pc-0',            'pc-0',            'pc-0',             None,              None,            1, False, False,  Family.jensen
    pc1          = 'pc-1',            'pc-1',            'pc-1',            'pc-1',             None,              None,            2, False, False,  Family.jensen
    pc2          = 'pc-2',            'pc-2',            'pc-2',            'pc-2',             None,              None,            3, False, False,  Family.jensen
    pc3          = 'pc-3',            'pc-3',            'pc-3',            'pc-3',             None,              None,            4, False, False,  Family.jensen
    augpc0       = 'aug-pc-0',        'aug-pc-0',         None,             'aug-pc-0',         None,              None,            1, False, False,  Family.jensen
    augpc1       = 'aug-pc-1',        'aug-pc-1',         None,             'aug-pc-1',         None,              None,            2, False, False,  Family.jensen
    augpc2       = 'aug-pc-2',        'aug-pc-2',         None,             'aug-pc-2',         None,              None,            3, False, False,  Family.jensen
    augpc3       = 'aug-pc-3',        'aug-pc-3',         None,             'aug-pc-3',         None,              None,            4, False, False,  Family.jensen
    d631g        = '6-31G',           '6-31G',           '6-31G',           '6-31G',           '6-31G',           '6-31G',          2, False, False,  Family.pople
    d631gd       = '6-31G(d)',        '6-31G(d)',        '6-31G(d)',        '6-31G*',          '6-31G(d)',        '6-31G(d)',       2, True,  False,  Family.pople
    d631gdp      = '6-31G(d,p)',      '6-31G(d,p)',      '6-31G(d,p)',      '6-31G**',         '6-31G(d,p)',      '6-31G(d,p)',     2, True,  False,  Family.pople
    d631g2d2p    = '6-31G(2d,2p)',    '6-31G(2d,2p)',    '6-31G(2d,2p)',    '6-31G(2d,2p)',    '6-31G(2d,2p)',    '6-31G(2d,2p)',   2, True,  False,  Family.pople
    d631pg       = '6-31+G',          '6-31+G',          '6-31+G',          '6-31+G',          '6-31+G',          '6-31+G',         2, False, True,   Family.pople
    d631pgd      = '6-31+G(d)',       '6-31+G(d)',       '6-31+G(d)',       '6-31+G*',         '6-31+G(d)',       '6-31+G(d)',      2, True,  True,   Family.pople
    d631pgdp     = '6-31+G(d,p)',     '6-31+G(d,p)',     '6-31+G(d,p)',     '6-31+G**',        '6-31+G(d,p)',     '6-31+G(d,p)',    2, True,  True,   Family.pople
    d631pg2d2p   = '6-31+G(2d,2p)',   '6-31+G(2d,2p)',   '6-31+G(2d,2p)',   '6-31+G(2d,2p)',   '6-31+G(2d,2p)',   '6-31+G(2d,2p)',  2, True,  True,   Family.pople
    d631ppg      = '6-31++G',         '6-31++G',         '6-31++G',         '6-31++G',         '6-31++G',         '6-31++G',        2, False, True,   Family.pople
    d631ppgd     = '6-31++G(d)',      '6-31++G(d)',      '6-31++G(d)',      '6-31++G*',        '6-31++G(d)',      '6-31++G(d)',     2, True,  True,   Family.pople
    d631ppgdp    = '6-31++G(d,p)',    '6-31++G(d,p)',    '6-31++G(d,p)',    '6-31++G**',       '6-31++G(d,p)',    '6-31++G(d,p)',   2, True,  True,   Family.pople
    d631ppg2d2p  = '6-31++G(2d,2p)',  '6-31++G(2d,2p)',  '6-31++G(2d,2p)',  '6-31++G(2d,2p)',  '6-31++G(2d,2p)',  '6-31++G(2d,2p)', 2, True,  True,   Family.pople
    d6311g       = '6-311G',          '6-311G',          '6-311G',          '6-311G',          '6-311G',          '6-311G',         3, False, False,  Family.pople
    d6311gd      = '6-311G(d)',       '6-311G(d)',       '6-311G(d)',       '6-311G*',         '6-311G(d)',       '6-311G(d)',      3, True,  False,  Family.pople
    d6311gdp     = '6-311G(d,p)',     '6-311G(d,p)',     '6-311G(d,p)',     '6-311G**',        '6-311G(d,p)',     '6-311G(d,p)',    3, True,  False,  Family.pople
    d6311g2d2p   = '6-311G(2d,2p)',   '6-311G(2d,2p)',   '6-311G(2d,2p)',   '6-311G(2d,2p)',   '6-311G(2d,2p)',   '6-311G(2d,2p)',  3, True,  False,  Family.pople
    d6311pg      = '6-311+G',         '6-311+G',         '6-311+G',         '6-311+G',         '6-311+G',         '6-311+G',        3, False, True,   Family.pople
    d6311pgd     = '6-311+G(d)',      '6-311+G(d)',      '6-311+G(d)',      '6-311+G*',        '6-311+G(d)',      '6-311+G(d)',     3, True,  True,   Family.pople
    d6311pgdp    = '6-311+G(d,p)',    '6-311+G(d,p)',    '6-311+G(d,p)',    '6-311+G**',       '6-311+G(d,p)',    '6-311+G(d,p)',   3, True,  True,   Family.pople
    d6311pg2d2p  = '6-311+G(2d,2p)',  '6-311+G(2d,2p)',  '6-311+G(2d,2p)',  '6-311+G(2d,2p)',  '6-311+G(2d,2p)',  '6-311+G(2d,2p)', 3, True,  True,   Family.pople
    d6311ppg     = '6-311++G',        '6-311++G',        '6-311++G',        '6-311++G',        '6-311++G',        '6-311++G',       3, False, True,   Family.pople
    d6311ppgd    = '6-311++G(d)',     '6-311++G(d)',     '6-311++G(d)',     '6-311++G*',       '6-311++G(d)',     '6-311++G(d)',    3, True,  True,   Family.pople
    d6311ppgdp   = '6-311++G(d,p)',   '6-311++G(d,p)',   '6-311++G(d,p)',   '6-311++G**',      '6-311++G(d,p)',   '6-311++G(d,p)',  3, True,  True,   Family.pople
    d6311ppg2d2p = '6-311++G(2d,2p)', '6-311++G(2d,2p)', '6-311++G(2d,2p)', '6-311++G(2d,2p)', '6-311++G(2d,2p)', '6-311++G(2d,2p)',3, True,  True,   Family.pople
