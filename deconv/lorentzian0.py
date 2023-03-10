import numpy as np

def lorentzian0_func(x, amp1, cen1, sigma1):
    num = sigma1 / 2
    den = np.add(np.square(np.subtract(x, cen1)),(0.5 * sigma1)**2)
    return np.multiply((amp1 / np.pi), np.divide(num, den))


def lorentzian0_2(x, amp1, cen1, sigma1,
               amp2, cen2, sigma2):
    lList = np.array(lorentzian0_func(x, amp1, cen1, sigma1))
    lList = np.add(lList, lorentzian0_func(x, amp2, cen2, sigma2))
    return lList


def lorentzian0_3(x, amp1, cen1, sigma1,
               amp2, cen2, sigma2,
               amp3, cen3, sigma3):

    lList = np.array(lorentzian0_func(x, amp1, cen1, sigma1))
    lList = np.add(lList, lorentzian0_func(x, amp2, cen2, sigma2))
    lList = np.add(lList, lorentzian0_func(x, amp3, cen3, sigma3))
    return lList


def lorentzian0_4(x, amp1, cen1, sigma1,
               amp2, cen2, sigma2,
               amp3, cen3, sigma3,
               amp4, cen4, sigma4):

    lList = np.array(lorentzian0_func(x, amp1, cen1, sigma1))
    lList = np.add(lList, lorentzian0_func(x, amp2, cen2, sigma2))
    lList = np.add(lList, lorentzian0_func(x, amp3, cen3, sigma3))
    lList = np.add(lList, lorentzian0_func(x, amp4, cen4, sigma4))
    return lList


def lorentzian0_5(x, amp1, cen1, sigma1,
               amp2, cen2, sigma2,
               amp3, cen3, sigma3,
               amp4, cen4, sigma4,
               amp5, cen5, sigma5):

    lList = np.array(lorentzian0_func(x, amp1, cen1, sigma1))
    lList = np.add(lList, lorentzian0_func(x, amp2, cen2, sigma2))
    lList = np.add(lList, lorentzian0_func(x, amp3, cen3, sigma3))
    lList = np.add(lList, lorentzian0_func(x, amp4, cen4, sigma4))
    lList = np.add(lList, lorentzian0_func(x, amp5, cen5, sigma5))
    return lList


def lorentzian0_6(x, amp1, cen1, sigma1,
               amp2, cen2, sigma2,
               amp3, cen3, sigma3,
               amp4, cen4, sigma4,
               amp5, cen5, sigma5,
               amp6, cen6, sigma6):

    lList = np.array(lorentzian0_func(x, amp1, cen1, sigma1))
    lList = np.add(lList, lorentzian0_func(x, amp2, cen2, sigma2))
    lList = np.add(lList, lorentzian0_func(x, amp3, cen3, sigma3))
    lList = np.add(lList, lorentzian0_func(x, amp4, cen4, sigma4))
    lList = np.add(lList, lorentzian0_func(x, amp5, cen5, sigma5))
    lList = np.add(lList, lorentzian0_func(x, amp6, cen6, sigma6))
    return lList


def lorentzian0_7(x, amp1, cen1, sigma1,
               amp2, cen2, sigma2,
               amp3, cen3, sigma3,
               amp4, cen4, sigma4,
               amp5, cen5, sigma5,
               amp6, cen6, sigma6,
               amp7, cen7, sigma7):

    lList = np.array(lorentzian0_func(x, amp1, cen1, sigma1))
    lList = np.add(lList, lorentzian0_func(x, amp2, cen2, sigma2))
    lList = np.add(lList, lorentzian0_func(x, amp3, cen3, sigma3))
    lList = np.add(lList, lorentzian0_func(x, amp4, cen4, sigma4))
    lList = np.add(lList, lorentzian0_func(x, amp5, cen5, sigma5))
    lList = np.add(lList, lorentzian0_func(x, amp6, cen6, sigma6))
    lList = np.add(lList, lorentzian0_func(x, amp7, cen7, sigma7))
    return lList


def lorentzian0_8(x, amp1, cen1, sigma1,
               amp2, cen2, sigma2,
               amp3, cen3, sigma3,
               amp4, cen4, sigma4,
               amp5, cen5, sigma5,
               amp6, cen6, sigma6,
               amp7, cen7, sigma7,
               amp8, cen8, sigma8):

    lList = np.array(lorentzian0_func(x, amp1, cen1, sigma1))
    lList = np.add(lList, lorentzian0_func(x, amp2, cen2, sigma2))
    lList = np.add(lList, lorentzian0_func(x, amp3, cen3, sigma3))
    lList = np.add(lList, lorentzian0_func(x, amp4, cen4, sigma4))
    lList = np.add(lList, lorentzian0_func(x, amp5, cen5, sigma5))
    lList = np.add(lList, lorentzian0_func(x, amp6, cen6, sigma6))
    lList = np.add(lList, lorentzian0_func(x, amp7, cen7, sigma7))
    lList = np.add(lList, lorentzian0_func(x, amp8, cen8, sigma8))
    return lList


def lorentzian0_9(x, amp1, cen1, sigma1,
               amp2, cen2, sigma2,
               amp3, cen3, sigma3,
               amp4, cen4, sigma4,
               amp5, cen5, sigma5,
               amp6, cen6, sigma6,
               amp7, cen7, sigma7,
               amp8, cen8, sigma8,
               amp9, cen9, sigma9):

    lList = np.array(lorentzian0_func(x, amp1, cen1, sigma1))
    lList = np.add(lList, lorentzian0_func(x, amp2, cen2, sigma2))
    lList = np.add(lList, lorentzian0_func(x, amp3, cen3, sigma3))
    lList = np.add(lList, lorentzian0_func(x, amp4, cen4, sigma4))
    lList = np.add(lList, lorentzian0_func(x, amp5, cen5, sigma5))
    lList = np.add(lList, lorentzian0_func(x, amp6, cen6, sigma6))
    lList = np.add(lList, lorentzian0_func(x, amp7, cen7, sigma7))
    lList = np.add(lList, lorentzian0_func(x, amp8, cen8, sigma8))
    lList = np.add(lList, lorentzian0_func(x, amp9, cen9, sigma9))
    return lList


def lorentzian0_10(x, amp1, cen1, sigma1,
                amp2, cen2, sigma2,
                amp3, cen3, sigma3,
                amp4, cen4, sigma4,
                amp5, cen5, sigma5,
                amp6, cen6, sigma6,
                amp7, cen7, sigma7,
                amp8, cen8, sigma8,
                amp9, cen9, sigma9,
                amp10, cen10, sigma10):

    lList = np.array(lorentzian0_func(x, amp1, cen1, sigma1))
    lList = np.add(lList, lorentzian0_func(x, amp2, cen2, sigma2))
    lList = np.add(lList, lorentzian0_func(x, amp3, cen3, sigma3))
    lList = np.add(lList, lorentzian0_func(x, amp4, cen4, sigma4))
    lList = np.add(lList, lorentzian0_func(x, amp5, cen5, sigma5))
    lList = np.add(lList, lorentzian0_func(x, amp6, cen6, sigma6))
    lList = np.add(lList, lorentzian0_func(x, amp7, cen7, sigma7))
    lList = np.add(lList, lorentzian0_func(x, amp8, cen8, sigma8))
    lList = np.add(lList, lorentzian0_func(x, amp9, cen9, sigma9))
    lList = np.add(lList, lorentzian0_func(x, amp10, cen10, sigma10))
    return lList


def lorentzian0_11(x, amp1, cen1, sigma1,
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

    lList = np.array(lorentzian0_func(x, amp1, cen1, sigma1))
    lList = np.add(lList, lorentzian0_func(x, amp2, cen2, sigma2))
    lList = np.add(lList, lorentzian0_func(x, amp3, cen3, sigma3))
    lList = np.add(lList, lorentzian0_func(x, amp4, cen4, sigma4))
    lList = np.add(lList, lorentzian0_func(x, amp5, cen5, sigma5))
    lList = np.add(lList, lorentzian0_func(x, amp6, cen6, sigma6))
    lList = np.add(lList, lorentzian0_func(x, amp7, cen7, sigma7))
    lList = np.add(lList, lorentzian0_func(x, amp8, cen8, sigma8))
    lList = np.add(lList, lorentzian0_func(x, amp9, cen9, sigma9))
    lList = np.add(lList, lorentzian0_func(x, amp10, cen10, sigma10))
    lList = np.add(lList, lorentzian0_func(x, amp11, cen11, sigma11))
    return lList


def lorentzian0_12(x, amp1, cen1, sigma1,
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

    lList = np.array(lorentzian0_func(x, amp1, cen1, sigma1))
    lList = np.add(lList, lorentzian0_func(x, amp2, cen2, sigma2))
    lList = np.add(lList, lorentzian0_func(x, amp3, cen3, sigma3))
    lList = np.add(lList, lorentzian0_func(x, amp4, cen4, sigma4))
    lList = np.add(lList, lorentzian0_func(x, amp5, cen5, sigma5))
    lList = np.add(lList, lorentzian0_func(x, amp6, cen6, sigma6))
    lList = np.add(lList, lorentzian0_func(x, amp7, cen7, sigma7))
    lList = np.add(lList, lorentzian0_func(x, amp8, cen8, sigma8))
    lList = np.add(lList, lorentzian0_func(x, amp9, cen9, sigma9))
    lList = np.add(lList, lorentzian0_func(x, amp10, cen10, sigma10))
    lList = np.add(lList, lorentzian0_func(x, amp11, cen11, sigma11))
    lList = np.add(lList, lorentzian0_func(x, amp12, cen12, sigma12))
    return lList


def lorentzian0_13(x, amp1, cen1, sigma1,
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

    lList = np.array(lorentzian0_func(x, amp1, cen1, sigma1))
    lList = np.add(lList, lorentzian0_func(x, amp2, cen2, sigma2))
    lList = np.add(lList, lorentzian0_func(x, amp3, cen3, sigma3))
    lList = np.add(lList, lorentzian0_func(x, amp4, cen4, sigma4))
    lList = np.add(lList, lorentzian0_func(x, amp5, cen5, sigma5))
    lList = np.add(lList, lorentzian0_func(x, amp6, cen6, sigma6))
    lList = np.add(lList, lorentzian0_func(x, amp7, cen7, sigma7))
    lList = np.add(lList, lorentzian0_func(x, amp8, cen8, sigma8))
    lList = np.add(lList, lorentzian0_func(x, amp9, cen9, sigma9))
    lList = np.add(lList, lorentzian0_func(x, amp10, cen10, sigma10))
    lList = np.add(lList, lorentzian0_func(x, amp11, cen11, sigma11))
    lList = np.add(lList, lorentzian0_func(x, amp12, cen12, sigma12))
    lList = np.add(lList, lorentzian0_func(x, amp13, cen13, sigma13))
    return lList


def lorentzian0_14(x, amp1, cen1, sigma1,
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

    lList = np.array(lorentzian0_func(x, amp1, cen1, sigma1))
    lList = np.add(lList, lorentzian0_func(x, amp2, cen2, sigma2))
    lList = np.add(lList, lorentzian0_func(x, amp3, cen3, sigma3))
    lList = np.add(lList, lorentzian0_func(x, amp4, cen4, sigma4))
    lList = np.add(lList, lorentzian0_func(x, amp5, cen5, sigma5))
    lList = np.add(lList, lorentzian0_func(x, amp6, cen6, sigma6))
    lList = np.add(lList, lorentzian0_func(x, amp7, cen7, sigma7))
    lList = np.add(lList, lorentzian0_func(x, amp8, cen8, sigma8))
    lList = np.add(lList, lorentzian0_func(x, amp9, cen9, sigma9))
    lList = np.add(lList, lorentzian0_func(x, amp10, cen10, sigma10))
    lList = np.add(lList, lorentzian0_func(x, amp11, cen11, sigma11))
    lList = np.add(lList, lorentzian0_func(x, amp12, cen12, sigma12))
    lList = np.add(lList, lorentzian0_func(x, amp13, cen13, sigma13))
    lList = np.add(lList, lorentzian0_func(x, amp14, cen14, sigma14))
    return lList


def lorentzian0_15(x, amp1, cen1, sigma1,
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

    lList = np.array(lorentzian0_func(x, amp1, cen1, sigma1))
    lList = np.add(lList, lorentzian0_func(x, amp2, cen2, sigma2))
    lList = np.add(lList, lorentzian0_func(x, amp3, cen3, sigma3))
    lList = np.add(lList, lorentzian0_func(x, amp4, cen4, sigma4))
    lList = np.add(lList, lorentzian0_func(x, amp5, cen5, sigma5))
    lList = np.add(lList, lorentzian0_func(x, amp6, cen6, sigma6))
    lList = np.add(lList, lorentzian0_func(x, amp7, cen7, sigma7))
    lList = np.add(lList, lorentzian0_func(x, amp8, cen8, sigma8))
    lList = np.add(lList, lorentzian0_func(x, amp9, cen9, sigma9))
    lList = np.add(lList, lorentzian0_func(x, amp10, cen10, sigma10))
    lList = np.add(lList, lorentzian0_func(x, amp11, cen11, sigma11))
    lList = np.add(lList, lorentzian0_func(x, amp12, cen12, sigma12))
    lList = np.add(lList, lorentzian0_func(x, amp13, cen13, sigma13))
    lList = np.add(lList, lorentzian0_func(x, amp14, cen14, sigma14))
    lList = np.add(lList, lorentzian0_func(x, amp15, cen15, sigma15))
    return lList


def lorentzian0_16(x, amp1, cen1, sigma1,
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

    lList = np.array(lorentzian0_func(x, amp1, cen1, sigma1))
    lList = np.add(lList, lorentzian0_func(x, amp2, cen2, sigma2))
    lList = np.add(lList, lorentzian0_func(x, amp3, cen3, sigma3))
    lList = np.add(lList, lorentzian0_func(x, amp4, cen4, sigma4))
    lList = np.add(lList, lorentzian0_func(x, amp5, cen5, sigma5))
    lList = np.add(lList, lorentzian0_func(x, amp6, cen6, sigma6))
    lList = np.add(lList, lorentzian0_func(x, amp7, cen7, sigma7))
    lList = np.add(lList, lorentzian0_func(x, amp8, cen8, sigma8))
    lList = np.add(lList, lorentzian0_func(x, amp9, cen9, sigma9))
    lList = np.add(lList, lorentzian0_func(x, amp10, cen10, sigma10))
    lList = np.add(lList, lorentzian0_func(x, amp11, cen11, sigma11))
    lList = np.add(lList, lorentzian0_func(x, amp12, cen12, sigma12))
    lList = np.add(lList, lorentzian0_func(x, amp13, cen13, sigma13))
    lList = np.add(lList, lorentzian0_func(x, amp14, cen14, sigma14))
    lList = np.add(lList, lorentzian0_func(x, amp15, cen15, sigma15))
    lList = np.add(lList, lorentzian0_func(x, amp16, cen16, sigma16))
    return lList


def lorentzian0_17(x, amp1, cen1, sigma1,
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

    lList = np.array(lorentzian0_func(x, amp1, cen1, sigma1))
    lList = np.add(lList, lorentzian0_func(x, amp2, cen2, sigma2))
    lList = np.add(lList, lorentzian0_func(x, amp3, cen3, sigma3))
    lList = np.add(lList, lorentzian0_func(x, amp4, cen4, sigma4))
    lList = np.add(lList, lorentzian0_func(x, amp5, cen5, sigma5))
    lList = np.add(lList, lorentzian0_func(x, amp6, cen6, sigma6))
    lList = np.add(lList, lorentzian0_func(x, amp7, cen7, sigma7))
    lList = np.add(lList, lorentzian0_func(x, amp8, cen8, sigma8))
    lList = np.add(lList, lorentzian0_func(x, amp9, cen9, sigma9))
    lList = np.add(lList, lorentzian0_func(x, amp10, cen10, sigma10))
    lList = np.add(lList, lorentzian0_func(x, amp11, cen11, sigma11))
    lList = np.add(lList, lorentzian0_func(x, amp12, cen12, sigma12))
    lList = np.add(lList, lorentzian0_func(x, amp13, cen13, sigma13))
    lList = np.add(lList, lorentzian0_func(x, amp14, cen14, sigma14))
    lList = np.add(lList, lorentzian0_func(x, amp15, cen15, sigma15))
    lList = np.add(lList, lorentzian0_func(x, amp16, cen16, sigma16))
    lList = np.add(lList, lorentzian0_func(x, amp17, cen17, sigma17))
    return lList


def lorentzian0_18(x, amp1, cen1, sigma1,
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

    lList = np.array(lorentzian0_func(x, amp1, cen1, sigma1))
    lList = np.add(lList, lorentzian0_func(x, amp2, cen2, sigma2))
    lList = np.add(lList, lorentzian0_func(x, amp3, cen3, sigma3))
    lList = np.add(lList, lorentzian0_func(x, amp4, cen4, sigma4))
    lList = np.add(lList, lorentzian0_func(x, amp5, cen5, sigma5))
    lList = np.add(lList, lorentzian0_func(x, amp6, cen6, sigma6))
    lList = np.add(lList, lorentzian0_func(x, amp7, cen7, sigma7))
    lList = np.add(lList, lorentzian0_func(x, amp8, cen8, sigma8))
    lList = np.add(lList, lorentzian0_func(x, amp9, cen9, sigma9))
    lList = np.add(lList, lorentzian0_func(x, amp10, cen10, sigma10))
    lList = np.add(lList, lorentzian0_func(x, amp11, cen11, sigma11))
    lList = np.add(lList, lorentzian0_func(x, amp12, cen12, sigma12))
    lList = np.add(lList, lorentzian0_func(x, amp13, cen13, sigma13))
    lList = np.add(lList, lorentzian0_func(x, amp14, cen14, sigma14))
    lList = np.add(lList, lorentzian0_func(x, amp15, cen15, sigma15))
    lList = np.add(lList, lorentzian0_func(x, amp16, cen16, sigma16))
    lList = np.add(lList, lorentzian0_func(x, amp17, cen17, sigma17))
    lList = np.add(lList, lorentzian0_func(x, amp18, cen18, sigma18))
    return lList


def lorentzian0_19(x, amp1, cen1, sigma1,
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

    lList = np.array(lorentzian0_func(x, amp1, cen1, sigma1))
    lList = np.add(lList, lorentzian0_func(x, amp2, cen2, sigma2))
    lList = np.add(lList, lorentzian0_func(x, amp3, cen3, sigma3))
    lList = np.add(lList, lorentzian0_func(x, amp4, cen4, sigma4))
    lList = np.add(lList, lorentzian0_func(x, amp5, cen5, sigma5))
    lList = np.add(lList, lorentzian0_func(x, amp6, cen6, sigma6))
    lList = np.add(lList, lorentzian0_func(x, amp7, cen7, sigma7))
    lList = np.add(lList, lorentzian0_func(x, amp8, cen8, sigma8))
    lList = np.add(lList, lorentzian0_func(x, amp9, cen9, sigma9))
    lList = np.add(lList, lorentzian0_func(x, amp10, cen10, sigma10))
    lList = np.add(lList, lorentzian0_func(x, amp11, cen11, sigma11))
    lList = np.add(lList, lorentzian0_func(x, amp12, cen12, sigma12))
    lList = np.add(lList, lorentzian0_func(x, amp13, cen13, sigma13))
    lList = np.add(lList, lorentzian0_func(x, amp14, cen14, sigma14))
    lList = np.add(lList, lorentzian0_func(x, amp15, cen15, sigma15))
    lList = np.add(lList, lorentzian0_func(x, amp16, cen16, sigma16))
    lList = np.add(lList, lorentzian0_func(x, amp17, cen17, sigma17))
    lList = np.add(lList, lorentzian0_func(x, amp18, cen18, sigma18))
    lList = np.add(lList, lorentzian0_func(x, amp19, cen19, sigma19))
    return lList


def lorentzian0_20(x, amp1, cen1, sigma1,
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

    lList = np.array(lorentzian0_func(x, amp1, cen1, sigma1))
    lList = np.add(lList, lorentzian0_func(x, amp2, cen2, sigma2))
    lList = np.add(lList, lorentzian0_func(x, amp3, cen3, sigma3))
    lList = np.add(lList, lorentzian0_func(x, amp4, cen4, sigma4))
    lList = np.add(lList, lorentzian0_func(x, amp5, cen5, sigma5))
    lList = np.add(lList, lorentzian0_func(x, amp6, cen6, sigma6))
    lList = np.add(lList, lorentzian0_func(x, amp7, cen7, sigma7))
    lList = np.add(lList, lorentzian0_func(x, amp8, cen8, sigma8))
    lList = np.add(lList, lorentzian0_func(x, amp9, cen9, sigma9))
    lList = np.add(lList, lorentzian0_func(x, amp10, cen10, sigma10))
    lList = np.add(lList, lorentzian0_func(x, amp11, cen11, sigma11))
    lList = np.add(lList, lorentzian0_func(x, amp12, cen12, sigma12))
    lList = np.add(lList, lorentzian0_func(x, amp13, cen13, sigma13))
    lList = np.add(lList, lorentzian0_func(x, amp14, cen14, sigma14))
    lList = np.add(lList, lorentzian0_func(x, amp15, cen15, sigma15))
    lList = np.add(lList, lorentzian0_func(x, amp16, cen16, sigma16))
    lList = np.add(lList, lorentzian0_func(x, amp17, cen17, sigma17))
    lList = np.add(lList, lorentzian0_func(x, amp18, cen18, sigma18))
    lList = np.add(lList, lorentzian0_func(x, amp19, cen19, sigma19))
    lList = np.add(lList, lorentzian0_func(x, amp20, cen20, sigma20))

lorentzian0FuncList = [lorentzian0_func, lorentzian0_func, lorentzian0_2,  lorentzian0_3,  lorentzian0_4,  lorentzian0_5,  lorentzian0_6,  lorentzian0_7,
                lorentzian0_8,    lorentzian0_9,    lorentzian0_10, lorentzian0_11, lorentzian0_12, lorentzian0_13, lorentzian0_14, lorentzian0_15,
                lorentzian0_16,   lorentzian0_17,   lorentzian0_18, lorentzian0_19, lorentzian0_20]
