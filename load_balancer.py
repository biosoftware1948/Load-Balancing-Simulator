import abc

class LoadBalancer(object):
    def __init__(self, output_interface_count):
        self.__output_interface_count = output_interface_count
        self.__JOB_QUEUE = Queue()
        self.__output_interfaces = [] #list of computing nodes, indexed
        #self.__algorithm = lambda a,b: print("No algorithm, fail")
                
    def add_job(self, job):
        self.__JOB_QUEUE.enqueue(job)

    def get_next_job(self):
        return self.__JOB_QUEUE.dequeue()

    def get_job_count(self):
        return self.__JOB_QUEUE.size()

    def add_output_node(self, node):
        self.__output_interfaces.append(node)
    
    def get_output_node(self, node_index):
        return self.__output_interfaces[node_index]

    def assign_job(node_index):
        self.__output_interfaces[node_index].assign_job

    def assign_cluster(self, cluster):
        self.__output_interfaces = cluster.nodes
    
    @abc.abstractmethod
    def run_load_balancing():
        #This should distribute all the jobs in the job_queue until its empty
        pass

class RandomLoadBalancer(LoadBalancer):
    def run_load_balancing(self):
        while (True):
            cur_node = cluster.nodes[randint(0,cluster.node_count-1)]
            if cur_node.state == 1:
                cur_node.assign_job()
                # assign_job makes the node state = busy, but what is keeping track of how long its busy for?
                # every job has a cycle number, but how will node be aware of that
                break

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

