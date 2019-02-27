from enum import Enum
from load_balancer import Queue

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
        self.job_queue = Queue()
        self.attributes = attributes

        self.completed_jobs = 0
        self.average_response_time = 0
        self.times_became_overloaded = 0
        
    def assign_job(self):
        self.state = DeviceState.BUSY
    
    def finish_job(self):
        self.state = DeviceState.FREE

class Cluster(object):
    def __init__(self, node_count, homogenous=True):
        self.node_count = node_count
        self.homogenous = homogenous
        self.nodes = []

        self.overflowed_nodes = 0
        self.completed_jobs = 0
        self.time_to_run_all_jobs = 0

        self.__createNodes()

    def get_cluster_statistics(self):
        pass
        #Here we can print things like
        #Average response time
        #total jobs ran
        #Nodes that got overloaded
        #More stats
        #example:
        total_completed_jobs = sum([node.completed_jobs for node in self.nodes])
        average_response_time = sum([node.average_response_time for node in self.nodes]) / self.node_count

    def __createNodes(self):
        if self.homogenous:
            for i in range(0, self.node_count):
                d = DeviceHardware(DEFAULT_CPU, DEFAULT_MEM)
                c = ComputeNode(DeviceHardware)
                self.nodes.append(c)

        else:
            #TODO READ FROM JSON FILE FOR ALL THE NODES
            pass




