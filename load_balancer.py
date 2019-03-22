import abc
import random

DEBUG = True

class LoadBalancer(object):
    def __init__(self, output_interface_count):
        self.__output_interface_count = output_interface_count
        self.JOB_QUEUE = Queue()
        self.output_interfaces = [] #list of computing nodes, indexed
        #self.__algorithm = lambda a,b: print("No algorithm, fail")
                
    def add_job(self, job):
        self.JOB_QUEUE.enqueue(job)

    def get_next_job(self):
        return self.JOB_QUEUE.dequeue()

    def get_job_count(self):
        return self.JOB_QUEUE.size()

    def add_output_node(self, node):
        self.__output_interfaces.append(node)
    
    def get_output_node(self, node_index):
        return self.__output_interfaces[node_index]

    def assign_job(self, node_index, job):
        self.__output_interfaces[node_index].assign_job(job)

    def assign_cluster(self, cluster):
        self.cluster = cluster
        self.__output_interfaces = cluster.nodes
                
    def invoke_algorithm():
        self.__algorithm(self.JOB_QUEUE,self.__output_interfaces)

    @abc.abstractmethod
    def run_load_balancing(self):
        #This should distribute all the jobs in the job_queue until its empty
        pass

class RandomLoadBalancer(LoadBalancer):
    def run_load_balancing(self):
        while (not self.JOB_QUEUE.isEmpty()):
            index = random.randint(0, self.cluster.get_num_nodes()-1)      
            job = self.get_next_job()
            self.assign_job(index, job)

            #cur_node = self.cluster.get_node(index)
            # if cur_node.state == 1:
            #     cur_node.assign_job()
            #     # assign_job makes the node state = busy, but what is keeping track of how long its busy for?
            #     # every job has a cycle number, but how will node be aware of that
            #     break

#like random, but will not assign to a busy node. if all nodes busy, it will just wait
class RandomFreeLoadBalancer(LoadBalancer):
    def run_load_balancing(self):
        while (not self.JOB_QUEUE.isEmpty()):
            emptyNodes = [i for i in range(self.cluster.get_num_nodes()) if self.cluster.get_node(i).is_free]
            if len(emptyNodes) == 0:
                if DEBUG:
                    print("no nodes available, waiting")
                return  #no free node - wait for one to be free
            index = random.choice(emptyNodes)      
            job = self.get_next_job()
            self.assign_job(index, job)

#Round Robin Algorithm. Still have to check for busy nodes and assign accordingly          
class RoundRobinLoadBalancer(LoadBalancer):

    def assign_cluster(self, cluster): 
        self.cluster = cluster
        self.__output_interfaces = cluster.nodes
        self.num_nodes = len(self.__output_interfaces)

        self.counter = 0

    def run_load_balancing(self):
        curr_node = self.__output_interfaces[self.counter]
        job = self.get_next_job()
        curr_node.assign_job(job)
        self.increment_counter()

    def increment_counter(self):
        self.counter += 1
        if self.counter >= self.num_nodes:
            self.counter = 0


class Queue(object):
    def __init__(self):
        self.items = []

    def front(self):
        return self.items[-1]

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

