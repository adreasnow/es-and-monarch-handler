from .newenum import *
from .software import Software
from .methods import Methods
from .basis import Basis
from .grids import Grids
from .pcm import PCM

class Jobs(NewEnum):
    def __init__(self, long:str) -> None:
            self.long    = long
            return
    
    def __str__(self):
      return self.long

    #       
    opt       = 'optimisation'
    freq      = 'frequencies'
    sp        = 'single_point'
    td        = 'td-dft'
    ex        = 'excitation'
    em        = 'emission'
    grad      = 'gradient'
    crest     = 'crest'
    casscf    = 'casscf_single_point'
    casscfOpt = 'casscf_optimisation'
    mp2Natorb = 'mp2-natural-orbitals'

class MetaJobs(NewEnum):
    def __init__(self, long:str, software:Software, job:Jobs, method:Methods, basis:Basis, grid:Grids, pcm:PCM, eq:PCM.Eq, excited:PCM.ExcitedModel, nroots:float, gs:bool, es:bool, used:bool=False, gasonly:bool=False) -> None:
            self.long       = long
            self.software   = software
            self.job        = job
            self.method     = method
            self.basis      = basis
            self.grid       = grid
            self.pcm        = pcm
            self.eq         = eq
            self.nroots     = nroots
            self.excited    = excited
            self.used       = used
            self.gasonly    = gasonly
            self.gs         = gs
            self.es         = es
            return
    
    def __str__(self):
        return self.long

    #                     job Decription                       Software        JobType             Method              Basis                Grid         PCM            Eq       Excitation Treatment  Nroots   GS      ES    Used Gas Only
    none               = 'None',                            'none',           'none',           'none',             'none',            'none',          'none',    'none',        'none',                 0,   False,  False, False
    # optimisations
    or_wb_opt_gs       = 'orca wb gs opt',                  Software.orca,    Jobs.opt,         Methods.wb97xd,     Basis.augccpvdz,   Grids.g75_302,   PCM.smd,   PCM.Eq.eq,     PCM.ExcitedModel.none,  1,   True,   False, True
    or_wb_opt_es       = 'orca wb es opt',                  Software.orca,    Jobs.opt,         Methods.wb97xd,     Basis.augccpvdz,   Grids.g75_302,   PCM.smd,   PCM.Eq.eq,     PCM.ExcitedModel.lr,    4,   False,  True,  True
    qc_wb_opt_gs       = 'qchem wb ss opt',                 Software.qchem,   Jobs.opt,         Methods.wb97xd,     Basis.augccpvdz,   Grids.g75_302,   PCM.cpcm,  PCM.Eq.eq,     PCM.ExcitedModel.none,  1,   True,   False
    qc_wb_opt_es       = 'qchem wb lr opt',                 Software.qchem,   Jobs.opt,         Methods.wb97xd,     Basis.augccpvdz,   Grids.g75_302,   PCM.cpcm,  PCM.Eq.eq,     PCM.ExcitedModel.lr,    4,   False,  True
    qc_wb_opt_ss_es    = 'qchem wb ss opt',                 Software.qchem,   Jobs.opt,         Methods.wb97xd,     Basis.augccpvdz,   Grids.g75_302,   PCM.cpcm,  PCM.Eq.eq,     PCM.ExcitedModel.clr,   4,   False,  True
    crest              = 'crest',                           Software.crest,   Jobs.crest,       Methods.crest,      Basis.none,        Grids.none,      PCM.alpb,  PCM.Eq.none,   PCM.ExcitedModel.none,  1,   True,   False
    casscf_opt         = 'casscf_optimisation',             Software.pyscf,   Jobs.casscfOpt,   Methods.casscf,     Basis.augccpvdz,   Grids.none,      PCM.none,  PCM.Eq.none,   PCM.ExcitedModel.none, 10,   True,   True,  False,  True
    mp2Natorb          = 'mp2-natural-orbitals',            Software.pyscf,   Jobs.mp2Natorb,   Methods.mp2,        Basis.d631pgd,     Grids.none,      PCM.none,  PCM.Eq.none,   PCM.ExcitedModel.none,  1,   True,   False, True,  True
    # frequencies 
    or_wb_freq_gs      = 'orca wb gs freq',                 Software.orca,    Jobs.freq,        Methods.wb97xd,     Basis.augccpvdz,   Grids.g75_302,   PCM.smd,   PCM.Eq.none,   PCM.ExcitedModel.none,  4,   True,   False
    or_wb_freq_es      = 'orca wb es freq',                 Software.orca,    Jobs.freq,        Methods.wb97xd,     Basis.augccpvdz,   Grids.g75_302,   PCM.smd,   PCM.Eq.eq,     PCM.ExcitedModel.lr,    4,   False,  True
    qc_wb_freq_gs      = 'qchem wb gs freq',                Software.qchem,   Jobs.freq,        Methods.wb97xd,     Basis.augccpvdz,   Grids.g75_302,   PCM.cpcm,  PCM.Eq.none,   PCM.ExcitedModel.none,  4,   True,   False
    qc_wb_freq_es      = 'qchem wb es freq',                Software.qchem,   Jobs.freq,        Methods.wb97xd,     Basis.augccpvdz,   Grids.g75_302,   PCM.cpcm,  PCM.Eq.eq,     PCM.ExcitedModel.lr,    4,   False,  True
    qc_wb_freq_ss_es   = 'qchem wb es freq',                Software.qchem,   Jobs.freq,        Methods.wb97xd,     Basis.augccpvdz,   Grids.g75_302,   PCM.cpcm,  PCM.Eq.eq,     PCM.ExcitedModel.clr,   4,   False,  True
    # excitations
    or_wb_ex           = 'orca wb smd ex',                  Software.orca,    Jobs.ex,          Methods.wb97xd,     Basis.augccpvdz,   Grids.g75_302,   PCM.smd,   PCM.Eq.neq,    PCM.ExcitedModel.lr,   10,   True,   True
    qc_wb_ex           = 'qchem wb ex',                     Software.qchem,   Jobs.ex,          Methods.wb97xd,     Basis.augccpvdz,   Grids.g75_302,   PCM.cpcm,  PCM.Eq.neq,    PCM.ExcitedModel.lr,   10,   True,   True
    qc_wb_ss_ex        = 'qchem wb ss ex',                  Software.qchem,   Jobs.ex,          Methods.wb97xd,     Basis.augccpvdz,   Grids.g75_302,   PCM.cpcm,  PCM.Eq.neq,    PCM.ExcitedModel.clr,  10,   True,   True
    # emission
    qc_wb_em           = 'qchem wb em',                     Software.qchem,   Jobs.em,          Methods.wb97xd,     Basis.augccpvdz,   Grids.g75_302,   PCM.cpcm,  PCM.Eq.eq_neq, PCM.ExcitedModel.lr,    4,   False,  True
    qc_wb_ss_em        = 'qchem wb ss em',                  Software.qchem,   Jobs.em,          Methods.wb97xd,     Basis.augccpvdz,   Grids.g75_302,   PCM.cpcm,  PCM.Eq.eq_neq, PCM.ExcitedModel.clr,   4,   False,  True, True
    # single point
    casscf_scan        = 'casscf_single_point',             Software.pyscf,   Jobs.casscf,      Methods.casscf,     Basis.augccpvdz,   Grids.none,      PCM.none,  PCM.Eq.none,   PCM.ExcitedModel.clr,  10,   True,  True, False,  True
