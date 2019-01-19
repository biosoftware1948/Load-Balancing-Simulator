from enum import Enum

class DeviceState(Enum):
    BUSY = 0
    FREE = 1

class ComputeNode(object):
    def __init__(self):
        self.state = DeviceState.FREE
    
    def assign_job(self):
        self.state = DeviceState.BUSY
    
    def finish_job(self):
        self.state = DeviceState.FREE
