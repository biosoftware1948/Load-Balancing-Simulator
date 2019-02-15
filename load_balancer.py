import abc

class LoadBalancer(object):
    def __init__(self, output_interface_count):
        self.__output_interface_count = output_interface_count
        self.__JOB_QUEUE = Queue()
        self.__output_interfaces = [] #list of computing nodes, indexed
        #self.__algorithm = lambda a,b: print("No algorithm, fail")
        
    def __init__(self, output_interface_count,algorithm):
        self.__output_interface_count = output_interface_count
        self.__JOB_QUEUE = Queue()
        self.__output_interfaces = [] #list of computing nodes, indexed
        self.__algorithm = algorithm
        
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
        
    def invoke_algorithm():
        self.__algorithm(self.__JOB_QUEUE,self.__output_interfaces)

    @abc.abstractmethod
    def run_load_balancing(load_balancing_algorithm):
        pass

class Queue(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

