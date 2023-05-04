from .newenum import NewEnum
from dataclasses import dataclass
from typing import Optional


class spectraType(NewEnum):
    emission   = 'em'
    absorbance = 'abs'
    excitation = 'ex'
    # ftir       = 'ftir'
    # qy         = 'qr'
    lifetime   = 'tr'
    esdex      = 'esd_abs'
    esdem      = 'esd_em'

@dataclass
class gaussian():
    center: float
    width: float
    amplitude: float


@dataclass
class deconvParams():
    amplitudes: tuple[float, float]
    sigma: tuple[int, int]
    convergence: float
    gaussianRange: tuple[int, int]
    maxiter: int

@dataclass
class _simpleSpectrum():
    x: list[float]
    y: list[float]
    exLambda: int = None
    emLambda: int = None

@dataclass
class spectrum():
    spectraType: spectraType
    spectrum: _simpleSpectrum
    deconvoluted: bool
    derivLevel: int = 0
    params: deconvParams | None = None
    residual: float | None = None
    peaks: list[gaussian] | None = None
    smoothing: int = None
    smoothing_deriv: int = None
    residual_deriv: Optional[float | None] = None
    peaks_deriv: Optional[list[gaussian] | None] = None
    solventSpectrum: _simpleSpectrum = None

    def _peaks_sorted(self, direction, level) -> list[gaussian]:
        if level == 'deriv':
            peaks = self.peaks_deriv
        else:
            peaks = self.peaks

        centerList = [gauss.center for gauss in peaks]
        sortList = sorted(centerList)
        outGaussList = []
        for center in sortList:
            for gauss in peaks:
                if gauss.center == center:
                    outGaussList += [gauss]
        if direction == 'forward':
            return outGaussList
        else:
            return reversed(outGaussList)

    @property
    def peaks_sorted(self) -> list[gaussian]:
        if self.spectrum == spectraType.emission:
            return self._peaks_sorted('backward', 'zeroth')
        else:
            return self._peaks_sorted('forward', 'zeroth')

    @property
    def peaks_sorted_deriv(self) -> list[gaussian]:
        if self.spectrum == spectraType.emission:
            return self._peaks_sorted('backward', 'deriv')
        else:
            return self._peaks_sorted('forward', 'deriv')


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
class esdSpectrum():
    spectrum: spectraType
    x: list[float]
    yT: list[float]
    yFC: list[float]
    yHT: list[float]
    peaks: list[float]
    amps: list[float]


@dataclass
class irf():
    I0: float
    d: float
    b: float
    t: float


@dataclass
class trf():
    t: float
    c: float


@dataclass
class Lifetime():
    spectrum: spectraType
    irf: list[float]
    trf: list[float]
    time: list[float]
    binWidth: int
    irf_fit: irf
    trf_fit: list[trf]
    residual: float
    chi2: float
    I0: float
    d: float
    b: float
