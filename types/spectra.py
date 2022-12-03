from .newenum import *
from dataclasses import dataclass

class spectraType(NewEnum):
    emission = auto()
    absborbance = auto()
    excitation = auto()

@dataclass
class gaussian():
    center: float
    width: float
    amplitude: float

@dataclass
class deconvParams():
    amplitudes: tuple[float,float]
    sigma: tuple[int,int]
    convergence: float
    gaussianRange: tuple[int,int]
    maxiter: int

@dataclass
class spectrum():
    spectrum: spectraType
    params: deconvParams
    residual: float
    x: list[float]
    y: list[float]
    peaks: list[gaussian]
