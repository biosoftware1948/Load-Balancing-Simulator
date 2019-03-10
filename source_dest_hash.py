#this is an alg used when persistence across dropped sesions is necessary
#it chooses a node based off a hash of the client and destination
#this results in every server-client pair being assigned to the same node every time it generates a workload
#the point is persistence, but all that massters to us is that this is effectively an alg that can be "worse than random" for us to compare to

#optionally uses a job attribute called source_dest which is effectively a hash key
from load_balancer import LoadBalancer
from compute_node import ComputeNode
from compute_node import DeviceHardware

class S_D_HashLoadBalancer(LoadBalancer):
    def run_load_balancing(self):
        attr = True
        if not self.cluster:
          print("S_D_HashLoadBalancer(): failure, no cluster")
          #os.flush()
          return True
        if not self.cluster.nodes:
          print("S_D_HashLoadBalancer(): failure, no nodes")
          #os.flush()
          return True
        if not self.cluster.nodes[0].attributes:
          print("S_D_HashLoadBalancer(): failure, no attributes, using job number as source-dest (this is not worth doing)")
          #os.flush()
          attr = False
        if not self.cluster.nodes[0].attributes.source_dest:
          print("S_D_HashLoadBalancer(): failure, no source-dest attributes, using job number as source-dest (this is not worth doing)")
          #os.flush()
          attr = False
        
        
        if not attr:
          print("using the job object IDs as the source-dest attribute is a bit of a waste of time, as they aren't very random")
          #os.flush()
          while not load_balancer.__JOB_QUEUE.empty(): #just modulo the job object IDs onto the node IDs
            j = load_balancer.get_next_job()
            self.cluster.nodes[id(j) % cluster.node_count].assign_job(j)
        else:
          i = 0
          while not load_balancer.__JOB_QUEUE.empty(): #just modulo the job source_dest attributes onto the node IDs
            j = load_balancer.get_next_job()
            self.cluster.nodes[j.attributes.source_dest % cluster.node_count].assign_job(j)
