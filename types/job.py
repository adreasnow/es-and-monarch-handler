from dataclasses import dataclass
from .solvents import Solvents
from .fluorophores import Fluorophores
from .states import States
from .basis import Basis
from .methods import Methods
from .software import Software
from .pcm import PCM
from .grids import Grids
from .jobs import Jobs, MetaJobs
from .orbs import Orbs

class _mem():
    def __int__(self):
        return self.total_gb

    def __init__(self, mem:int, cores:int):
        self.total_gb = mem
        self.total_mb = self.total_gb*1024
        self.per_core_gb = int(round(mem/cores))
        self.per_core_mb = self.per_core_gb*1024

@dataclass
class Job():
    software: Software
    fluorophore: Fluorophores
    solv: Solvents
    method: Methods
    basis: Basis
    pcm: PCM
    eq: PCM.Eq
    state: States
    job: Jobs

    # presets
    grid: Grids = Grids.g75_302
    procs: int = 16
    mem: int = 64
    time: int = 24
    partner: bool = True
    submit: bool = False
    submitFlags: str = '-NS'

    nroots: bool = 4
    rootpath: str = '/home/asnow/p2015120004/asnow'
    rootfolder: str = 'fluorophores-ds'

    # orca specific
    mopath:str=''
    xyzpath:str=''
    catxyzpath:str=''
    scfstring:str=''
    kdiis:bool=False
    soscf:bool=True
    notrah:bool=True

    # casscf specific settings
    casscf:tuple[int,int] = (4,4)
    casscfend:tuple[int,int] = (12,12)

    #orbs
    orbs:Orbs=Orbs.can

    pcm_es:PCM.ExcitedModel=PCM.ExcitedModel.none

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    @classmethod
    def from_MetaJob(cls, metajob:MetaJobs, fluorophore:Fluorophores, solvent:Solvents, state:States):
        x = cls(metajob.software, fluorophore, solvent, metajob.method, 
                metajob.basis, metajob.pcm, metajob.eq, state, metajob.job, grid=metajob.grid, nroots=metajob.nroots, pcm_es=metajob.excited)
        return x

    software: Software
    fluorophore: Fluorophores
    solv: Solvents
    method: Methods
    basis: Basis
    pcm: PCM
    eq: PCM.Eq
    state: States
    job: Jobs

    def __post_init__(self):
        if self.solv == Solvents.gas:
            self.pcm = PCM.none
            self.eq = PCM.Eq.none
        self.mem = _mem(self.mem, self.procs)
        self.name = f'{self.software.short}_{self.fluorophore.name}_{self.solv.name}_{self.method.name}_{self.basis.name}_{self.pcm.name}_{self.eq}_{self.state.name}_{self.job}'
        if self.software == Software.crest:
            self.path = f'{self.rootpath}/{self.rootfolder}/{self.fluorophore.name}/{self.solv.name}/crest'
            self.infile = f'{self.path}/{self.fluorophore.name}-crest{self.software.ext}'
            self.xyzfile = f'{self.path}/crest_best.xyz'
        else:
            if self.job in [Jobs.casscfOpt, Jobs.casscf]:
                norbs, nelec = self.casscf
                self.path = f'{self.rootpath}/{self.rootfolder}/{self.fluorophore.name}/{self.solv.name}/{self.state.name}/{self.job}-{norbs}-{nelec}'
                self.name = f'{self.name}-{norbs}-{nelec}'
            else:
                self.path = f'{self.rootpath}/{self.rootfolder}/{self.fluorophore.name}/{self.solv.name}/{self.state.name}/{self.job}'
            self.crestpath = f'{self.rootpath}/{self.rootfolder}/{self.fluorophore.name}/{self.solv.name}/crest'
            self.infile = f'{self.path}/{self.name}{self.software.ext}'
            self.xyzfile = f'{self.path}/{self.name}/{self.name}.xyz'
        self.outfile = f'{self.path}/{self.name}.out'


    




