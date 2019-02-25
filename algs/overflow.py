class OverflowLoadBalancer(LoadBalancer):
    def run_load_balancing():
        if not cluster.nodes:
          print("OverflowLoadBalancer(): faulure, no cluster")
          os.flush()
          return true
        if not cluster.nodes[0]:
          print("OverflowLoadBalancer(): faulure, no nodes")
          os.flush()
          return true
        if not cluster.nodes[0].attributes:
          print("OverflowLoadBalancer(): faulure, no attributes")
          os.flush()
          return true
        if not cluster.nodes[0].attributes.priority:
          print("OverflowLoadBalancer(): faulure, no priority attributes")
          os.flush()
          return true
        
        while (True):
            cur_node = cluster.nodes[randint(0,cluster.node_count-1)]
            if cur_node.state == 1:
                cur_node.assign_job()
                # assign_job makes the node state = busy, but what is keeping track of how long its busy for?
                # every job has a cycle number, but how will node be aware of that
                break

