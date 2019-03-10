#this is an alg used when persistence across dropped sesions is necessary
#it chooses a node based off a hash of the client and destination
#this results in every server-client pair being assigned to the same node every time it generates a workload
#the point is persistence, but all that massters to us is that this is effectively an alg that can be "worse than random" for us to compare to

#optionally uses a job attribute called source_dest which is effectively a hash key
class S_D_HashLoadBalancer(LoadBalancer):
    def run_load_balancing():
        attr = true
        #if not cluster:
        #  print("S_D_HashLoadBalancer(): failure, no cluster")
        #  os.flush()
        #  return true
        try:
            self.cluster
        except NameError:
            print("S_D_HashLoadBalancer(): failure, no cluster")
            return true
        #if not cluster.nodes:
        #  print("S_D_HashLoadBalancer(): failure, no nodes")
        #  os.flush()
        #  return true
        try:
            self.cluster.nodes
        except NameError:
            print("S_D_HashLoadBalancer(): failure, no nodes")
            return true
        #if not cluster.nodes[0].attributes:
        #  print("S_D_HashLoadBalancer(): failure, no attributes, using job number as source-dest (this is not worth doing)")
        #  os.flush()
        #  attr = false
        try:
            self.cluster.nodes[0].attributes
        except NameError:
            print("S_D_HashLoadBalancer(): warn, no attributes, using job number as source-dest (this is not worth doing)")
            return true
        #if not cluster.nodes[0].attributes.source_dest:
        #  print("S_D_HashLoadBalancer(): failure, no source-dest attributes, using job number as source-dest (this is not worth doing)")
        #  os.flush()
        #  attr = false
        try:
            self.cluster.nodes[0].attributes.source_dest
        except NameError:
            print("S_D_HashLoadBalancer(): warn, no source-dest attributes, using job number as source-dest (this is not worth doing)")
            return true
        
        if not attr:
          print("using the job object IDs as the source-dest attribute is a bit of a waste of time, as they aren't very random")
          os.flush()
          while not load_balancer.__JOB_QUEUE.empty(): #just modulo the job object IDs onto the node IDs
            j = load_balancer.get_next_job()
            cluster.nodes[id(j) % cluster.node_count].assign_job(j)
        else:
          i = 0
          while not load_balancer.__JOB_QUEUE.empty(): #just modulo the job source_dest attributes onto the node IDs
            j = load_balancer.get_next_job()
            cluster.nodes[j.attributes.source_dest % cluster.node_count].assign_job(j)
