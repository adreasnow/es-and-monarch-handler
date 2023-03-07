import numpy as np
import tomli
import os
from .types.solvents import Solvents
from .types.fluorophores import Fluorophores
from .types.methods import Methods
from openbabel.pybel import readstring as pbreadstring
from dataclasses import dataclass


@dataclass
class _local():
    dbLocationMac: str
    dbLocationWin: str
    dataFolderMac: str
    dataFolderWin: str
    MonARCHFolderMac: str
    MonARCHFolderWin: str


@dataclass
class _monarch():
    host: str
    user: str
    python: str
    slurmCheckFreq: int
    timedOutCheckFreq: int
    squeue: str
    sbatch: str
    toslm: str

@dataclass
class _ifttt():
    jobid: str
    jobkey: str

@dataclass
class Config():
    local: _local
    monarch: _monarch
    ifttt: _ifttt

    def __post_init__(self):
        self.local = _local(**self.local)
        self.monarch = _monarch(**self.monarch)
        self.ifttt = _ifttt(**self.ifttt)

def loadConfig() -> dict:
    root_dir = os.path.dirname(os.path.abspath(__file__))
    with open(f'{root_dir}/config.toml', 'rb') as f:
        config = tomli.load(f)
    return Config(**config)

def evToNm(eV: float | list[float], error: float = 0.0) -> float | tuple[float, float, float]:
    '''Converts eV values to nm'''
    def ev2nm(eV):
        h = 4.135667e-15
        c = 2.99792e8
        return np.divide(np.multiply(h, c), np.multiply(eV, 1e-9))

    if type(eV) == float:
        nm = ev2nm([eV, eV + error, eV - error])
        if error == 0:
            return nm[0]
        elif error != 0:
            return (nm[0], nm[1], nm[2])

    else:
        nm = ev2nm(eV)
        return nm


def nmToEv(nm, error: float = 0.0):
    '''Converts eV values to nm. Is just a wrapper for evToNm, since the maths is the same'''
    return evToNm(nm, error)


def stripIllegal(string: str) -> str:
    '''Removes characters that might mess with unix dirs'''
    chars = '(),'
    for char in chars:
        string = string.replace(char, '')
    return string


def smiles2xyz(smiles: str) -> str:
    '''Converts a SMILES string input to an XYZ string output using pybel'''
    mol = pbreadstring('smi', smiles)
    mol.make3D()
    return mol.write('xyz')


def rmsd(expectation: float, predictedlist: list[float]) -> float:
    '''Calculates the RMSD of a list of floats, given an expectation value'''
    rmsd = np.sqrt(np.divide(np.sum(np.square(np.subtract(predictedlist, expectation))), np.shape(predictedlist)[0]))
    return rmsd


def fluorophores_solvents_methods() -> tuple[list[Fluorophores], list[Solvents], list[Methods]]:
    fluorophores = [fluorophore for fluorophore in Fluorophores if bool(fluorophore)]
    solvents = [solvent for solvent in Solvents if bool(solvent)]
    methods = [method for method in Methods if bool(method)]
    return fluorophores, solvents, methods


def script_builder(filePath: str, strName: str) -> str:
    with open(filePath, 'r') as f:
        lines = f.readlines()
    outStr = f'{strName} = \'\'\n'
    for line in lines:
        line = line.replace('\n', '\\n')
        line = line.replace('\t', '\\t')
        line = line.replace('\'', '\"')
        outStr += f'{strName} += f\'{line}\'\n'
    outStr += f'\nreturn {strName}\n'
    return outStr


class dsLoad(object):
    import pandas as pd

    def __init__(self, ds: str = 'fluorophores-ds', df: str = 'dataset') -> None:
        config = loadConfig()
        if os.name == 'nt':
            self.main_path = config.local.dbLocationWin
        else:
            self.main_path = config.local.dbLocationMac
        self.db = f'{self.main_path}/{df}'
        return

    def __enter__(self) -> pd.DataFrame:
        self.df = self.pd.read_pickle(self.db)
        return self.df

    def __exit__(self, a, b, c) -> None:
        self.df.to_pickle(self.db)
        return


class statusLoad(object):
    import pandas as pd

    def __init__(self, df: str = 'progress') -> None:
        config = loadConfig()
        if os.name == 'nt':
            self.main_path = config.local.dbLocationWin
        else:
            self.main_path = config.local.dbLocationMac
        self.db = f'{self.main_path}/{df}'
        return

    def __enter__(self) -> pd.DataFrame:
        self.df = self.pd.read_pickle(self.db)
        return self.df

    def __exit__(self, a, b, c) -> None:
        self.df.to_pickle(self.db)
        return
