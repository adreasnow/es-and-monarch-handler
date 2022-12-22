from .newenum import *
class Status(NewEnum):
    queued    = 'queued'
    running   = 'running'
    finished  = 'finished'
    failed    = 'failed'
    timed_out = 'timedout'