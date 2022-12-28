from .newenum import *
from .software import Software
from .methods import Methods
from .basis import Basis
from .grids import Grids
from .pcm import PCM
from .tddft import TDDFT

class Jobs(NewEnum):
    def __init__(self, long:str) -> None:
            self.long = long
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
    def __init__(self, long:str, software:Software, job:Jobs, method:Methods, basis:Basis, grid:Grids, tddft:TDDFT, pcm:PCM, eq:PCM.Eq, excited:PCM.ExcitedModel, nroots:float, gs:bool, es:bool, used:bool, gasonly:bool, triplets:TDDFT.Triplets, pcm_form:PCM.Formalism, pcm_disc:PCM.Discretisation, pcm_radii:PCM.Radii, pcm_VDWScale:float, pcm_probe_radii:float, pcm_surfaceType:PCM.Cavity) -> None:
            self.long             = long
            self.software         = software
            self.job              = job
            self.method           = method
            self.basis            = basis
            self.grid             = grid
            self.pcm              = pcm
            self.eq               = eq
            self.nroots           = nroots
            self.excited          = excited
            self.used             = used
            self.gasonly          = gasonly
            self.gs               = gs
            self.es               = es
            self.tddft            = tddft
            self.triplets         = triplets
            self.pcm_form         = pcm_form
            self.pcm_disc         = pcm_disc
            self.pcm_radii        = pcm_radii
            self.pcm_VDWScale     = pcm_VDWScale
            self.pcm_probe_radii  = pcm_probe_radii
            self.pcm_surfaceType  = pcm_surfaceType
            return
    
    def __str__(self):
        return self.long

    #                     job Decription                       Software        JobType             Method              Basis                Grid         TDDFT           PCM            Eq       Excitation Treatment  Nroots   GS      ES    Used  Gas Only        Triplets            PCM Formalism             PCM Discretisation            PCM Radii set    VDW r  Probe r         Cavity
    none               = 'None',                            'none',           'none',           'none',             'none',            'none',          'none',        'none',    'none',        'none',                   0,   False,  False, False, False,   TDDFT.Triplets.off,   PCM.Formalism.none,      PCM.Discretisation.default,     PCM.Radii.default,   1.2,    0.0,      PCM.Cavity.default
    
    # optimisations
    or_wb_opt_gs       = 'orca wb gs opt',                  Software.orca,    Jobs.opt,         Methods.wb97xd,     Basis.augccpvdz,   Grids.g75_302,   TDDFT.none,     PCM.smd,   PCM.Eq.eq,      PCM.ExcitedModel.none,  1,   True,   False, True,  False,   TDDFT.Triplets.off,   PCM.Formalism.cpcm,      PCM.Discretisation.default,     PCM.Radii.default,   1.2,    0.0,      PCM.Cavity.default
    or_wb_opt_es       = 'orca wb es opt',                  Software.orca,    Jobs.opt,         Methods.wb97xd,     Basis.augccpvdz,   Grids.g75_302,   TDDFT.tddft,    PCM.smd,   PCM.Eq.eq,      PCM.ExcitedModel.lr,    4,   False,  True,  True,  False,   TDDFT.Triplets.off,   PCM.Formalism.cpcm,      PCM.Discretisation.default,     PCM.Radii.default,   1.2,    0.0,      PCM.Cavity.default
    qc_wb_opt_gs       = 'qchem wb opt',                    Software.qchem,   Jobs.opt,         Methods.wb97xd,     Basis.augccpvdz,   Grids.g75_302,   TDDFT.none,     PCM.cpcm,  PCM.Eq.eq,      PCM.ExcitedModel.none,  1,   True,   False, False, False,   TDDFT.Triplets.off,   PCM.Formalism.iefpcm,    PCM.Discretisation.default,     PCM.Radii.default,   1.2,    0.0,      PCM.Cavity.default
    qc_wb_opt_es       = 'qchem wb lr opt',                 Software.qchem,   Jobs.opt,         Methods.wb97xd,     Basis.augccpvdz,   Grids.g75_302,   TDDFT.tddft,    PCM.cpcm,  PCM.Eq.eq,      PCM.ExcitedModel.lr,    4,   False,  True,  False, False,   TDDFT.Triplets.off,   PCM.Formalism.iefpcm,    PCM.Discretisation.default,     PCM.Radii.default,   1.2,    0.0,      PCM.Cavity.default
    qc_wb_opt_ss_es    = 'qchem wb ss opt',                 Software.qchem,   Jobs.opt,         Methods.wb97xd,     Basis.augccpvdz,   Grids.g75_302,   TDDFT.tddft,    PCM.cpcm,  PCM.Eq.eq,      PCM.ExcitedModel.clr,   4,   False,  True,  False, False,   TDDFT.Triplets.off,   PCM.Formalism.iefpcm,    PCM.Discretisation.default,     PCM.Radii.default,   1.2,    0.0,      PCM.Cavity.default
    crest              = 'crest',                           Software.crest,   Jobs.crest,       Methods.crest,      Basis.none,        Grids.none,      TDDFT.none,     PCM.alpb,  PCM.Eq.none,    PCM.ExcitedModel.none,  1,   True,   False, False, False,   TDDFT.Triplets.off,   PCM.Formalism.pb,        PCM.Discretisation.default,     PCM.Radii.default,   1.2,    0.0,      PCM.Cavity.default
    casscf_opt         = 'casscf_optimisation',             Software.pyscf,   Jobs.casscfOpt,   Methods.casscf,     Basis.augccpvdz,   Grids.none,      TDDFT.none,     PCM.none,  PCM.Eq.none,    PCM.ExcitedModel.none, 10,   True,   True,  True,  True,    TDDFT.Triplets.off,   PCM.Formalism.none,      PCM.Discretisation.default,     PCM.Radii.default,   1.2,    0.0,      PCM.Cavity.default
    mp2Natorb          = 'mp2-natural-orbitals',            Software.pyscf,   Jobs.mp2Natorb,   Methods.mp2,        Basis.d631pgd,     Grids.none,      TDDFT.none,     PCM.none,  PCM.Eq.none,    PCM.ExcitedModel.none,  1,   True,   False, True,  True,    TDDFT.Triplets.off,   PCM.Formalism.none,      PCM.Discretisation.default,     PCM.Radii.default,   1.2,    0.0,      PCM.Cavity.default
    
    # frequencies 
    or_wb_freq_gs      = 'orca wb gs freq',                 Software.orca,    Jobs.freq,        Methods.wb97xd,     Basis.augccpvdz,   Grids.g75_302,   TDDFT.none,     PCM.smd,   PCM.Eq.eq,      PCM.ExcitedModel.none,  4,   True,   False, True,  False,   TDDFT.Triplets.off,   PCM.Formalism.cpcm,      PCM.Discretisation.default,     PCM.Radii.default,   1.2,    0.0,      PCM.Cavity.default
    or_wb_freq_es      = 'orca wb es freq',                 Software.orca,    Jobs.freq,        Methods.wb97xd,     Basis.augccpvdz,   Grids.g75_302,   TDDFT.tddft,    PCM.smd,   PCM.Eq.eq,      PCM.ExcitedModel.lr,    4,   False,  True,  False, False,   TDDFT.Triplets.off,   PCM.Formalism.cpcm,      PCM.Discretisation.default,     PCM.Radii.default,   1.2,    0.0,      PCM.Cavity.default
    qc_wb_freq_gs      = 'qchem wb gs freq',                Software.qchem,   Jobs.freq,        Methods.wb97xd,     Basis.augccpvdz,   Grids.g75_302,   TDDFT.none,     PCM.cpcm,  PCM.Eq.eq,      PCM.ExcitedModel.none,  4,   True,   False, False, False,   TDDFT.Triplets.off,   PCM.Formalism.iefpcm,    PCM.Discretisation.default,     PCM.Radii.default,   1.2,    0.0,      PCM.Cavity.default
    qc_wb_freq_es      = 'qchem wb es freq',                Software.qchem,   Jobs.freq,        Methods.wb97xd,     Basis.augccpvdz,   Grids.g75_302,   TDDFT.tddft,    PCM.cpcm,  PCM.Eq.eq,      PCM.ExcitedModel.lr,    4,   False,  True,  False, False,   TDDFT.Triplets.off,   PCM.Formalism.iefpcm,    PCM.Discretisation.default,     PCM.Radii.default,   1.2,    0.0,      PCM.Cavity.default
    qc_wb_freq_ss_es   = 'qchem wb es freq',                Software.qchem,   Jobs.freq,        Methods.wb97xd,     Basis.augccpvdz,   Grids.g75_302,   TDDFT.tddft,    PCM.cpcm,  PCM.Eq.eq,      PCM.ExcitedModel.clr,   4,   False,  True,  False, False,   TDDFT.Triplets.off,   PCM.Formalism.iefpcm,    PCM.Discretisation.default,     PCM.Radii.default,   1.2,    0.0,      PCM.Cavity.default
    
    # excitations
    or_wb_ex           = 'orca wb smd ex',                  Software.orca,    Jobs.ex,          Methods.wb97xd,     Basis.augccpvdz,   Grids.g75_302,   TDDFT.tddft,    PCM.smd,   PCM.Eq.neq,     PCM.ExcitedModel.lr,   10,   True,   True,  False, False,   TDDFT.Triplets.off,   PCM.Formalism.cpcm,      PCM.Discretisation.default,     PCM.Radii.default,   1.2,    0.0,      PCM.Cavity.default
    qc_wb_ex           = 'qchem wb ex',                     Software.qchem,   Jobs.ex,          Methods.wb97xd,     Basis.augccpvdz,   Grids.g75_302,   TDDFT.tddft,    PCM.cpcm,  PCM.Eq.neq,     PCM.ExcitedModel.lr,   10,   True,   True,  False, False,   TDDFT.Triplets.off,   PCM.Formalism.iefpcm,    PCM.Discretisation.default,     PCM.Radii.default,   1.2,    0.0,      PCM.Cavity.default
    qc_wb_ss_ex        = 'qchem wb ss ex',                  Software.qchem,   Jobs.ex,          Methods.wb97xd,     Basis.augccpvdz,   Grids.g75_302,   TDDFT.tddft,    PCM.sspcm, PCM.Eq.neq,     PCM.ExcitedModel.clr,  10,   True,   True,  True,  False,   TDDFT.Triplets.off,   PCM.Formalism.iefpcm,    PCM.Discretisation.default,     PCM.Radii.default,   1.2,    0.0,      PCM.Cavity.default
    
    # emission
    # qc_wb_em           = 'qchem wb em',                     Software.qchem,   Jobs.em,          Methods.wb97xd,     Basis.augccpvdz,   Grids.g75_302,   TDDFT.tddft,    PCM.cpcm,  PCM.Eq.eq_neq,  PCM.ExcitedModel.lr,    4,   False,  True,  False, False,   TDDFT.Triplets.off,   PCM.Formalism.iefpcm,    PCM.Discretisation.default,     PCM.Radii.default,   1.2,    0.0,      PCM.Cavity.default
    qc_wb_ss_em        = 'qchem wb ss em',                  Software.qchem,   Jobs.em,          Methods.wb97xd,     Basis.augccpvdz,   Grids.g99_590,   TDDFT.tddft,    PCM.sspcm,  PCM.Eq.eq_neq, PCM.ExcitedModel.clr,   4,   False,  True,  True,  False,   TDDFT.Triplets.off,   PCM.Formalism.iefpcm,    PCM.Discretisation.default,     PCM.Radii.default,   1.2,    0.0,      PCM.Cavity.default
    
    # single point
    casscf_scan        = 'casscf_single_point',             Software.pyscf,   Jobs.casscf,      Methods.casscf,     Basis.augccpvdz,   Grids.none,      TDDFT.none,     PCM.none,  PCM.Eq.none,    PCM.ExcitedModel.clr,  10,   True,   True,  False, True,    TDDFT.Triplets.off,   PCM.Formalism.none,      PCM.Discretisation.default,     PCM.Radii.default,   1.2,    0.0,      PCM.Cavity.default


    PCM.Discretisation.default,     PCM.Radii.default,   1.2,    0.0,      PCM.Cavity.default