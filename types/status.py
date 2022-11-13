from .newenum import *
class Status(NewEnum):
    @skip
    class Crest(NewEnum):
        queued   = auto()
        running  = auto()
        finished = auto()
        failed   = auto()

    class initOrca(NewEnum):
        queued   = auto()
        running  = auto()
        finished = auto()
        failed   = auto()
        
    class SMD(NewEnum):
        queued   = auto()
        running  = auto()
        finished = auto()
        failed   = auto()

    class CASSCF(NewEnum):
        queued   = auto()
        running  = auto()
        finished = auto()
        failed   = auto()