from .newenum import NewEnum, skip


class TDDFT(NewEnum):

    @skip
    class Triplets(NewEnum):
        on = 'on'
        off = 'off'

    @skip
    class TDA(NewEnum):
        on = 'on'
        off = 'off'
        fitting = 'fitting'

    none = 'none'
    tddft = 'tddft'
