import numpy as np
from scipy.special import voigt_profile
from .gaussian0 import gaussian0_func
from .lorentzian0 import lorentzian0_func

def voigt0_func(x, amp1, cen1, sigma1):
    fraction = 0.5
    np.log2(2)
    sigma1_g = sigma1 / np.sqrt(2 * np.log2(2))
    gauss_component = np.multiply(1 - fraction, gaussian0_func(x, amp1, cen1, sigma1_g))
    lorentz_compenent = np.multiply(fraction, lorentzian0_func(x, amp1, cen1, sigma1))
    return np.add(gauss_component, lorentz_compenent)


def voigt0_2(x, amp1, cen1, sigma1,
               amp2, cen2, sigma2):
    vList = np.array(voigt0_func(x, amp1, cen1, sigma1))
    vList = np.add(vList, voigt0_func(x, amp2, cen2, sigma2))
    return vList


def voigt0_3(x, amp1, cen1, sigma1,
               amp2, cen2, sigma2,
               amp3, cen3, sigma3):

    vList = np.array(voigt0_func(x, amp1, cen1, sigma1))
    vList = np.add(vList, voigt0_func(x, amp2, cen2, sigma2))
    vList = np.add(vList, voigt0_func(x, amp3, cen3, sigma3))
    return vList


def voigt0_4(x, amp1, cen1, sigma1,
               amp2, cen2, sigma2,
               amp3, cen3, sigma3,
               amp4, cen4, sigma4):

    vList = np.array(voigt0_func(x, amp1, cen1, sigma1))
    vList = np.add(vList, voigt0_func(x, amp2, cen2, sigma2))
    vList = np.add(vList, voigt0_func(x, amp3, cen3, sigma3))
    vList = np.add(vList, voigt0_func(x, amp4, cen4, sigma4))
    return vList


def voigt0_5(x, amp1, cen1, sigma1,
               amp2, cen2, sigma2,
               amp3, cen3, sigma3,
               amp4, cen4, sigma4,
               amp5, cen5, sigma5):

    vList = np.array(voigt0_func(x, amp1, cen1, sigma1))
    vList = np.add(vList, voigt0_func(x, amp2, cen2, sigma2))
    vList = np.add(vList, voigt0_func(x, amp3, cen3, sigma3))
    vList = np.add(vList, voigt0_func(x, amp4, cen4, sigma4))
    vList = np.add(vList, voigt0_func(x, amp5, cen5, sigma5))
    return vList


def voigt0_6(x, amp1, cen1, sigma1,
               amp2, cen2, sigma2,
               amp3, cen3, sigma3,
               amp4, cen4, sigma4,
               amp5, cen5, sigma5,
               amp6, cen6, sigma6):

    vList = np.array(voigt0_func(x, amp1, cen1, sigma1))
    vList = np.add(vList, voigt0_func(x, amp2, cen2, sigma2))
    vList = np.add(vList, voigt0_func(x, amp3, cen3, sigma3))
    vList = np.add(vList, voigt0_func(x, amp4, cen4, sigma4))
    vList = np.add(vList, voigt0_func(x, amp5, cen5, sigma5))
    vList = np.add(vList, voigt0_func(x, amp6, cen6, sigma6))
    return vList


def voigt0_7(x, amp1, cen1, sigma1,
               amp2, cen2, sigma2,
               amp3, cen3, sigma3,
               amp4, cen4, sigma4,
               amp5, cen5, sigma5,
               amp6, cen6, sigma6,
               amp7, cen7, sigma7):

    vList = np.array(voigt0_func(x, amp1, cen1, sigma1))
    vList = np.add(vList, voigt0_func(x, amp2, cen2, sigma2))
    vList = np.add(vList, voigt0_func(x, amp3, cen3, sigma3))
    vList = np.add(vList, voigt0_func(x, amp4, cen4, sigma4))
    vList = np.add(vList, voigt0_func(x, amp5, cen5, sigma5))
    vList = np.add(vList, voigt0_func(x, amp6, cen6, sigma6))
    vList = np.add(vList, voigt0_func(x, amp7, cen7, sigma7))
    return vList


def voigt0_8(x, amp1, cen1, sigma1,
               amp2, cen2, sigma2,
               amp3, cen3, sigma3,
               amp4, cen4, sigma4,
               amp5, cen5, sigma5,
               amp6, cen6, sigma6,
               amp7, cen7, sigma7,
               amp8, cen8, sigma8):

    vList = np.array(voigt0_func(x, amp1, cen1, sigma1))
    vList = np.add(vList, voigt0_func(x, amp2, cen2, sigma2))
    vList = np.add(vList, voigt0_func(x, amp3, cen3, sigma3))
    vList = np.add(vList, voigt0_func(x, amp4, cen4, sigma4))
    vList = np.add(vList, voigt0_func(x, amp5, cen5, sigma5))
    vList = np.add(vList, voigt0_func(x, amp6, cen6, sigma6))
    vList = np.add(vList, voigt0_func(x, amp7, cen7, sigma7))
    vList = np.add(vList, voigt0_func(x, amp8, cen8, sigma8))
    return vList


def voigt0_9(x, amp1, cen1, sigma1,
               amp2, cen2, sigma2,
               amp3, cen3, sigma3,
               amp4, cen4, sigma4,
               amp5, cen5, sigma5,
               amp6, cen6, sigma6,
               amp7, cen7, sigma7,
               amp8, cen8, sigma8,
               amp9, cen9, sigma9):

    vList = np.array(voigt0_func(x, amp1, cen1, sigma1))
    vList = np.add(vList, voigt0_func(x, amp2, cen2, sigma2))
    vList = np.add(vList, voigt0_func(x, amp3, cen3, sigma3))
    vList = np.add(vList, voigt0_func(x, amp4, cen4, sigma4))
    vList = np.add(vList, voigt0_func(x, amp5, cen5, sigma5))
    vList = np.add(vList, voigt0_func(x, amp6, cen6, sigma6))
    vList = np.add(vList, voigt0_func(x, amp7, cen7, sigma7))
    vList = np.add(vList, voigt0_func(x, amp8, cen8, sigma8))
    vList = np.add(vList, voigt0_func(x, amp9, cen9, sigma9))
    return vList


def voigt0_10(x, amp1, cen1, sigma1,
                amp2, cen2, sigma2,
                amp3, cen3, sigma3,
                amp4, cen4, sigma4,
                amp5, cen5, sigma5,
                amp6, cen6, sigma6,
                amp7, cen7, sigma7,
                amp8, cen8, sigma8,
                amp9, cen9, sigma9,
                amp10, cen10, sigma10):

    vList = np.array(voigt0_func(x, amp1, cen1, sigma1))
    vList = np.add(vList, voigt0_func(x, amp2, cen2, sigma2))
    vList = np.add(vList, voigt0_func(x, amp3, cen3, sigma3))
    vList = np.add(vList, voigt0_func(x, amp4, cen4, sigma4))
    vList = np.add(vList, voigt0_func(x, amp5, cen5, sigma5))
    vList = np.add(vList, voigt0_func(x, amp6, cen6, sigma6))
    vList = np.add(vList, voigt0_func(x, amp7, cen7, sigma7))
    vList = np.add(vList, voigt0_func(x, amp8, cen8, sigma8))
    vList = np.add(vList, voigt0_func(x, amp9, cen9, sigma9))
    vList = np.add(vList, voigt0_func(x, amp10, cen10, sigma10))
    return vList


def voigt0_11(x, amp1, cen1, sigma1,
                amp2, cen2, sigma2,
                amp3, cen3, sigma3,
                amp4, cen4, sigma4,
                amp5, cen5, sigma5,
                amp6, cen6, sigma6,
                amp7, cen7, sigma7,
                amp8, cen8, sigma8,
                amp9, cen9, sigma9,
                amp10, cen10, sigma10,
                amp11, cen11, sigma11):

    vList = np.array(voigt0_func(x, amp1, cen1, sigma1))
    vList = np.add(vList, voigt0_func(x, amp2, cen2, sigma2))
    vList = np.add(vList, voigt0_func(x, amp3, cen3, sigma3))
    vList = np.add(vList, voigt0_func(x, amp4, cen4, sigma4))
    vList = np.add(vList, voigt0_func(x, amp5, cen5, sigma5))
    vList = np.add(vList, voigt0_func(x, amp6, cen6, sigma6))
    vList = np.add(vList, voigt0_func(x, amp7, cen7, sigma7))
    vList = np.add(vList, voigt0_func(x, amp8, cen8, sigma8))
    vList = np.add(vList, voigt0_func(x, amp9, cen9, sigma9))
    vList = np.add(vList, voigt0_func(x, amp10, cen10, sigma10))
    vList = np.add(vList, voigt0_func(x, amp11, cen11, sigma11))
    return vList


def voigt0_12(x, amp1, cen1, sigma1,
                amp2, cen2, sigma2,
                amp3, cen3, sigma3,
                amp4, cen4, sigma4,
                amp5, cen5, sigma5,
                amp6, cen6, sigma6,
                amp7, cen7, sigma7,
                amp8, cen8, sigma8,
                amp9, cen9, sigma9,
                amp10, cen10, sigma10,
                amp11, cen11, sigma11,
                amp12, cen12, sigma12):

    vList = np.array(voigt0_func(x, amp1, cen1, sigma1))
    vList = np.add(vList, voigt0_func(x, amp2, cen2, sigma2))
    vList = np.add(vList, voigt0_func(x, amp3, cen3, sigma3))
    vList = np.add(vList, voigt0_func(x, amp4, cen4, sigma4))
    vList = np.add(vList, voigt0_func(x, amp5, cen5, sigma5))
    vList = np.add(vList, voigt0_func(x, amp6, cen6, sigma6))
    vList = np.add(vList, voigt0_func(x, amp7, cen7, sigma7))
    vList = np.add(vList, voigt0_func(x, amp8, cen8, sigma8))
    vList = np.add(vList, voigt0_func(x, amp9, cen9, sigma9))
    vList = np.add(vList, voigt0_func(x, amp10, cen10, sigma10))
    vList = np.add(vList, voigt0_func(x, amp11, cen11, sigma11))
    vList = np.add(vList, voigt0_func(x, amp12, cen12, sigma12))
    return vList


def voigt0_13(x, amp1, cen1, sigma1,
                amp2, cen2, sigma2,
                amp3, cen3, sigma3,
                amp4, cen4, sigma4,
                amp5, cen5, sigma5,
                amp6, cen6, sigma6,
                amp7, cen7, sigma7,
                amp8, cen8, sigma8,
                amp9, cen9, sigma9,
                amp10, cen10, sigma10,
                amp11, cen11, sigma11,
                amp12, cen12, sigma12,
                amp13, cen13, sigma13):

    vList = np.array(voigt0_func(x, amp1, cen1, sigma1))
    vList = np.add(vList, voigt0_func(x, amp2, cen2, sigma2))
    vList = np.add(vList, voigt0_func(x, amp3, cen3, sigma3))
    vList = np.add(vList, voigt0_func(x, amp4, cen4, sigma4))
    vList = np.add(vList, voigt0_func(x, amp5, cen5, sigma5))
    vList = np.add(vList, voigt0_func(x, amp6, cen6, sigma6))
    vList = np.add(vList, voigt0_func(x, amp7, cen7, sigma7))
    vList = np.add(vList, voigt0_func(x, amp8, cen8, sigma8))
    vList = np.add(vList, voigt0_func(x, amp9, cen9, sigma9))
    vList = np.add(vList, voigt0_func(x, amp10, cen10, sigma10))
    vList = np.add(vList, voigt0_func(x, amp11, cen11, sigma11))
    vList = np.add(vList, voigt0_func(x, amp12, cen12, sigma12))
    vList = np.add(vList, voigt0_func(x, amp13, cen13, sigma13))
    return vList


def voigt0_14(x, amp1, cen1, sigma1,
                amp2, cen2, sigma2,
                amp3, cen3, sigma3,
                amp4, cen4, sigma4,
                amp5, cen5, sigma5,
                amp6, cen6, sigma6,
                amp7, cen7, sigma7,
                amp8, cen8, sigma8,
                amp9, cen9, sigma9,
                amp10, cen10, sigma10,
                amp11, cen11, sigma11,
                amp12, cen12, sigma12,
                amp13, cen13, sigma13,
                amp14, cen14, sigma14):

    vList = np.array(voigt0_func(x, amp1, cen1, sigma1))
    vList = np.add(vList, voigt0_func(x, amp2, cen2, sigma2))
    vList = np.add(vList, voigt0_func(x, amp3, cen3, sigma3))
    vList = np.add(vList, voigt0_func(x, amp4, cen4, sigma4))
    vList = np.add(vList, voigt0_func(x, amp5, cen5, sigma5))
    vList = np.add(vList, voigt0_func(x, amp6, cen6, sigma6))
    vList = np.add(vList, voigt0_func(x, amp7, cen7, sigma7))
    vList = np.add(vList, voigt0_func(x, amp8, cen8, sigma8))
    vList = np.add(vList, voigt0_func(x, amp9, cen9, sigma9))
    vList = np.add(vList, voigt0_func(x, amp10, cen10, sigma10))
    vList = np.add(vList, voigt0_func(x, amp11, cen11, sigma11))
    vList = np.add(vList, voigt0_func(x, amp12, cen12, sigma12))
    vList = np.add(vList, voigt0_func(x, amp13, cen13, sigma13))
    vList = np.add(vList, voigt0_func(x, amp14, cen14, sigma14))
    return vList


def voigt0_15(x, amp1, cen1, sigma1,
                amp2, cen2, sigma2,
                amp3, cen3, sigma3,
                amp4, cen4, sigma4,
                amp5, cen5, sigma5,
                amp6, cen6, sigma6,
                amp7, cen7, sigma7,
                amp8, cen8, sigma8,
                amp9, cen9, sigma9,
                amp10, cen10, sigma10,
                amp11, cen11, sigma11,
                amp12, cen12, sigma12,
                amp13, cen13, sigma13,
                amp14, cen14, sigma14,
                amp15, cen15, sigma15):

    vList = np.array(voigt0_func(x, amp1, cen1, sigma1))
    vList = np.add(vList, voigt0_func(x, amp2, cen2, sigma2))
    vList = np.add(vList, voigt0_func(x, amp3, cen3, sigma3))
    vList = np.add(vList, voigt0_func(x, amp4, cen4, sigma4))
    vList = np.add(vList, voigt0_func(x, amp5, cen5, sigma5))
    vList = np.add(vList, voigt0_func(x, amp6, cen6, sigma6))
    vList = np.add(vList, voigt0_func(x, amp7, cen7, sigma7))
    vList = np.add(vList, voigt0_func(x, amp8, cen8, sigma8))
    vList = np.add(vList, voigt0_func(x, amp9, cen9, sigma9))
    vList = np.add(vList, voigt0_func(x, amp10, cen10, sigma10))
    vList = np.add(vList, voigt0_func(x, amp11, cen11, sigma11))
    vList = np.add(vList, voigt0_func(x, amp12, cen12, sigma12))
    vList = np.add(vList, voigt0_func(x, amp13, cen13, sigma13))
    vList = np.add(vList, voigt0_func(x, amp14, cen14, sigma14))
    vList = np.add(vList, voigt0_func(x, amp15, cen15, sigma15))
    return vList


def voigt0_16(x, amp1, cen1, sigma1,
                amp2, cen2, sigma2,
                amp3, cen3, sigma3,
                amp4, cen4, sigma4,
                amp5, cen5, sigma5,
                amp6, cen6, sigma6,
                amp7, cen7, sigma7,
                amp8, cen8, sigma8,
                amp9, cen9, sigma9,
                amp10, cen10, sigma10,
                amp11, cen11, sigma11,
                amp12, cen12, sigma12,
                amp13, cen13, sigma13,
                amp14, cen14, sigma14,
                amp15, cen15, sigma15,
                amp16, cen16, sigma16):

    vList = np.array(voigt0_func(x, amp1, cen1, sigma1))
    vList = np.add(vList, voigt0_func(x, amp2, cen2, sigma2))
    vList = np.add(vList, voigt0_func(x, amp3, cen3, sigma3))
    vList = np.add(vList, voigt0_func(x, amp4, cen4, sigma4))
    vList = np.add(vList, voigt0_func(x, amp5, cen5, sigma5))
    vList = np.add(vList, voigt0_func(x, amp6, cen6, sigma6))
    vList = np.add(vList, voigt0_func(x, amp7, cen7, sigma7))
    vList = np.add(vList, voigt0_func(x, amp8, cen8, sigma8))
    vList = np.add(vList, voigt0_func(x, amp9, cen9, sigma9))
    vList = np.add(vList, voigt0_func(x, amp10, cen10, sigma10))
    vList = np.add(vList, voigt0_func(x, amp11, cen11, sigma11))
    vList = np.add(vList, voigt0_func(x, amp12, cen12, sigma12))
    vList = np.add(vList, voigt0_func(x, amp13, cen13, sigma13))
    vList = np.add(vList, voigt0_func(x, amp14, cen14, sigma14))
    vList = np.add(vList, voigt0_func(x, amp15, cen15, sigma15))
    vList = np.add(vList, voigt0_func(x, amp16, cen16, sigma16))
    return vList


def voigt0_17(x, amp1, cen1, sigma1,
                amp2, cen2, sigma2,
                amp3, cen3, sigma3,
                amp4, cen4, sigma4,
                amp5, cen5, sigma5,
                amp6, cen6, sigma6,
                amp7, cen7, sigma7,
                amp8, cen8, sigma8,
                amp9, cen9, sigma9,
                amp10, cen10, sigma10,
                amp11, cen11, sigma11,
                amp12, cen12, sigma12,
                amp13, cen13, sigma13,
                amp14, cen14, sigma14,
                amp15, cen15, sigma15,
                amp16, cen16, sigma16,
                amp17, cen17, sigma17):

    vList = np.array(voigt0_func(x, amp1, cen1, sigma1))
    vList = np.add(vList, voigt0_func(x, amp2, cen2, sigma2))
    vList = np.add(vList, voigt0_func(x, amp3, cen3, sigma3))
    vList = np.add(vList, voigt0_func(x, amp4, cen4, sigma4))
    vList = np.add(vList, voigt0_func(x, amp5, cen5, sigma5))
    vList = np.add(vList, voigt0_func(x, amp6, cen6, sigma6))
    vList = np.add(vList, voigt0_func(x, amp7, cen7, sigma7))
    vList = np.add(vList, voigt0_func(x, amp8, cen8, sigma8))
    vList = np.add(vList, voigt0_func(x, amp9, cen9, sigma9))
    vList = np.add(vList, voigt0_func(x, amp10, cen10, sigma10))
    vList = np.add(vList, voigt0_func(x, amp11, cen11, sigma11))
    vList = np.add(vList, voigt0_func(x, amp12, cen12, sigma12))
    vList = np.add(vList, voigt0_func(x, amp13, cen13, sigma13))
    vList = np.add(vList, voigt0_func(x, amp14, cen14, sigma14))
    vList = np.add(vList, voigt0_func(x, amp15, cen15, sigma15))
    vList = np.add(vList, voigt0_func(x, amp16, cen16, sigma16))
    vList = np.add(vList, voigt0_func(x, amp17, cen17, sigma17))
    return vList


def voigt0_18(x, amp1, cen1, sigma1,
                amp2, cen2, sigma2,
                amp3, cen3, sigma3,
                amp4, cen4, sigma4,
                amp5, cen5, sigma5,
                amp6, cen6, sigma6,
                amp7, cen7, sigma7,
                amp8, cen8, sigma8,
                amp9, cen9, sigma9,
                amp10, cen10, sigma10,
                amp11, cen11, sigma11,
                amp12, cen12, sigma12,
                amp13, cen13, sigma13,
                amp14, cen14, sigma14,
                amp15, cen15, sigma15,
                amp16, cen16, sigma16,
                amp17, cen17, sigma17,
                amp18, cen18, sigma18):

    vList = np.array(voigt0_func(x, amp1, cen1, sigma1))
    vList = np.add(vList, voigt0_func(x, amp2, cen2, sigma2))
    vList = np.add(vList, voigt0_func(x, amp3, cen3, sigma3))
    vList = np.add(vList, voigt0_func(x, amp4, cen4, sigma4))
    vList = np.add(vList, voigt0_func(x, amp5, cen5, sigma5))
    vList = np.add(vList, voigt0_func(x, amp6, cen6, sigma6))
    vList = np.add(vList, voigt0_func(x, amp7, cen7, sigma7))
    vList = np.add(vList, voigt0_func(x, amp8, cen8, sigma8))
    vList = np.add(vList, voigt0_func(x, amp9, cen9, sigma9))
    vList = np.add(vList, voigt0_func(x, amp10, cen10, sigma10))
    vList = np.add(vList, voigt0_func(x, amp11, cen11, sigma11))
    vList = np.add(vList, voigt0_func(x, amp12, cen12, sigma12))
    vList = np.add(vList, voigt0_func(x, amp13, cen13, sigma13))
    vList = np.add(vList, voigt0_func(x, amp14, cen14, sigma14))
    vList = np.add(vList, voigt0_func(x, amp15, cen15, sigma15))
    vList = np.add(vList, voigt0_func(x, amp16, cen16, sigma16))
    vList = np.add(vList, voigt0_func(x, amp17, cen17, sigma17))
    vList = np.add(vList, voigt0_func(x, amp18, cen18, sigma18))
    return vList


def voigt0_19(x, amp1, cen1, sigma1,
                amp2, cen2, sigma2,
                amp3, cen3, sigma3,
                amp4, cen4, sigma4,
                amp5, cen5, sigma5,
                amp6, cen6, sigma6,
                amp7, cen7, sigma7,
                amp8, cen8, sigma8,
                amp9, cen9, sigma9,
                amp10, cen10, sigma10,
                amp11, cen11, sigma11,
                amp12, cen12, sigma12,
                amp13, cen13, sigma13,
                amp14, cen14, sigma14,
                amp15, cen15, sigma15,
                amp16, cen16, sigma16,
                amp17, cen17, sigma17,
                amp18, cen18, sigma18,
                amp19, cen19, sigma19):

    vList = np.array(voigt0_func(x, amp1, cen1, sigma1))
    vList = np.add(vList, voigt0_func(x, amp2, cen2, sigma2))
    vList = np.add(vList, voigt0_func(x, amp3, cen3, sigma3))
    vList = np.add(vList, voigt0_func(x, amp4, cen4, sigma4))
    vList = np.add(vList, voigt0_func(x, amp5, cen5, sigma5))
    vList = np.add(vList, voigt0_func(x, amp6, cen6, sigma6))
    vList = np.add(vList, voigt0_func(x, amp7, cen7, sigma7))
    vList = np.add(vList, voigt0_func(x, amp8, cen8, sigma8))
    vList = np.add(vList, voigt0_func(x, amp9, cen9, sigma9))
    vList = np.add(vList, voigt0_func(x, amp10, cen10, sigma10))
    vList = np.add(vList, voigt0_func(x, amp11, cen11, sigma11))
    vList = np.add(vList, voigt0_func(x, amp12, cen12, sigma12))
    vList = np.add(vList, voigt0_func(x, amp13, cen13, sigma13))
    vList = np.add(vList, voigt0_func(x, amp14, cen14, sigma14))
    vList = np.add(vList, voigt0_func(x, amp15, cen15, sigma15))
    vList = np.add(vList, voigt0_func(x, amp16, cen16, sigma16))
    vList = np.add(vList, voigt0_func(x, amp17, cen17, sigma17))
    vList = np.add(vList, voigt0_func(x, amp18, cen18, sigma18))
    vList = np.add(vList, voigt0_func(x, amp19, cen19, sigma19))
    return vList


def voigt0_20(x, amp1, cen1, sigma1,
                amp2, cen2, sigma2,
                amp3, cen3, sigma3,
                amp4, cen4, sigma4,
                amp5, cen5, sigma5,
                amp6, cen6, sigma6,
                amp7, cen7, sigma7,
                amp8, cen8, sigma8,
                amp9, cen9, sigma9,
                amp10, cen10, sigma10,
                amp11, cen11, sigma11,
                amp12, cen12, sigma12,
                amp13, cen13, sigma13,
                amp14, cen14, sigma14,
                amp15, cen15, sigma15,
                amp16, cen16, sigma16,
                amp17, cen17, sigma17,
                amp18, cen18, sigma18,
                amp19, cen19, sigma19,
                amp20, cen20, sigma20):

    vList = np.array(voigt0_func(x, amp1, cen1, sigma1))
    vList = np.add(vList, voigt0_func(x, amp2, cen2, sigma2))
    vList = np.add(vList, voigt0_func(x, amp3, cen3, sigma3))
    vList = np.add(vList, voigt0_func(x, amp4, cen4, sigma4))
    vList = np.add(vList, voigt0_func(x, amp5, cen5, sigma5))
    vList = np.add(vList, voigt0_func(x, amp6, cen6, sigma6))
    vList = np.add(vList, voigt0_func(x, amp7, cen7, sigma7))
    vList = np.add(vList, voigt0_func(x, amp8, cen8, sigma8))
    vList = np.add(vList, voigt0_func(x, amp9, cen9, sigma9))
    vList = np.add(vList, voigt0_func(x, amp10, cen10, sigma10))
    vList = np.add(vList, voigt0_func(x, amp11, cen11, sigma11))
    vList = np.add(vList, voigt0_func(x, amp12, cen12, sigma12))
    vList = np.add(vList, voigt0_func(x, amp13, cen13, sigma13))
    vList = np.add(vList, voigt0_func(x, amp14, cen14, sigma14))
    vList = np.add(vList, voigt0_func(x, amp15, cen15, sigma15))
    vList = np.add(vList, voigt0_func(x, amp16, cen16, sigma16))
    vList = np.add(vList, voigt0_func(x, amp17, cen17, sigma17))
    vList = np.add(vList, voigt0_func(x, amp18, cen18, sigma18))
    vList = np.add(vList, voigt0_func(x, amp19, cen19, sigma19))
    vList = np.add(vList, voigt0_func(x, amp20, cen20, sigma20))

voigt0FuncList = [voigt0_func, voigt0_func, voigt0_2,  voigt0_3,  voigt0_4,  voigt0_5,  voigt0_6,  voigt0_7,
                  voigt0_8,    voigt0_9,    voigt0_10, voigt0_11, voigt0_12, voigt0_13, voigt0_14, voigt0_15,
                  voigt0_16,   voigt0_17,   voigt0_18, voigt0_19, voigt0_20]
