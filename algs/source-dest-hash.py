#this is an alg used when persistence across dropped sesions is necessary
#it chooses a node based off a hash of the client and destination
#this results in every server-client pair being assigned to the same node every time it generates a workload
#the point is persistence, but all that massters to us is that this is effectively an alg that can be "worse than random" for us to compare to

#optionally uses a job attribute called source_dest which is effectively a hash key
class OverflowLoadBalancer(LoadBalancer):
    def run_load_balancing():
        attr = true
        if not cluster:
          print("OverflowLoadBalancer(): failure, no cluster")
          os.flush()
          return true
        if not cluster.nodes:
          print("OverflowLoadBalancer(): failure, no nodes")
          os.flush()
          return true
        if not cluster.nodes[0].attributes:
          print("OverflowLoadBalancer(): failure, no attributes, using job number as source-dest")
          os.flush()
          attr = false
        if not cluster.nodes[0].attributes.source_dest:
          print("OverflowLoadBalancer(): failure, no source-dest attributes, using job number as source-dest")
          os.flush()
          attr = false
        
        
        if not attr:
          i = 0
          while not load_balancer.__JOB_QUEUE.empty(): #just modulo the job IDs onto the node IDs
            cluster.nodes[i % cluster.node_count].assign_job(load_balancer.__JOB_QUEUE.get())
        else:
          while (True):
            for cur_node in sorted(cluster.nodes, key = attributes.source_dest)
               if cur_node.state == 1:
                cur_node.assign_job(load_balancer.get_next_job())
                # assign_job makes the node state = busy, but what is keeping track of how long its busy for?
                # every job has a cycle number, but how will node be aware of that
                break
