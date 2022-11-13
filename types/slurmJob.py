from dataclasses import dataclass
from .newenum import NewEnum, auto

class slurmStatus(NewEnum):
    PENDING = auto()
    RUNNING = auto()
    COMPLETING = auto()
    FAILED = auto()
    NONE = auto()

@dataclass
class slurmJob():
    SlurmID: int
    jobName: str
    status: slurmStatus

    def __str__(self):
        return self.jobName

    def __repr__(self):
        return self.jobName

