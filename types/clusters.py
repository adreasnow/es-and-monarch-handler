import os
import tomli
from .newenum import NewEnum
from aenum import StrEnum
from dataclasses import dataclass


class clusters(StrEnum):
    m3      = 'M3'
    monarch = 'MonARCH'
    gadi    = 'Gadi'

@dataclass
class _cluster():
    hostName: str
    host: str
    user: str
    python: str
    slurmCheckFreq: int
    timedOutCheckFreq: int
    account: str
    projectPath: str
    squeue: str
    sbatch: str
    toslm: str
    scratch: str = None
    project: str = None
    cluster: clusters = None

    def __post_init__(self):
        self.scratch  = f'/home/{self.user}/scratch'
        self.project  = f'{self.projectPath}/{self.account}'
        self.homePath = f'{self.project}/{self.user}'

@dataclass
class _Clusters():
    monarch: _cluster
    m3: _cluster
    gadi: _cluster

    def __post_init__(self):
        self.monarch = _cluster(**self.monarch)
        self.m3 = _cluster(**self.m3)
        self.gadi = _cluster(**self.gadi)

def loadRemotes(cluster: clusters = None) -> dict:
    root_dir = os.path.dirname(os.path.abspath(__file__))
    with open(f'{root_dir}/../remotes.toml', 'rb') as f:
        config = tomli.load(f)
        clusterChoices = _Clusters(**config)
    if cluster == None:
        return clusterChoices
    elif cluster == clusters.monarch:
        choice = clusterChoices.monarch
    elif cluster == clusters.m3:
        choice = clusterChoices.m3
    elif cluster == clusters.gadi:
        choice = clusterChoices.gadi
    choice.cluster = cluster
    return choice
