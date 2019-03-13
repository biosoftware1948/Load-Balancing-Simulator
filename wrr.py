# weighted round robin
from load_balancer import LoadBalancer
from compute_node import ComputeNode
from compute_node import DeviceHardware

MAX_CYCLE = 100
CARE_IF_BUSY = True

class WRRBalancer(LoadBalancer):

    #set the ratio when we get the clusters, according to cpu
    def assign_cluster(self, cluster):
         #can I make this a constant?
        self.cluster = cluster
        self.__output_interfaces = cluster.nodes
        self.total = 0
        self.num_nodes = len(self.__output_interfaces)
        self.weights = []
        for node in cluster.nodes:
            cpu = node.device_hardware.cpu
            self.total += cpu
            self.weights.append(cpu)

        #scale the maximum cycle size to maximum total cycles
        if (self.total >= MAX_CYCLE):
            print("adjusting down to max cycles")
            for i in range(len(self.weights)):
                self.weights[i] = self.weights[i] * (self.total / MAX_CYCLE)
            self.total = MAX_CYCLE

        self.small_counter = 0
        self.large_counter = 0

        print("assigning cluster in WRRBalancer")
        print("cluster: "+str(self.cluster))
        print("wrr total cpu= "+str(self.total))
        print("wrr weights"+str(self.weights))

    def run_load_balancing(self):
        curr_node = self.__output_interfaces[self.large_counter]
        job = self.get_next_job() #some algs could pick from a different position in the queue
        curr_node.assign_job(job)
        #self.assign_job(self.large_counter, job)
        #print("wrr.run_load_balancing: assigned" +str(job)+ "to node "+str(self.large_counter))
        self.increment_small()
    
    def increment_small(self):
        self.small_counter += 1
        if (self.small_counter >= self.weights[self.large_counter]):
            self.small_counter = 0
            self.increment_large()

    def increment_large(self):
        self.large_counter += 1
        if self.large_counter >= self.num_nodes:
            self.large_counter = 0