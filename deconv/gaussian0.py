import numpy as np

def gaussian0_func(x, amp1, cen1, sigma1):
    return np.multiply(amp1, np.exp(np.negative(np.divide(np.square(np.subtract(cen1, x)), (2 * sigma1)**2))))


def gaussian0_2(x, amp1, cen1, sigma1,
               amp2, cen2, sigma2):
    gList = np.array(gaussian0_func(x, amp1, cen1, sigma1))
    gList = np.add(gList, gaussian0_func(x, amp2, cen2, sigma2))
    return gList


def gaussian0_3(x, amp1, cen1, sigma1,
               amp2, cen2, sigma2,
               amp3, cen3, sigma3):

    gList = np.array(gaussian0_func(x, amp1, cen1, sigma1))
    gList = np.add(gList, gaussian0_func(x, amp2, cen2, sigma2))
    gList = np.add(gList, gaussian0_func(x, amp3, cen3, sigma3))
    return gList


def gaussian0_4(x, amp1, cen1, sigma1,
               amp2, cen2, sigma2,
               amp3, cen3, sigma3,
               amp4, cen4, sigma4):

    gList = np.array(gaussian0_func(x, amp1, cen1, sigma1))
    gList = np.add(gList, gaussian0_func(x, amp2, cen2, sigma2))
    gList = np.add(gList, gaussian0_func(x, amp3, cen3, sigma3))
    gList = np.add(gList, gaussian0_func(x, amp4, cen4, sigma4))
    return gList


def gaussian0_5(x, amp1, cen1, sigma1,
               amp2, cen2, sigma2,
               amp3, cen3, sigma3,
               amp4, cen4, sigma4,
               amp5, cen5, sigma5):

    gList = np.array(gaussian0_func(x, amp1, cen1, sigma1))
    gList = np.add(gList, gaussian0_func(x, amp2, cen2, sigma2))
    gList = np.add(gList, gaussian0_func(x, amp3, cen3, sigma3))
    gList = np.add(gList, gaussian0_func(x, amp4, cen4, sigma4))
    gList = np.add(gList, gaussian0_func(x, amp5, cen5, sigma5))
    return gList


def gaussian0_6(x, amp1, cen1, sigma1,
               amp2, cen2, sigma2,
               amp3, cen3, sigma3,
               amp4, cen4, sigma4,
               amp5, cen5, sigma5,
               amp6, cen6, sigma6):

    gList = np.array(gaussian0_func(x, amp1, cen1, sigma1))
    gList = np.add(gList, gaussian0_func(x, amp2, cen2, sigma2))
    gList = np.add(gList, gaussian0_func(x, amp3, cen3, sigma3))
    gList = np.add(gList, gaussian0_func(x, amp4, cen4, sigma4))
    gList = np.add(gList, gaussian0_func(x, amp5, cen5, sigma5))
    gList = np.add(gList, gaussian0_func(x, amp6, cen6, sigma6))
    return gList


def gaussian0_7(x, amp1, cen1, sigma1,
               amp2, cen2, sigma2,
               amp3, cen3, sigma3,
               amp4, cen4, sigma4,
               amp5, cen5, sigma5,
               amp6, cen6, sigma6,
               amp7, cen7, sigma7):

    gList = np.array(gaussian0_func(x, amp1, cen1, sigma1))
    gList = np.add(gList, gaussian0_func(x, amp2, cen2, sigma2))
    gList = np.add(gList, gaussian0_func(x, amp3, cen3, sigma3))
    gList = np.add(gList, gaussian0_func(x, amp4, cen4, sigma4))
    gList = np.add(gList, gaussian0_func(x, amp5, cen5, sigma5))
    gList = np.add(gList, gaussian0_func(x, amp6, cen6, sigma6))
    gList = np.add(gList, gaussian0_func(x, amp7, cen7, sigma7))
    return gList


def gaussian0_8(x, amp1, cen1, sigma1,
               amp2, cen2, sigma2,
               amp3, cen3, sigma3,
               amp4, cen4, sigma4,
               amp5, cen5, sigma5,
               amp6, cen6, sigma6,
               amp7, cen7, sigma7,
               amp8, cen8, sigma8):

    gList = np.array(gaussian0_func(x, amp1, cen1, sigma1))
    gList = np.add(gList, gaussian0_func(x, amp2, cen2, sigma2))
    gList = np.add(gList, gaussian0_func(x, amp3, cen3, sigma3))
    gList = np.add(gList, gaussian0_func(x, amp4, cen4, sigma4))
    gList = np.add(gList, gaussian0_func(x, amp5, cen5, sigma5))
    gList = np.add(gList, gaussian0_func(x, amp6, cen6, sigma6))
    gList = np.add(gList, gaussian0_func(x, amp7, cen7, sigma7))
    gList = np.add(gList, gaussian0_func(x, amp8, cen8, sigma8))
    return gList


def gaussian0_9(x, amp1, cen1, sigma1,
               amp2, cen2, sigma2,
               amp3, cen3, sigma3,
               amp4, cen4, sigma4,
               amp5, cen5, sigma5,
               amp6, cen6, sigma6,
               amp7, cen7, sigma7,
               amp8, cen8, sigma8,
               amp9, cen9, sigma9):

    gList = np.array(gaussian0_func(x, amp1, cen1, sigma1))
    gList = np.add(gList, gaussian0_func(x, amp2, cen2, sigma2))
    gList = np.add(gList, gaussian0_func(x, amp3, cen3, sigma3))
    gList = np.add(gList, gaussian0_func(x, amp4, cen4, sigma4))
    gList = np.add(gList, gaussian0_func(x, amp5, cen5, sigma5))
    gList = np.add(gList, gaussian0_func(x, amp6, cen6, sigma6))
    gList = np.add(gList, gaussian0_func(x, amp7, cen7, sigma7))
    gList = np.add(gList, gaussian0_func(x, amp8, cen8, sigma8))
    gList = np.add(gList, gaussian0_func(x, amp9, cen9, sigma9))
    return gList


def gaussian0_10(x, amp1, cen1, sigma1,
                amp2, cen2, sigma2,
                amp3, cen3, sigma3,
                amp4, cen4, sigma4,
                amp5, cen5, sigma5,
                amp6, cen6, sigma6,
                amp7, cen7, sigma7,
                amp8, cen8, sigma8,
                amp9, cen9, sigma9,
                amp10, cen10, sigma10):

    gList = np.array(gaussian0_func(x, amp1, cen1, sigma1))
    gList = np.add(gList, gaussian0_func(x, amp2, cen2, sigma2))
    gList = np.add(gList, gaussian0_func(x, amp3, cen3, sigma3))
    gList = np.add(gList, gaussian0_func(x, amp4, cen4, sigma4))
    gList = np.add(gList, gaussian0_func(x, amp5, cen5, sigma5))
    gList = np.add(gList, gaussian0_func(x, amp6, cen6, sigma6))
    gList = np.add(gList, gaussian0_func(x, amp7, cen7, sigma7))
    gList = np.add(gList, gaussian0_func(x, amp8, cen8, sigma8))
    gList = np.add(gList, gaussian0_func(x, amp9, cen9, sigma9))
    gList = np.add(gList, gaussian0_func(x, amp10, cen10, sigma10))
    return gList


def gaussian0_11(x, amp1, cen1, sigma1,
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

    gList = np.array(gaussian0_func(x, amp1, cen1, sigma1))
    gList = np.add(gList, gaussian0_func(x, amp2, cen2, sigma2))
    gList = np.add(gList, gaussian0_func(x, amp3, cen3, sigma3))
    gList = np.add(gList, gaussian0_func(x, amp4, cen4, sigma4))
    gList = np.add(gList, gaussian0_func(x, amp5, cen5, sigma5))
    gList = np.add(gList, gaussian0_func(x, amp6, cen6, sigma6))
    gList = np.add(gList, gaussian0_func(x, amp7, cen7, sigma7))
    gList = np.add(gList, gaussian0_func(x, amp8, cen8, sigma8))
    gList = np.add(gList, gaussian0_func(x, amp9, cen9, sigma9))
    gList = np.add(gList, gaussian0_func(x, amp10, cen10, sigma10))
    gList = np.add(gList, gaussian0_func(x, amp11, cen11, sigma11))
    return gList


def gaussian0_12(x, amp1, cen1, sigma1,
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

    gList = np.array(gaussian0_func(x, amp1, cen1, sigma1))
    gList = np.add(gList, gaussian0_func(x, amp2, cen2, sigma2))
    gList = np.add(gList, gaussian0_func(x, amp3, cen3, sigma3))
    gList = np.add(gList, gaussian0_func(x, amp4, cen4, sigma4))
    gList = np.add(gList, gaussian0_func(x, amp5, cen5, sigma5))
    gList = np.add(gList, gaussian0_func(x, amp6, cen6, sigma6))
    gList = np.add(gList, gaussian0_func(x, amp7, cen7, sigma7))
    gList = np.add(gList, gaussian0_func(x, amp8, cen8, sigma8))
    gList = np.add(gList, gaussian0_func(x, amp9, cen9, sigma9))
    gList = np.add(gList, gaussian0_func(x, amp10, cen10, sigma10))
    gList = np.add(gList, gaussian0_func(x, amp11, cen11, sigma11))
    gList = np.add(gList, gaussian0_func(x, amp12, cen12, sigma12))
    return gList


def gaussian0_13(x, amp1, cen1, sigma1,
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

    gList = np.array(gaussian0_func(x, amp1, cen1, sigma1))
    gList = np.add(gList, gaussian0_func(x, amp2, cen2, sigma2))
    gList = np.add(gList, gaussian0_func(x, amp3, cen3, sigma3))
    gList = np.add(gList, gaussian0_func(x, amp4, cen4, sigma4))
    gList = np.add(gList, gaussian0_func(x, amp5, cen5, sigma5))
    gList = np.add(gList, gaussian0_func(x, amp6, cen6, sigma6))
    gList = np.add(gList, gaussian0_func(x, amp7, cen7, sigma7))
    gList = np.add(gList, gaussian0_func(x, amp8, cen8, sigma8))
    gList = np.add(gList, gaussian0_func(x, amp9, cen9, sigma9))
    gList = np.add(gList, gaussian0_func(x, amp10, cen10, sigma10))
    gList = np.add(gList, gaussian0_func(x, amp11, cen11, sigma11))
    gList = np.add(gList, gaussian0_func(x, amp12, cen12, sigma12))
    gList = np.add(gList, gaussian0_func(x, amp13, cen13, sigma13))
    return gList


def gaussian0_14(x, amp1, cen1, sigma1,
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

    gList = np.array(gaussian0_func(x, amp1, cen1, sigma1))
    gList = np.add(gList, gaussian0_func(x, amp2, cen2, sigma2))
    gList = np.add(gList, gaussian0_func(x, amp3, cen3, sigma3))
    gList = np.add(gList, gaussian0_func(x, amp4, cen4, sigma4))
    gList = np.add(gList, gaussian0_func(x, amp5, cen5, sigma5))
    gList = np.add(gList, gaussian0_func(x, amp6, cen6, sigma6))
    gList = np.add(gList, gaussian0_func(x, amp7, cen7, sigma7))
    gList = np.add(gList, gaussian0_func(x, amp8, cen8, sigma8))
    gList = np.add(gList, gaussian0_func(x, amp9, cen9, sigma9))
    gList = np.add(gList, gaussian0_func(x, amp10, cen10, sigma10))
    gList = np.add(gList, gaussian0_func(x, amp11, cen11, sigma11))
    gList = np.add(gList, gaussian0_func(x, amp12, cen12, sigma12))
    gList = np.add(gList, gaussian0_func(x, amp13, cen13, sigma13))
    gList = np.add(gList, gaussian0_func(x, amp14, cen14, sigma14))
    return gList


def gaussian0_15(x, amp1, cen1, sigma1,
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

    gList = np.array(gaussian0_func(x, amp1, cen1, sigma1))
    gList = np.add(gList, gaussian0_func(x, amp2, cen2, sigma2))
    gList = np.add(gList, gaussian0_func(x, amp3, cen3, sigma3))
    gList = np.add(gList, gaussian0_func(x, amp4, cen4, sigma4))
    gList = np.add(gList, gaussian0_func(x, amp5, cen5, sigma5))
    gList = np.add(gList, gaussian0_func(x, amp6, cen6, sigma6))
    gList = np.add(gList, gaussian0_func(x, amp7, cen7, sigma7))
    gList = np.add(gList, gaussian0_func(x, amp8, cen8, sigma8))
    gList = np.add(gList, gaussian0_func(x, amp9, cen9, sigma9))
    gList = np.add(gList, gaussian0_func(x, amp10, cen10, sigma10))
    gList = np.add(gList, gaussian0_func(x, amp11, cen11, sigma11))
    gList = np.add(gList, gaussian0_func(x, amp12, cen12, sigma12))
    gList = np.add(gList, gaussian0_func(x, amp13, cen13, sigma13))
    gList = np.add(gList, gaussian0_func(x, amp14, cen14, sigma14))
    gList = np.add(gList, gaussian0_func(x, amp15, cen15, sigma15))
    return gList


def gaussian0_16(x, amp1, cen1, sigma1,
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

    gList = np.array(gaussian0_func(x, amp1, cen1, sigma1))
    gList = np.add(gList, gaussian0_func(x, amp2, cen2, sigma2))
    gList = np.add(gList, gaussian0_func(x, amp3, cen3, sigma3))
    gList = np.add(gList, gaussian0_func(x, amp4, cen4, sigma4))
    gList = np.add(gList, gaussian0_func(x, amp5, cen5, sigma5))
    gList = np.add(gList, gaussian0_func(x, amp6, cen6, sigma6))
    gList = np.add(gList, gaussian0_func(x, amp7, cen7, sigma7))
    gList = np.add(gList, gaussian0_func(x, amp8, cen8, sigma8))
    gList = np.add(gList, gaussian0_func(x, amp9, cen9, sigma9))
    gList = np.add(gList, gaussian0_func(x, amp10, cen10, sigma10))
    gList = np.add(gList, gaussian0_func(x, amp11, cen11, sigma11))
    gList = np.add(gList, gaussian0_func(x, amp12, cen12, sigma12))
    gList = np.add(gList, gaussian0_func(x, amp13, cen13, sigma13))
    gList = np.add(gList, gaussian0_func(x, amp14, cen14, sigma14))
    gList = np.add(gList, gaussian0_func(x, amp15, cen15, sigma15))
    gList = np.add(gList, gaussian0_func(x, amp16, cen16, sigma16))
    return gList


def gaussian0_17(x, amp1, cen1, sigma1,
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

    gList = np.array(gaussian0_func(x, amp1, cen1, sigma1))
    gList = np.add(gList, gaussian0_func(x, amp2, cen2, sigma2))
    gList = np.add(gList, gaussian0_func(x, amp3, cen3, sigma3))
    gList = np.add(gList, gaussian0_func(x, amp4, cen4, sigma4))
    gList = np.add(gList, gaussian0_func(x, amp5, cen5, sigma5))
    gList = np.add(gList, gaussian0_func(x, amp6, cen6, sigma6))
    gList = np.add(gList, gaussian0_func(x, amp7, cen7, sigma7))
    gList = np.add(gList, gaussian0_func(x, amp8, cen8, sigma8))
    gList = np.add(gList, gaussian0_func(x, amp9, cen9, sigma9))
    gList = np.add(gList, gaussian0_func(x, amp10, cen10, sigma10))
    gList = np.add(gList, gaussian0_func(x, amp11, cen11, sigma11))
    gList = np.add(gList, gaussian0_func(x, amp12, cen12, sigma12))
    gList = np.add(gList, gaussian0_func(x, amp13, cen13, sigma13))
    gList = np.add(gList, gaussian0_func(x, amp14, cen14, sigma14))
    gList = np.add(gList, gaussian0_func(x, amp15, cen15, sigma15))
    gList = np.add(gList, gaussian0_func(x, amp16, cen16, sigma16))
    gList = np.add(gList, gaussian0_func(x, amp17, cen17, sigma17))
    return gList


def gaussian0_18(x, amp1, cen1, sigma1,
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

    gList = np.array(gaussian0_func(x, amp1, cen1, sigma1))
    gList = np.add(gList, gaussian0_func(x, amp2, cen2, sigma2))
    gList = np.add(gList, gaussian0_func(x, amp3, cen3, sigma3))
    gList = np.add(gList, gaussian0_func(x, amp4, cen4, sigma4))
    gList = np.add(gList, gaussian0_func(x, amp5, cen5, sigma5))
    gList = np.add(gList, gaussian0_func(x, amp6, cen6, sigma6))
    gList = np.add(gList, gaussian0_func(x, amp7, cen7, sigma7))
    gList = np.add(gList, gaussian0_func(x, amp8, cen8, sigma8))
    gList = np.add(gList, gaussian0_func(x, amp9, cen9, sigma9))
    gList = np.add(gList, gaussian0_func(x, amp10, cen10, sigma10))
    gList = np.add(gList, gaussian0_func(x, amp11, cen11, sigma11))
    gList = np.add(gList, gaussian0_func(x, amp12, cen12, sigma12))
    gList = np.add(gList, gaussian0_func(x, amp13, cen13, sigma13))
    gList = np.add(gList, gaussian0_func(x, amp14, cen14, sigma14))
    gList = np.add(gList, gaussian0_func(x, amp15, cen15, sigma15))
    gList = np.add(gList, gaussian0_func(x, amp16, cen16, sigma16))
    gList = np.add(gList, gaussian0_func(x, amp17, cen17, sigma17))
    gList = np.add(gList, gaussian0_func(x, amp18, cen18, sigma18))
    return gList


def gaussian0_19(x, amp1, cen1, sigma1,
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

    gList = np.array(gaussian0_func(x, amp1, cen1, sigma1))
    gList = np.add(gList, gaussian0_func(x, amp2, cen2, sigma2))
    gList = np.add(gList, gaussian0_func(x, amp3, cen3, sigma3))
    gList = np.add(gList, gaussian0_func(x, amp4, cen4, sigma4))
    gList = np.add(gList, gaussian0_func(x, amp5, cen5, sigma5))
    gList = np.add(gList, gaussian0_func(x, amp6, cen6, sigma6))
    gList = np.add(gList, gaussian0_func(x, amp7, cen7, sigma7))
    gList = np.add(gList, gaussian0_func(x, amp8, cen8, sigma8))
    gList = np.add(gList, gaussian0_func(x, amp9, cen9, sigma9))
    gList = np.add(gList, gaussian0_func(x, amp10, cen10, sigma10))
    gList = np.add(gList, gaussian0_func(x, amp11, cen11, sigma11))
    gList = np.add(gList, gaussian0_func(x, amp12, cen12, sigma12))
    gList = np.add(gList, gaussian0_func(x, amp13, cen13, sigma13))
    gList = np.add(gList, gaussian0_func(x, amp14, cen14, sigma14))
    gList = np.add(gList, gaussian0_func(x, amp15, cen15, sigma15))
    gList = np.add(gList, gaussian0_func(x, amp16, cen16, sigma16))
    gList = np.add(gList, gaussian0_func(x, amp17, cen17, sigma17))
    gList = np.add(gList, gaussian0_func(x, amp18, cen18, sigma18))
    gList = np.add(gList, gaussian0_func(x, amp19, cen19, sigma19))
    return gList


def gaussian0_20(x, amp1, cen1, sigma1,
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

    gList = np.array(gaussian0_func(x, amp1, cen1, sigma1))
    gList = np.add(gList, gaussian0_func(x, amp2, cen2, sigma2))
    gList = np.add(gList, gaussian0_func(x, amp3, cen3, sigma3))
    gList = np.add(gList, gaussian0_func(x, amp4, cen4, sigma4))
    gList = np.add(gList, gaussian0_func(x, amp5, cen5, sigma5))
    gList = np.add(gList, gaussian0_func(x, amp6, cen6, sigma6))
    gList = np.add(gList, gaussian0_func(x, amp7, cen7, sigma7))
    gList = np.add(gList, gaussian0_func(x, amp8, cen8, sigma8))
    gList = np.add(gList, gaussian0_func(x, amp9, cen9, sigma9))
    gList = np.add(gList, gaussian0_func(x, amp10, cen10, sigma10))
    gList = np.add(gList, gaussian0_func(x, amp11, cen11, sigma11))
    gList = np.add(gList, gaussian0_func(x, amp12, cen12, sigma12))
    gList = np.add(gList, gaussian0_func(x, amp13, cen13, sigma13))
    gList = np.add(gList, gaussian0_func(x, amp14, cen14, sigma14))
    gList = np.add(gList, gaussian0_func(x, amp15, cen15, sigma15))
    gList = np.add(gList, gaussian0_func(x, amp16, cen16, sigma16))
    gList = np.add(gList, gaussian0_func(x, amp17, cen17, sigma17))
    gList = np.add(gList, gaussian0_func(x, amp18, cen18, sigma18))
    gList = np.add(gList, gaussian0_func(x, amp19, cen19, sigma19))
    gList = np.add(gList, gaussian0_func(x, amp20, cen20, sigma20))

gaussian0FuncList = [gaussian0_func, gaussian0_func, gaussian0_2,  gaussian0_3,  gaussian0_4,  gaussian0_5,  gaussian0_6,  gaussian0_7,
                     gaussian0_8,    gaussian0_9,    gaussian0_10, gaussian0_11, gaussian0_12, gaussian0_13, gaussian0_14, gaussian0_15,
                     gaussian0_16,   gaussian0_17,   gaussian0_18, gaussian0_19, gaussian0_20]
