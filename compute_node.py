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
    def __init__(self, cpu, mem):
        self.__cpu = cpu
        self.__mem = mem

class ComputeNode(object):
    def __init__(self, device_hardware, attributes = None):
        self.state = DeviceState.FREE
        self.device_hardware = device_hardware
        self.attributes = attributes
        
    def assign_job(self):
        self.state = DeviceState.BUSY
    
    def finish_job(self):
        self.state = DeviceState.FREE


class Cluster(object):
    def __init__(self, node_count, homogenous=True):
        self.node_count = node_count
        self.homogenous = homogenous
        self.nodes = []
        self.__createNodes()

    def __createNodes(self):
        if self.homogenous:
            for i in range(0, self.node_count):
                d = DeviceHardware(DEFAULT_CPU, DEFAULT_MEM)
                c = ComputeNode(DeviceHardware)
                self.nodes.append(c)

        else:
            #TODO READ FROM JSON FILE FOR ALL THE NODES
            pass



