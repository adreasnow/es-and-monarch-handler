from .newenum import *
class Energy(NewEnum):    
    @skip
    class Freq(NewEnum):
        zpve  = 'ΔE_ZPVE'
        de    = 'ΔE'
        neg   = '#-ve_freqs' 

    @skip
    class Emission(NewEnum):
        es1ts0  = 'ΔE_s1->s0'
        es1tt1  = 'ΔE_s1->t1'
        es2ts0  = 'ΔE_s2->s0'
        es2ts1  = 'ΔE_s2->s1'
        es2tt1  = 'ΔE_s2->t1'
        es2tt2  = 'ΔE_s2->t2'
        fs1ts0  = 'f_s1->s0'
        fs1tt1  = 'f_s1->t1'
        fs2ts0  = 'f_s2->s0'
        fs2ts1  = 'f_s2->s1'
        fs2tt1  = 'f_s2->t1'
        fs2tt2  = 'f_s2->t2'


    @skip
    class Excitation(NewEnum):
        es0ts1  = 'ΔE_s0->s1'
        es0ts2  = 'ΔE_s0->s2'
        es0ts3  = 'ΔE_s0->s3'
        es0ts4  = 'ΔE_s0->s4'
        es0ts5  = 'ΔE_s0->s5'
        es0ts6  = 'ΔE_s0->s6'
        es0ts7  = 'ΔE_s0->s7'
        es0ts8  = 'ΔE_s0->s8'
        es0ts9  = 'ΔE_s0->s9'
        es0ts10 = 'ΔE_s0->s10'
        fs0ts1  = 'f_s0->s1'
        fs0ts2  = 'f_s0->s2'
        fs0ts3  = 'f_s0->s3'
        fs0ts4  = 'f_s0->s4'
        fs0ts5  = 'f_s0->s5'
        fs0ts6  = 'f_s0->s6'
        fs0ts7  = 'f_s0->s7'
        fs0ts8  = 'f_s0->s8'
        fs0ts9  = 'f_s0->s9'
        fs0ts10 = 'f_s0->s10'

    @skip
    class CASSCF(NewEnum):
        es0ts1  = 'ΔE_s0->s1'
        es0ts2  = 'ΔE_s0->s2'
        es0ts3  = 'ΔE_s0->s3'
        es0ts4  = 'ΔE_s0->s4'
        es0ts5  = 'ΔE_s0->s5'
        es0ts6  = 'ΔE_s0->s6'
        es0ts7  = 'ΔE_s0->s7'
        es0ts8  = 'ΔE_s0->s8'
        es0ts9  = 'ΔE_s0->s9'
        es0ts10 = 'ΔE_s0->s10'
        fs0ts1  = 'f_s0->s1'
        fs0ts2  = 'f_s0->s2'
        fs0ts3  = 'f_s0->s3'
        fs0ts4  = 'f_s0->s4'
        fs0ts5  = 'f_s0->s5'
        fs0ts6  = 'f_s0->s6'
        fs0ts7  = 'f_s0->s7'
        fs0ts8  = 'f_s0->s8'
        fs0ts9  = 'f_s0->s9'
        fs0ts10 = 'f_s0->s10'
        m       = 'M-Diagnostic'
        # occ     = 'Occupations'
