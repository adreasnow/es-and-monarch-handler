from .newenum import *
from dataclasses import dataclass

class spectraType(NewEnum):
    emission = auto()
    absorbance = auto()
    excitation = auto()
    ftir = auto()
    qy = auto()
    lifetime = auto()

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
    params: deconvParams | None
    residual: float | None
    x: list[float]
    y: list[float]
    peaks: list[gaussian] | None

    @property
    def peaks_sorted_forward(self) -> list[gaussian]:
        centerList = [gauss.center for gauss in self.peaks]
        sortList = sorted(centerList)
        outGaussList = []
        for center in sortList:
            for gauss in self.peaks:
                if gauss.center == center:
                    outGaussList += [gauss]
        return outGaussList

    @property
    def peaks_sorted_reverse(self) -> list[gaussian]:
        return reversed(self.peaks_sorted_forward)

@dataclass
class _simpleSpectrum():
    maxy: float
    integrand: float
    x: list[float]
    y: list[float]

@dataclass
class spectrumSeries():
    spectrum: spectraType
    absorbanceSpectra: list[_simpleSpectrum]
    emissionSpectra: list[_simpleSpectrum]
    excitation: int
    qy: float | None 

@dataclass
class decay():
    I0: float
    t: float
    v: float
    h: float

@dataclass
class Lifetime():
    spectrum: spectraType
    irf: list[float]
    trf: list[float]
    time: list[float]
    binWidth: int
    irf_fit: decay
    t: list[decay]