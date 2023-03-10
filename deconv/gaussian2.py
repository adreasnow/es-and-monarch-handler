import numpy as np

def gaussian2_func(x, amp1, cen1, sigma1):
    first = np.multiply(amp1, np.exp(np.negative(np.divide(np.square(np.subtract(cen1, x)), (2 * sigma1)**2))))
    inner = np.add(np.subtract(np.subtract(cen1**2, np.multiply(2 * cen1, x)), sigma1**2), np.square(x))
    return np.divide(np.multiply(first, inner), sigma1**4)

def gaussian2_2(x, amp1, cen1, sigma1,
               amp2, cen2, sigma2):
    gList = np.array(gaussian2_func(x, amp1, cen1, sigma1))
    gList = np.add(gList, gaussian2_func(x, amp2, cen2, sigma2))
    return gList


def gaussian2_3(x, amp1, cen1, sigma1,
               amp2, cen2, sigma2,
               amp3, cen3, sigma3):

    gList = np.array(gaussian2_func(x, amp1, cen1, sigma1))
    gList = np.add(gList, gaussian2_func(x, amp2, cen2, sigma2))
    gList = np.add(gList, gaussian2_func(x, amp3, cen3, sigma3))
    return gList


def gaussian2_4(x, amp1, cen1, sigma1,
               amp2, cen2, sigma2,
               amp3, cen3, sigma3,
               amp4, cen4, sigma4):

    gList = np.array(gaussian2_func(x, amp1, cen1, sigma1))
    gList = np.add(gList, gaussian2_func(x, amp2, cen2, sigma2))
    gList = np.add(gList, gaussian2_func(x, amp3, cen3, sigma3))
    gList = np.add(gList, gaussian2_func(x, amp4, cen4, sigma4))
    return gList


def gaussian2_5(x, amp1, cen1, sigma1,
               amp2, cen2, sigma2,
               amp3, cen3, sigma3,
               amp4, cen4, sigma4,
               amp5, cen5, sigma5):

    gList = np.array(gaussian2_func(x, amp1, cen1, sigma1))
    gList = np.add(gList, gaussian2_func(x, amp2, cen2, sigma2))
    gList = np.add(gList, gaussian2_func(x, amp3, cen3, sigma3))
    gList = np.add(gList, gaussian2_func(x, amp4, cen4, sigma4))
    gList = np.add(gList, gaussian2_func(x, amp5, cen5, sigma5))
    return gList


def gaussian2_6(x, amp1, cen1, sigma1,
               amp2, cen2, sigma2,
               amp3, cen3, sigma3,
               amp4, cen4, sigma4,
               amp5, cen5, sigma5,
               amp6, cen6, sigma6):

    gList = np.array(gaussian2_func(x, amp1, cen1, sigma1))
    gList = np.add(gList, gaussian2_func(x, amp2, cen2, sigma2))
    gList = np.add(gList, gaussian2_func(x, amp3, cen3, sigma3))
    gList = np.add(gList, gaussian2_func(x, amp4, cen4, sigma4))
    gList = np.add(gList, gaussian2_func(x, amp5, cen5, sigma5))
    gList = np.add(gList, gaussian2_func(x, amp6, cen6, sigma6))
    return gList


def gaussian2_7(x, amp1, cen1, sigma1,
               amp2, cen2, sigma2,
               amp3, cen3, sigma3,
               amp4, cen4, sigma4,
               amp5, cen5, sigma5,
               amp6, cen6, sigma6,
               amp7, cen7, sigma7):

    gList = np.array(gaussian2_func(x, amp1, cen1, sigma1))
    gList = np.add(gList, gaussian2_func(x, amp2, cen2, sigma2))
    gList = np.add(gList, gaussian2_func(x, amp3, cen3, sigma3))
    gList = np.add(gList, gaussian2_func(x, amp4, cen4, sigma4))
    gList = np.add(gList, gaussian2_func(x, amp5, cen5, sigma5))
    gList = np.add(gList, gaussian2_func(x, amp6, cen6, sigma6))
    gList = np.add(gList, gaussian2_func(x, amp7, cen7, sigma7))
    return gList


def gaussian2_8(x, amp1, cen1, sigma1,
               amp2, cen2, sigma2,
               amp3, cen3, sigma3,
               amp4, cen4, sigma4,
               amp5, cen5, sigma5,
               amp6, cen6, sigma6,
               amp7, cen7, sigma7,
               amp8, cen8, sigma8):

    gList = np.array(gaussian2_func(x, amp1, cen1, sigma1))
    gList = np.add(gList, gaussian2_func(x, amp2, cen2, sigma2))
    gList = np.add(gList, gaussian2_func(x, amp3, cen3, sigma3))
    gList = np.add(gList, gaussian2_func(x, amp4, cen4, sigma4))
    gList = np.add(gList, gaussian2_func(x, amp5, cen5, sigma5))
    gList = np.add(gList, gaussian2_func(x, amp6, cen6, sigma6))
    gList = np.add(gList, gaussian2_func(x, amp7, cen7, sigma7))
    gList = np.add(gList, gaussian2_func(x, amp8, cen8, sigma8))
    return gList


def gaussian2_9(x, amp1, cen1, sigma1,
               amp2, cen2, sigma2,
               amp3, cen3, sigma3,
               amp4, cen4, sigma4,
               amp5, cen5, sigma5,
               amp6, cen6, sigma6,
               amp7, cen7, sigma7,
               amp8, cen8, sigma8,
               amp9, cen9, sigma9):

    gList = np.array(gaussian2_func(x, amp1, cen1, sigma1))
    gList = np.add(gList, gaussian2_func(x, amp2, cen2, sigma2))
    gList = np.add(gList, gaussian2_func(x, amp3, cen3, sigma3))
    gList = np.add(gList, gaussian2_func(x, amp4, cen4, sigma4))
    gList = np.add(gList, gaussian2_func(x, amp5, cen5, sigma5))
    gList = np.add(gList, gaussian2_func(x, amp6, cen6, sigma6))
    gList = np.add(gList, gaussian2_func(x, amp7, cen7, sigma7))
    gList = np.add(gList, gaussian2_func(x, amp8, cen8, sigma8))
    gList = np.add(gList, gaussian2_func(x, amp9, cen9, sigma9))
    return gList


def gaussian2_10(x, amp1, cen1, sigma1,
                amp2, cen2, sigma2,
                amp3, cen3, sigma3,
                amp4, cen4, sigma4,
                amp5, cen5, sigma5,
                amp6, cen6, sigma6,
                amp7, cen7, sigma7,
                amp8, cen8, sigma8,
                amp9, cen9, sigma9,
                amp10, cen10, sigma10):

    gList = np.array(gaussian2_func(x, amp1, cen1, sigma1))
    gList = np.add(gList, gaussian2_func(x, amp2, cen2, sigma2))
    gList = np.add(gList, gaussian2_func(x, amp3, cen3, sigma3))
    gList = np.add(gList, gaussian2_func(x, amp4, cen4, sigma4))
    gList = np.add(gList, gaussian2_func(x, amp5, cen5, sigma5))
    gList = np.add(gList, gaussian2_func(x, amp6, cen6, sigma6))
    gList = np.add(gList, gaussian2_func(x, amp7, cen7, sigma7))
    gList = np.add(gList, gaussian2_func(x, amp8, cen8, sigma8))
    gList = np.add(gList, gaussian2_func(x, amp9, cen9, sigma9))
    gList = np.add(gList, gaussian2_func(x, amp10, cen10, sigma10))
    return gList


def gaussian2_11(x, amp1, cen1, sigma1,
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

    gList = np.array(gaussian2_func(x, amp1, cen1, sigma1))
    gList = np.add(gList, gaussian2_func(x, amp2, cen2, sigma2))
    gList = np.add(gList, gaussian2_func(x, amp3, cen3, sigma3))
    gList = np.add(gList, gaussian2_func(x, amp4, cen4, sigma4))
    gList = np.add(gList, gaussian2_func(x, amp5, cen5, sigma5))
    gList = np.add(gList, gaussian2_func(x, amp6, cen6, sigma6))
    gList = np.add(gList, gaussian2_func(x, amp7, cen7, sigma7))
    gList = np.add(gList, gaussian2_func(x, amp8, cen8, sigma8))
    gList = np.add(gList, gaussian2_func(x, amp9, cen9, sigma9))
    gList = np.add(gList, gaussian2_func(x, amp10, cen10, sigma10))
    gList = np.add(gList, gaussian2_func(x, amp11, cen11, sigma11))
    return gList


def gaussian2_12(x, amp1, cen1, sigma1,
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

    gList = np.array(gaussian2_func(x, amp1, cen1, sigma1))
    gList = np.add(gList, gaussian2_func(x, amp2, cen2, sigma2))
    gList = np.add(gList, gaussian2_func(x, amp3, cen3, sigma3))
    gList = np.add(gList, gaussian2_func(x, amp4, cen4, sigma4))
    gList = np.add(gList, gaussian2_func(x, amp5, cen5, sigma5))
    gList = np.add(gList, gaussian2_func(x, amp6, cen6, sigma6))
    gList = np.add(gList, gaussian2_func(x, amp7, cen7, sigma7))
    gList = np.add(gList, gaussian2_func(x, amp8, cen8, sigma8))
    gList = np.add(gList, gaussian2_func(x, amp9, cen9, sigma9))
    gList = np.add(gList, gaussian2_func(x, amp10, cen10, sigma10))
    gList = np.add(gList, gaussian2_func(x, amp11, cen11, sigma11))
    gList = np.add(gList, gaussian2_func(x, amp12, cen12, sigma12))
    return gList


def gaussian2_13(x, amp1, cen1, sigma1,
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

    gList = np.array(gaussian2_func(x, amp1, cen1, sigma1))
    gList = np.add(gList, gaussian2_func(x, amp2, cen2, sigma2))
    gList = np.add(gList, gaussian2_func(x, amp3, cen3, sigma3))
    gList = np.add(gList, gaussian2_func(x, amp4, cen4, sigma4))
    gList = np.add(gList, gaussian2_func(x, amp5, cen5, sigma5))
    gList = np.add(gList, gaussian2_func(x, amp6, cen6, sigma6))
    gList = np.add(gList, gaussian2_func(x, amp7, cen7, sigma7))
    gList = np.add(gList, gaussian2_func(x, amp8, cen8, sigma8))
    gList = np.add(gList, gaussian2_func(x, amp9, cen9, sigma9))
    gList = np.add(gList, gaussian2_func(x, amp10, cen10, sigma10))
    gList = np.add(gList, gaussian2_func(x, amp11, cen11, sigma11))
    gList = np.add(gList, gaussian2_func(x, amp12, cen12, sigma12))
    gList = np.add(gList, gaussian2_func(x, amp13, cen13, sigma13))
    return gList


def gaussian2_14(x, amp1, cen1, sigma1,
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

    gList = np.array(gaussian2_func(x, amp1, cen1, sigma1))
    gList = np.add(gList, gaussian2_func(x, amp2, cen2, sigma2))
    gList = np.add(gList, gaussian2_func(x, amp3, cen3, sigma3))
    gList = np.add(gList, gaussian2_func(x, amp4, cen4, sigma4))
    gList = np.add(gList, gaussian2_func(x, amp5, cen5, sigma5))
    gList = np.add(gList, gaussian2_func(x, amp6, cen6, sigma6))
    gList = np.add(gList, gaussian2_func(x, amp7, cen7, sigma7))
    gList = np.add(gList, gaussian2_func(x, amp8, cen8, sigma8))
    gList = np.add(gList, gaussian2_func(x, amp9, cen9, sigma9))
    gList = np.add(gList, gaussian2_func(x, amp10, cen10, sigma10))
    gList = np.add(gList, gaussian2_func(x, amp11, cen11, sigma11))
    gList = np.add(gList, gaussian2_func(x, amp12, cen12, sigma12))
    gList = np.add(gList, gaussian2_func(x, amp13, cen13, sigma13))
    gList = np.add(gList, gaussian2_func(x, amp14, cen14, sigma14))
    return gList


def gaussian2_15(x, amp1, cen1, sigma1,
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

    gList = np.array(gaussian2_func(x, amp1, cen1, sigma1))
    gList = np.add(gList, gaussian2_func(x, amp2, cen2, sigma2))
    gList = np.add(gList, gaussian2_func(x, amp3, cen3, sigma3))
    gList = np.add(gList, gaussian2_func(x, amp4, cen4, sigma4))
    gList = np.add(gList, gaussian2_func(x, amp5, cen5, sigma5))
    gList = np.add(gList, gaussian2_func(x, amp6, cen6, sigma6))
    gList = np.add(gList, gaussian2_func(x, amp7, cen7, sigma7))
    gList = np.add(gList, gaussian2_func(x, amp8, cen8, sigma8))
    gList = np.add(gList, gaussian2_func(x, amp9, cen9, sigma9))
    gList = np.add(gList, gaussian2_func(x, amp10, cen10, sigma10))
    gList = np.add(gList, gaussian2_func(x, amp11, cen11, sigma11))
    gList = np.add(gList, gaussian2_func(x, amp12, cen12, sigma12))
    gList = np.add(gList, gaussian2_func(x, amp13, cen13, sigma13))
    gList = np.add(gList, gaussian2_func(x, amp14, cen14, sigma14))
    gList = np.add(gList, gaussian2_func(x, amp15, cen15, sigma15))
    return gList


def gaussian2_16(x, amp1, cen1, sigma1,
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

    gList = np.array(gaussian2_func(x, amp1, cen1, sigma1))
    gList = np.add(gList, gaussian2_func(x, amp2, cen2, sigma2))
    gList = np.add(gList, gaussian2_func(x, amp3, cen3, sigma3))
    gList = np.add(gList, gaussian2_func(x, amp4, cen4, sigma4))
    gList = np.add(gList, gaussian2_func(x, amp5, cen5, sigma5))
    gList = np.add(gList, gaussian2_func(x, amp6, cen6, sigma6))
    gList = np.add(gList, gaussian2_func(x, amp7, cen7, sigma7))
    gList = np.add(gList, gaussian2_func(x, amp8, cen8, sigma8))
    gList = np.add(gList, gaussian2_func(x, amp9, cen9, sigma9))
    gList = np.add(gList, gaussian2_func(x, amp10, cen10, sigma10))
    gList = np.add(gList, gaussian2_func(x, amp11, cen11, sigma11))
    gList = np.add(gList, gaussian2_func(x, amp12, cen12, sigma12))
    gList = np.add(gList, gaussian2_func(x, amp13, cen13, sigma13))
    gList = np.add(gList, gaussian2_func(x, amp14, cen14, sigma14))
    gList = np.add(gList, gaussian2_func(x, amp15, cen15, sigma15))
    gList = np.add(gList, gaussian2_func(x, amp16, cen16, sigma16))
    return gList


def gaussian2_17(x, amp1, cen1, sigma1,
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

    gList = np.array(gaussian2_func(x, amp1, cen1, sigma1))
    gList = np.add(gList, gaussian2_func(x, amp2, cen2, sigma2))
    gList = np.add(gList, gaussian2_func(x, amp3, cen3, sigma3))
    gList = np.add(gList, gaussian2_func(x, amp4, cen4, sigma4))
    gList = np.add(gList, gaussian2_func(x, amp5, cen5, sigma5))
    gList = np.add(gList, gaussian2_func(x, amp6, cen6, sigma6))
    gList = np.add(gList, gaussian2_func(x, amp7, cen7, sigma7))
    gList = np.add(gList, gaussian2_func(x, amp8, cen8, sigma8))
    gList = np.add(gList, gaussian2_func(x, amp9, cen9, sigma9))
    gList = np.add(gList, gaussian2_func(x, amp10, cen10, sigma10))
    gList = np.add(gList, gaussian2_func(x, amp11, cen11, sigma11))
    gList = np.add(gList, gaussian2_func(x, amp12, cen12, sigma12))
    gList = np.add(gList, gaussian2_func(x, amp13, cen13, sigma13))
    gList = np.add(gList, gaussian2_func(x, amp14, cen14, sigma14))
    gList = np.add(gList, gaussian2_func(x, amp15, cen15, sigma15))
    gList = np.add(gList, gaussian2_func(x, amp16, cen16, sigma16))
    gList = np.add(gList, gaussian2_func(x, amp17, cen17, sigma17))
    return gList


def gaussian2_18(x, amp1, cen1, sigma1,
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

    gList = np.array(gaussian2_func(x, amp1, cen1, sigma1))
    gList = np.add(gList, gaussian2_func(x, amp2, cen2, sigma2))
    gList = np.add(gList, gaussian2_func(x, amp3, cen3, sigma3))
    gList = np.add(gList, gaussian2_func(x, amp4, cen4, sigma4))
    gList = np.add(gList, gaussian2_func(x, amp5, cen5, sigma5))
    gList = np.add(gList, gaussian2_func(x, amp6, cen6, sigma6))
    gList = np.add(gList, gaussian2_func(x, amp7, cen7, sigma7))
    gList = np.add(gList, gaussian2_func(x, amp8, cen8, sigma8))
    gList = np.add(gList, gaussian2_func(x, amp9, cen9, sigma9))
    gList = np.add(gList, gaussian2_func(x, amp10, cen10, sigma10))
    gList = np.add(gList, gaussian2_func(x, amp11, cen11, sigma11))
    gList = np.add(gList, gaussian2_func(x, amp12, cen12, sigma12))
    gList = np.add(gList, gaussian2_func(x, amp13, cen13, sigma13))
    gList = np.add(gList, gaussian2_func(x, amp14, cen14, sigma14))
    gList = np.add(gList, gaussian2_func(x, amp15, cen15, sigma15))
    gList = np.add(gList, gaussian2_func(x, amp16, cen16, sigma16))
    gList = np.add(gList, gaussian2_func(x, amp17, cen17, sigma17))
    gList = np.add(gList, gaussian2_func(x, amp18, cen18, sigma18))
    return gList


def gaussian2_19(x, amp1, cen1, sigma1,
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

    gList = np.array(gaussian2_func(x, amp1, cen1, sigma1))
    gList = np.add(gList, gaussian2_func(x, amp2, cen2, sigma2))
    gList = np.add(gList, gaussian2_func(x, amp3, cen3, sigma3))
    gList = np.add(gList, gaussian2_func(x, amp4, cen4, sigma4))
    gList = np.add(gList, gaussian2_func(x, amp5, cen5, sigma5))
    gList = np.add(gList, gaussian2_func(x, amp6, cen6, sigma6))
    gList = np.add(gList, gaussian2_func(x, amp7, cen7, sigma7))
    gList = np.add(gList, gaussian2_func(x, amp8, cen8, sigma8))
    gList = np.add(gList, gaussian2_func(x, amp9, cen9, sigma9))
    gList = np.add(gList, gaussian2_func(x, amp10, cen10, sigma10))
    gList = np.add(gList, gaussian2_func(x, amp11, cen11, sigma11))
    gList = np.add(gList, gaussian2_func(x, amp12, cen12, sigma12))
    gList = np.add(gList, gaussian2_func(x, amp13, cen13, sigma13))
    gList = np.add(gList, gaussian2_func(x, amp14, cen14, sigma14))
    gList = np.add(gList, gaussian2_func(x, amp15, cen15, sigma15))
    gList = np.add(gList, gaussian2_func(x, amp16, cen16, sigma16))
    gList = np.add(gList, gaussian2_func(x, amp17, cen17, sigma17))
    gList = np.add(gList, gaussian2_func(x, amp18, cen18, sigma18))
    gList = np.add(gList, gaussian2_func(x, amp19, cen19, sigma19))
    return gList


def gaussian2_20(x, amp1, cen1, sigma1,
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

    gList = np.array(gaussian2_func(x, amp1, cen1, sigma1))
    gList = np.add(gList, gaussian2_func(x, amp2, cen2, sigma2))
    gList = np.add(gList, gaussian2_func(x, amp3, cen3, sigma3))
    gList = np.add(gList, gaussian2_func(x, amp4, cen4, sigma4))
    gList = np.add(gList, gaussian2_func(x, amp5, cen5, sigma5))
    gList = np.add(gList, gaussian2_func(x, amp6, cen6, sigma6))
    gList = np.add(gList, gaussian2_func(x, amp7, cen7, sigma7))
    gList = np.add(gList, gaussian2_func(x, amp8, cen8, sigma8))
    gList = np.add(gList, gaussian2_func(x, amp9, cen9, sigma9))
    gList = np.add(gList, gaussian2_func(x, amp10, cen10, sigma10))
    gList = np.add(gList, gaussian2_func(x, amp11, cen11, sigma11))
    gList = np.add(gList, gaussian2_func(x, amp12, cen12, sigma12))
    gList = np.add(gList, gaussian2_func(x, amp13, cen13, sigma13))
    gList = np.add(gList, gaussian2_func(x, amp14, cen14, sigma14))
    gList = np.add(gList, gaussian2_func(x, amp15, cen15, sigma15))
    gList = np.add(gList, gaussian2_func(x, amp16, cen16, sigma16))
    gList = np.add(gList, gaussian2_func(x, amp17, cen17, sigma17))
    gList = np.add(gList, gaussian2_func(x, amp18, cen18, sigma18))
    gList = np.add(gList, gaussian2_func(x, amp19, cen19, sigma19))
    gList = np.add(gList, gaussian2_func(x, amp20, cen20, sigma20))


gaussian2FuncList = [gaussian2_func, gaussian2_func, gaussian2_2,  gaussian2_3,  gaussian2_4,  gaussian2_5,  gaussian2_6,  gaussian2_7,
                      gaussian2_8,    gaussian2_9,    gaussian2_10, gaussian2_11, gaussian2_12, gaussian2_13, gaussian2_14, gaussian2_15,
                      gaussian2_16,   gaussian2_17,   gaussian2_18, gaussian2_19, gaussian2_20]

