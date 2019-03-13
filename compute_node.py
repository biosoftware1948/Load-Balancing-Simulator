from enum import Enum
import random
from load_balancer import Queue
import math

DEFAULT_CPU = 1
DEFAULT_CPU_FLOOR = 1
DEFAULT_MAX_CPU = 6

DEFAULT_MEM = 100
DEFAULT_MEM_FLOOR = 50
DEFAULT_MEM_CIEL = 150

DEBUG = False

class DeviceState(Enum):
    BUSY = 0
    FREE = 1

class DeviceHardware(object):
    def __init__(self, cpu, mem):
        self.cpu = cpu
        self.mem = mem

class ComputeNode(object):
    def __init__(self, device_hardware, attributes = None):
        #self.state = DeviceState.FREE
        self.device_hardware = device_hardware
        #self.job_queue = Queue()
        self.attributes = attributes
        self.reset()

    def is_free(self):
        return self.state == FREE

    def reset(self):
        #job progress
        self.job_queue = Queue()
        self.state = DeviceState.FREE
        self.current_time = -1
        self.current_job = None
        self.progress = 0

        #metrics
        self.started_jobs = 0
        self.completed_jobs = 0
        self.average_response_time = 0
        self.times_became_overloaded = 0
        self.cycles_used = 0
        self.cycles_idle = 0
        self.response_times = []
        self.turnaround_times = []
        
    
    def __str__(self):
        return "ComputeNode: cpu = " + str(self.device_hardware.cpu) + ", mem = "+str(self.device_hardware.mem)

    def assign_job(self, job):
        self.state = DeviceState.BUSY
        self.log("received the job: "+str(job))
        self.job_queue.enqueue(job)

    #do work for one unit of time
    def do_work(self, current_time):
        self.current_time = current_time
        #no current job: start a job from the queue if there is one, otherwise idle
        if self.current_job is None: 
            if self.job_queue.isEmpty():
                self.idle()
                return
            else:
                self.begin_next_job()
        #then work on the current job, whether or not it was just started
        self.work_on_current_job()

    def idle(self):
        #if DEBUG:
            #self.log("idle")
        self.cycles_idle += 1

        #begins the job in self.current_job - or should it take job param?
    def begin_next_job(self):
        self.current_job = self.job_queue.dequeue()
        #self.log("starting job from queue: "+ str(self.current_job))
        arrival = self.current_job.arrival_time
        difference = self.current_time - arrival
        if DEBUG:
            print("beginning job in cycle "+str(self.current_time)+ ": arrival time = "+str(arrival)+", current time = "+str(self.current_time) +", difference = "+str(difference)+", state = "+str(self.state))
        self.response_times.append(difference)
        self.progress = 0 #do we need to specify progress toward what job? not if there's only one current job
        self.started_jobs += 1

    def finish_current_job(self):
        if self.job_queue.isEmpty():
            self.state = DeviceState.FREE #should it be free if there are jobs in the queue?
        arrival = self.current_job.arrival_time
        difference = self.current_time - arrival
        if DEBUG:
            print("finishing job in cycle "+str(self.current_time)+ ": arrival time = "+str(arrival)+", current time = "+str(self.current_time) +", difference = "+str(difference)+", state = "+str(self.state))
        self.turnaround_times.append(self.current_time - arrival)
        self.current_job = None
        self.completed_jobs += 1

    def work_on_current_job(self):
        self.cycles_used += 1
        self.progress += self.device_hardware.cpu
        #self.log("working on job: "+str(self.current_job)+", progress = "+str(self.progress))
        if (self.progress >= self.current_job.runtime):
            self.finish_current_job()

    #could write to a log for each node. or maybe not necessary if we track everything with class variables
    def log(self, message):
        if DEBUG:
            print(message)
        pass

    def get_node_statistics(self):
        average_response_time = "undefined"
        average_turaround_time = "undefined"
        if len(self.response_times) > 0:
            average_response_time = math.floor(sum(self.response_times) / len(self.response_times))
        if len(self.turnaround_times) > 0:    
            average_turaround_time = math.floor(sum(self.turnaround_times) / len(self.turnaround_times))

        returnString = "completed jobs = "+str(self.completed_jobs)
        returnString += ", times overloaded: "+ str(self.times_became_overloaded)
        returnString += ", cycles used: " + str(self.cycles_used)
        returnString += ", cycles idle: " + str(self.cycles_idle)
        if DEBUG:
            returnString += ", response times: " + str(self.response_times)
            returnString += ", turnaround times: " + str(self.turnaround_times)
        returnString += ", avg response: "+str(average_response_time)
        returnString += ", avg turnaround: " + str(average_turaround_time)
        return returnString


class Cluster(object):
    def __init__(self, node_count, homogenous=True):
        self.node_count = node_count
        self.homogenous = homogenous
        self.nodes = []

        # self.overflowed_nodes = 0
        # self.completed_jobs = 0
        # self.time_to_run_all_jobs = 0

        self.__createNodes()

    def get_num_nodes(self):
        return self.node_count

    def get_node(self, index):
        return self.nodes[index]

    def get_cluster_statistics(self):
        pass
        #Here we can print things like
        #Average response time
        #total jobs ran
        #Nodes that got overloaded
        #More stats
        #example:
        print("statistics per node (total nodes = "+str(len(self.nodes))+")")
        for i in range(len(self.nodes)):
            print(str(i)+": "+ self.nodes[i].get_node_statistics())

        total_completed_jobs = sum([node.completed_jobs for node in self.nodes])
        
        #average_response_time = sum([node.average_response_time for node in self.nodes]) / self.node_count
        #average over jobs instead of nodes
        
        average_response_time = "undefined"
        average_turnaround_time = "undefined"

        sum_started = sum ([len(node.response_times) for node in self.nodes]) #could track these separately in nodes
        sum_finished = sum ([len(node.turnaround_times) for node in self.nodes])
        sum_response_time = sum ([sum(node.response_times) for node in self.nodes])
        sum_turnaround_time = sum ([sum(node.turnaround_times) for node in self.nodes])

        if sum_started > 0:
            average_response_time = sum_response_time / sum_started
        if sum_finished > 0:
            average_turnaround_time = sum_turnaround_time / sum_finished
        
        print("\ntotal completed jobs: " + str(total_completed_jobs))
        print("total number of response times recorded: "+str(sum_started))
        print("total number of turnaround times recorded: "+str(sum_finished))
        print("average_response_time: " + str(math.floor(average_response_time)))
        print("average_turnaround_time: " + str(math.floor(average_turnaround_time)))
        #print("average_turnaround_time: " + str((average_turnaround_time)))

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

    def do_work(self, current_time):
        for node in self.nodes:
            node.do_work(current_time)

    def __str__(self):
        output = "Cluster: "
        for node in self.nodes:
            output += "[" + str(node)+"], "
        return output

    def reset(self):
        for node in self.nodes:
            node.reset()