from dataclasses import dataclass
from .newenum import NewEnum


class slurmStatus(NewEnum):
    PENDING    = 'pending'
    RUNNING    = 'running'
    COMPLETING = 'completing'
    FAILED     = 'failed'
    TIMED_OUT  = 'timedout'
    NONE       = 'none'


@dataclass
class slurmJob():
    SlurmID: int
    jobName: str
    status: slurmStatus

    def __str__(self):
        return self.jobName

    def __repr__(self):
        return self.jobName
