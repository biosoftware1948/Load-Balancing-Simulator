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
          print("OverflowLoadBalancer(): failure, no attributes, using node order as priority")
          os.flush()
          attr = false
        if not cluster.nodes[0].attributes.priority:
          print("OverflowLoadBalancer(): failure, no priority attributes, using node order as priority")
          os.flush()
          attr = false
        
        
        if not attr:
          while (True):
            for cur_node in cluster.nodes
              if cur_node.state == 1:
                cur_node.assign_job()
                # assign_job makes the node state = busy, but what is keeping track of how long its busy for?
                # every job has a cycle number, but how will node be aware of that
                break
        else:
          while (True):
            for cur_node in sorted(cluster.nodes, key = attributes.priority)
               if cur_node.state == 1:
                cur_node.assign_job()
                # assign_job makes the node state = busy, but what is keeping track of how long its busy for?
                # every job has a cycle number, but how will node be aware of that
                break
