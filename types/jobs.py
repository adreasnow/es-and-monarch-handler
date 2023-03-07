from .newenum import NewEnum
from .software import Software
from .methods import Methods
from .basis import Basis
from .grids import Grids
from .pcm import PCM
from .tddft import TDDFT


class Jobs(NewEnum):
    def __init__(self, long: str) -> None:
        self.long = long
        return

    def __str__(self):
        return self.long

    #
    opt        = 'optimisation'
    freq       = 'frequencies'
    sp         = 'single_point'
    td         = 'td-dft'
    ex         = 'excitation'
    em         = 'emission'
    grad       = 'gradient'
    crest      = 'crest'
    casscf     = 'casscf_single_point'
    caspt2     = 'caspt2_single_point'
    nevpt2     = 'nevpt2_single_point'
    casscfOpt  = 'casscf_optimisation'
    casscfFreq = 'casscf_frequencies'
    mp2Natorb  = 'mp2-natural-orbitals'
    pol        = 'polarisabilities'
    esd        = 'excited_state_dynamics'

class MetaJobs(NewEnum):
    def __init__(self, long: str,
                 software: Software,
                 job: Jobs,
                 method: Methods,
                 basis: Basis,
                 grid: Grids,
                 tddft: TDDFT,
                 pcm: PCM,
                 eq: PCM.Eq,
                 excited: PCM.ExcitedModel,
                 nroots: float,
                 gs: bool,
                 es: bool,
                 used: bool,
                 gasonly: bool,
                 triplets: TDDFT.Triplets,
                 pcm_form: PCM.Formalism,
                 pcm_disc: PCM.Discretisation,
                 pcm_radii: PCM.Radii,
                 pcm_VDWScale: float,
                 pcm_probe_radii: float,
                 pcm_surfaceType: PCM.Cavity,
                 perturbed: float,
                 sa: bool) -> None:
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
        self.perturbed        = perturbed
        self.sa               = sa
        return

    def __str__(self):
        return self.long

    #                     job Decription                       Software        JobType             Method              Basis                Grid         TDDFT           PCM            Eq       Excitation Treatment  Nroots   GS      ES    Used  Gas Only        Triplets            PCM Formalism             PCM Discretisation            PCM Radii set    VDW r  Probe r         Cavity       Perturbed Roots   SA
    none               = 'None',                            'none',           'none',           'none',             'none',            'none',          'none',        'none',    'none',        'none',                   0,   False,  False, False, False,   TDDFT.Triplets.off,   PCM.Formalism.none,      PCM.Discretisation.default,     PCM.Radii.default,   1.2,    0.0,      PCM.Cavity.default,    0,        False

    # optimisations
    or_wb_opt          = 'orca wb opt',                     Software.orca,    Jobs.opt,         Methods.wb97xd,     Basis.augccpvdz,   Grids.g99_590,   TDDFT.tddft,    PCM.smd,   PCM.Eq.eq,      PCM.ExcitedModel.lr,    4,   True,   True,  True,  False,   TDDFT.Triplets.off,   PCM.Formalism.cpcm,      PCM.Discretisation.default,     PCM.Radii.default,   1.2,    0.0,      PCM.Cavity.default,    0,        False
    or_cb_opt          = 'orca cb opt',                     Software.orca,    Jobs.opt,         Methods.cb3lyp,     Basis.augccpvdz,   Grids.g99_590,   TDDFT.tddft,    PCM.smd,   PCM.Eq.eq,      PCM.ExcitedModel.lr,    4,   True,   True,  True,  False,   TDDFT.Triplets.off,   PCM.Formalism.cpcm,      PCM.Discretisation.default,     PCM.Radii.default,   1.2,    0.0,      PCM.Cavity.default,    0,        False
    qc_wb_opt_lr       = 'qchem wb lr opt',                 Software.qchem,   Jobs.opt,         Methods.wb97xd,     Basis.augccpvdz,   Grids.g99_590,   TDDFT.tddft,    PCM.cpcm,  PCM.Eq.eq,      PCM.ExcitedModel.lr,    4,   True,   True,  False, False,   TDDFT.Triplets.off,   PCM.Formalism.iefpcm,    PCM.Discretisation.default,     PCM.Radii.default,   1.2,    0.0,      PCM.Cavity.default,    0,        False
    qc_wb_opt_ss       = 'qchem wb ss opt',                 Software.qchem,   Jobs.opt,         Methods.wb97xd,     Basis.augccpvdz,   Grids.g99_590,   TDDFT.tddft,    PCM.cpcm,  PCM.Eq.eq,      PCM.ExcitedModel.clr,   4,   True,   True,  False, False,   TDDFT.Triplets.off,   PCM.Formalism.iefpcm,    PCM.Discretisation.default,     PCM.Radii.default,   1.2,    0.0,      PCM.Cavity.default,    0,        False
    crest              = 'crest',                           Software.crest,   Jobs.crest,       Methods.crest,      Basis.none,        Grids.none,      TDDFT.none,     PCM.alpb,  PCM.Eq.none,    PCM.ExcitedModel.none,  1,   True,   False, False, False,   TDDFT.Triplets.off,   PCM.Formalism.pb,        PCM.Discretisation.default,     PCM.Radii.default,   1.2,    0.0,      PCM.Cavity.default,    0,        False
    casscf_opt         = 'casscf_optimisation',             Software.orca,    Jobs.casscfOpt,   Methods.casscf,     Basis.augccpvdz,   Grids.none,      TDDFT.none,     PCM.none,  PCM.Eq.none,    PCM.ExcitedModel.none,  4,   True,   True,  True,  True,    TDDFT.Triplets.off,   PCM.Formalism.none,      PCM.Discretisation.default,     PCM.Radii.default,   1.2,    0.0,      PCM.Cavity.default,    0,        False
    mp2Natorb          = 'mp2-natural-orbitals',            Software.orca,    Jobs.mp2Natorb,   Methods.mp2,        Basis.augccpvdz,   Grids.none,      TDDFT.none,     PCM.none,  PCM.Eq.none,    PCM.ExcitedModel.none,  1,   True,   False, True,  True,    TDDFT.Triplets.off,   PCM.Formalism.none,      PCM.Discretisation.default,     PCM.Radii.default,   1.2,    0.0,      PCM.Cavity.default,    0,        False

    # frequencies
    or_wb_freq         = 'orca wb freq',                    Software.orca,    Jobs.freq,        Methods.wb97xd,     Basis.augccpvdz,   Grids.g99_590,   TDDFT.tddft,    PCM.smd,   PCM.Eq.eq,      PCM.ExcitedModel.none,  4,   True,   True,  True,  False,   TDDFT.Triplets.off,   PCM.Formalism.cpcm,      PCM.Discretisation.default,     PCM.Radii.default,   1.2,    0.0,      PCM.Cavity.default,    0,        False
    or_cb_freq         = 'orca cb freq',                    Software.orca,    Jobs.freq,        Methods.cb3lyp,     Basis.augccpvdz,   Grids.g99_590,   TDDFT.tddft,    PCM.smd,   PCM.Eq.eq,      PCM.ExcitedModel.none,  4,   True,   True,  True,  False,   TDDFT.Triplets.off,   PCM.Formalism.cpcm,      PCM.Discretisation.default,     PCM.Radii.default,   1.2,    0.0,      PCM.Cavity.default,    0,        False
    qc_wb_freq         = 'qchem wb freq',                   Software.qchem,   Jobs.freq,        Methods.wb97xd,     Basis.augccpvdz,   Grids.g99_590,   TDDFT.tddft,    PCM.cpcm,  PCM.Eq.eq,      PCM.ExcitedModel.none,  4,   True,   True,  False, False,   TDDFT.Triplets.off,   PCM.Formalism.iefpcm,    PCM.Discretisation.default,     PCM.Radii.default,   1.2,    0.0,      PCM.Cavity.default,    0,        False
    qc_wb_freq_ss      = 'qchem wb freq',                   Software.qchem,   Jobs.freq,        Methods.wb97xd,     Basis.augccpvdz,   Grids.g99_590,   TDDFT.tddft,    PCM.cpcm,  PCM.Eq.eq,      PCM.ExcitedModel.clr,   4,   True,   True,  False, False,   TDDFT.Triplets.off,   PCM.Formalism.iefpcm,    PCM.Discretisation.default,     PCM.Radii.default,   1.2,    0.0,      PCM.Cavity.default,    0,        False
    casscf_freq        = 'casscf_freq',                     Software.orca,    Jobs.casscfFreq,  Methods.casscf,     Basis.augccpvdz,   Grids.none,      TDDFT.none,     PCM.none,  PCM.Eq.none,    PCM.ExcitedModel.clr,   4,   True,   True,  True,  True,    TDDFT.Triplets.off,   PCM.Formalism.none,      PCM.Discretisation.default,     PCM.Radii.default,   1.2,    0.0,      PCM.Cavity.default,    4,        False

    # excitation
    or_wb_ex           = 'orca wb smd ex',                  Software.orca,    Jobs.ex,          Methods.wb97xd,     Basis.augccpvdz,   Grids.g99_590,   TDDFT.tddft,    PCM.smd,   PCM.Eq.neq,     PCM.ExcitedModel.lr,   10,   True,   True,  False, False,   TDDFT.Triplets.off,   PCM.Formalism.cpcm,      PCM.Discretisation.default,     PCM.Radii.default,   1.2,    0.0,      PCM.Cavity.default,    0,        False
    qc_wb_ex           = 'qchem wb ex',                     Software.qchem,   Jobs.ex,          Methods.wb97xd,     Basis.augccpvdz,   Grids.g99_590,   TDDFT.tddft,    PCM.cpcm,  PCM.Eq.neq,     PCM.ExcitedModel.lr,   10,   True,   True,  False, False,   TDDFT.Triplets.off,   PCM.Formalism.iefpcm,    PCM.Discretisation.default,     PCM.Radii.default,   1.2,    0.0,      PCM.Cavity.default,    0,        False
    qc_wb_ss_ex        = 'qchem wb ss ex',                  Software.qchem,   Jobs.ex,          Methods.wb97xd,     Basis.augccpvdz,   Grids.g99_590,   TDDFT.tddft,    PCM.sspcm, PCM.Eq.neq,     PCM.ExcitedModel.clr,  10,   True,   True,  True,  False,   TDDFT.Triplets.off,   PCM.Formalism.iefpcm,    PCM.Discretisation.default,     PCM.Radii.default,   1.2,    0.0,      PCM.Cavity.default,    0,        False
    qc_cb_ss_ex        = 'qchem cb ss ex',                  Software.qchem,   Jobs.ex,          Methods.cb3lyp,     Basis.augccpvdz,   Grids.g99_590,   TDDFT.tddft,    PCM.sspcm, PCM.Eq.neq,     PCM.ExcitedModel.clr,  10,   True,   True,  True,  False,   TDDFT.Triplets.off,   PCM.Formalism.iefpcm,    PCM.Discretisation.default,     PCM.Radii.default,   1.2,    0.0,      PCM.Cavity.default,    0,        False

    # emission
    # qc_wb_em           = 'qchem wb em',                     Software.qchem,   Jobs.em,          Methods.wb97xd,     Basis.augccpvdz,   Grids.g99_590,   TDDFT.tddft,    PCM.cpcm,  PCM.Eq.eq_neq,  PCM.ExcitedModel.lr,    4,   False,  True,  False, False,   TDDFT.Triplets.off,   PCM.Formalism.iefpcm,    PCM.Discretisation.default,     PCM.Radii.default,   1.2,    0.0,      PCM.Cavity.default,    0,        False
    qc_wb_ss_em        = 'qchem wb ss em',                  Software.qchem,   Jobs.em,          Methods.wb97xd,     Basis.augccpvdz,   Grids.g99_590,   TDDFT.tddft,    PCM.sspcm,  PCM.Eq.eq_neq, PCM.ExcitedModel.clr,   4,   False,  True,  True,  False,   TDDFT.Triplets.off,   PCM.Formalism.iefpcm,    PCM.Discretisation.default,     PCM.Radii.default,   1.2,    0.0,      PCM.Cavity.default,    0,        False
    qc_cb_ss_em        = 'qchem cb ss em',                  Software.qchem,   Jobs.em,          Methods.cb3lyp,     Basis.augccpvdz,   Grids.g99_590,   TDDFT.tddft,    PCM.sspcm,  PCM.Eq.eq_neq, PCM.ExcitedModel.clr,   4,   False,  True,  True,  False,   TDDFT.Triplets.off,   PCM.Formalism.iefpcm,    PCM.Discretisation.default,     PCM.Radii.default,   1.2,    0.0,      PCM.Cavity.default,    0,        False

    # esd
    or_wb_esd          = 'orca wb esd',                     Software.orca,    Jobs.esd,         Methods.wb97xd,     Basis.augccpvdz,   Grids.g99_590,   TDDFT.tddft,    PCM.smd,   PCM.Eq.eq,      PCM.ExcitedModel.lr,    2,   True,   True,  True,  False,   TDDFT.Triplets.off,   PCM.Formalism.none,      PCM.Discretisation.default,     PCM.Radii.default,   1.2,    0.0,      PCM.Cavity.default,    0,        False
    or_cb_esd          = 'orca cb esd',                     Software.orca,    Jobs.esd,         Methods.cb3lyp,     Basis.augccpvdz,   Grids.g99_590,   TDDFT.tddft,    PCM.smd,   PCM.Eq.eq,      PCM.ExcitedModel.lr,    2,   True,   True,  True,  False,   TDDFT.Triplets.off,   PCM.Formalism.none,      PCM.Discretisation.default,     PCM.Radii.default,   1.2,    0.0,      PCM.Cavity.default,    0,        False
    or_casscf_esd      = 'orca casscf esd',                 Software.orca,    Jobs.esd,         Methods.casscf,     Basis.augccpvdz,   Grids.none,      TDDFT.none,     PCM.none,  PCM.Eq.none,    PCM.ExcitedModel.none,  2,   True,   True,  True,  False,   TDDFT.Triplets.off,   PCM.Formalism.none,      PCM.Discretisation.default,     PCM.Radii.default,   1.2,    0.0,      PCM.Cavity.default,    0,        False

    # single point
    casscf             = 'casscf_single_point',             Software.orca,    Jobs.casscf,      Methods.casscf,     Basis.augccpvdz,   Grids.none,      TDDFT.none,     PCM.none,  PCM.Eq.none,    PCM.ExcitedModel.none,  4,   True,   True,  True,  True,    TDDFT.Triplets.off,   PCM.Formalism.none,      PCM.Discretisation.default,     PCM.Radii.default,   1.2,    0.0,      PCM.Cavity.default,    4,        False
    casscf_sa          = 'casscf_single_point_sa',          Software.orca,    Jobs.casscf,      Methods.casscf,     Basis.augccpvdz,   Grids.none,      TDDFT.none,     PCM.none,  PCM.Eq.none,    PCM.ExcitedModel.none,  4,   True,   True,  True,  True,    TDDFT.Triplets.off,   PCM.Formalism.none,      PCM.Discretisation.default,     PCM.Radii.default,   1.2,    0.0,      PCM.Cavity.default,    4,        True
    caspt2             = 'caspt2_single_point',             Software.orca,    Jobs.caspt2,      Methods.caspt2,     Basis.augccpvdz,   Grids.none,      TDDFT.none,     PCM.none,  PCM.Eq.none,    PCM.ExcitedModel.none,  4,   True,   True,  True,  True,    TDDFT.Triplets.off,   PCM.Formalism.none,      PCM.Discretisation.default,     PCM.Radii.default,   1.2,    0.0,      PCM.Cavity.default,    4,        True
    nevpt2             = 'nevpt2_single_point',             Software.orca,    Jobs.nevpt2,      Methods.nevpt2,     Basis.augccpvdz,   Grids.none,      TDDFT.none,     PCM.none,  PCM.Eq.none,    PCM.ExcitedModel.none,  4,   True,   True,  True,  True,    TDDFT.Triplets.off,   PCM.Formalism.none,      PCM.Discretisation.default,     PCM.Radii.default,   1.2,    0.0,      PCM.Cavity.default,    4,        True
    or_wb_sp_es        = 'orca wb es sp',                   Software.orca,    Jobs.sp,          Methods.wb97xd,     Basis.augccpvdz,   Grids.g99_590,   TDDFT.tddft,    PCM.smd,   PCM.Eq.eq,      PCM.ExcitedModel.lr,    4,   False,  True,  True,  True,    TDDFT.Triplets.off,   PCM.Formalism.none,      PCM.Discretisation.default,     PCM.Radii.default,   1.2,    0.0,      PCM.Cavity.default,    0,        False

    # Polarisability                                                                                    basis justification; 10.1021/jp502475e
    polarisability     = 'orca gas pol',                    Software.orca,    Jobs.pol,         Methods.wb97xd,     Basis.augccpvtz,   Grids.g99_590,   TDDFT.tddft,    PCM.none,  PCM.Eq.none,    PCM.ExcitedModel.none,  4,   True,   True,  True,  True,    TDDFT.Triplets.off,   PCM.Formalism.none,      PCM.Discretisation.default,     PCM.Radii.default,   1.2,    0.0,      PCM.Cavity.default,    0,        False