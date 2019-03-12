from load_balancer import LoadBalancer
from compute_node import ComputeNode
from compute_node import DeviceHardware

# least connection algorithm
#   - checks to find the first free node that has the best CPU power
DEBUG = True

class LeastConnectionsCPUBalancer(LoadBalancer):

    def run_load_balancing(self):
        while (not self.JOB_QUEUE.isEmpty()):
            emptyNodes = [i for i in range(self.cluster.get_num_nodes()) if self.cluster.get_node(i).is_free]
            
            if len(emptyNodes) == 0:
                if DEBUG:
                    print("no nodes available, waiting")
                return  #no free node - wait for one to be free

            index = emptyNodes[0]
            for tempIndex in emptyNodes:
                if self.cluster.get_node(index).device_hardware.cpu < self.cluster.get_node(tempIndex).device_hardware.cpu:
                    index = tempIndex
        
            job = self.get_next_job()
            self.assign_job(index, job)


