from enum import Enum
import random
from load_balancer import Queue

DEFAULT_CPU = 1
DEFAULT_CPU_FLOOR = 1
DEFAULT_MAX_CPU = 6

DEFAULT_MEM = 100
DEFAULT_MEM_FLOOR = 50
DEFAULT_MEM_CIEL = 150

class DeviceState(Enum):
    BUSY = 0
    FREE = 1

class DeviceHardware(object):
    def __init__(self, cpu, mem):
        self.cpu = cpu
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
        self.cycles_idle = 0

        self.current_job = None
        self.progress = 0
    
    def __str__(self):
        return "ComputeNode: cpu = " + str(self.device_hardware.cpu) + ", mem = "+str(self.device_hardware.mem)

    def assign_job(self, job):
        #self.state = DeviceState.BUSY
        self.log("node was assigned the job: "+str(job))
        self.job_queue.enqueue(job)

    #def begin_next_job(self, job)

    def finish_job(self, job):
        #self.state = DeviceState.FREE
        self.current_job = None
        self.completed_jobs += 1

    #do work for one unit of time
    def do_work(self):
        #no current job: start a job from the queue if there is one, otherwise idle
        if self.current_job is None: 
            if self.job_queue.isEmpty():
                self.idle()
                return
            else:
                self.current_job = self.job_queue.dequeue()
                self.log("starting job from queue: "+ str(self.current_job))
                self.progress = 0 #do we need to specify progress toward what job? not if there's only one current job
        #then work on the job - more cpu means it works faster. ignore mem requirements for now
        self.progress += self.device_hardware.cpu
        if (self.progress >= self.current_job.runtime):
            self.finish_job(current_job)

    def idle():
        self.log("idle")
        self.cycles_idle += 1

    #could write to a log for each node. or maybe not necessary if we track everything with class variables
    def log(self, message):
        print(message)
        pass


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
        print("total completed jobs: " + str(total_completed_jobs))
        print("average_response_time: " + str(average_response_time))

    def __createNodes(self):
        if self.homogenous:
            for i in range(0, self.node_count):
                d = DeviceHardware(DEFAULT_CPU, DEFAULT_MEM)
                c = ComputeNode(d)
                self.nodes.append(c)

        else:
            #TODO READ FROM JSON FILE FOR ALL THE NODES
            #for now, do random values
            for i in range(0, self.node_count):
                cpu = random.randint(DEFAULT_CPU_FLOOR, DEFAULT_MAX_CPU)
                mem = random.randint(DEFAULT_MEM_FLOOR, DEFAULT_MEM_CIEL)
                d = DeviceHardware(cpu, mem)
                c = ComputeNode(d)
                self.nodes.append(c)
            pass

    def do_work(self):
        for node in self.nodes:
            node.do_work()




