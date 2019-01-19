from enum import Enum

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
