from enum import Enum

DEFAULT_CPU = 1
DEFAULT_MAX_CPU = 6


DEFAULT_MEM = 100
DEFAULT_MEM_FLOOR = 50
DEFAULT_MEM_CIEL = 150


class DeviceState(Enum):
    BUSY = 0
    FREE = 1

class DeviceHardware(object):
    def __init__(cpu, mem):
        self.__cpu = cpu
        self.__mem = mem

class ComputeNode(object):
    def __init__(self, device_hardware):
        self.state = DeviceState.FREE
        self.device_hardware = device_hardware
        
    def assign_job(self):
        self.state = DeviceState.BUSY
    
    def finish_job(self):
        self.state = DeviceState.FREE


def ComputeNodeFactory(num_nodes, homogenous=1):

