from load_balancer import LoadBalancer
from compute_node import ComputeNode
from compute_node import DeviceHardware

class OverflowLoadBalancer(LoadBalancer):
    def run_load_balancing(self):
        attr = True
        #if not self.cluster:
        #  print("OverflowLoadBalancer(): failure, no cluster")
        #  #os.flush()
        #  return true
        try:
            self.cluster
        except NameError:
            print("OverflowLoadBalancer(): failure, no cluster")
            return true
        #if not self.cluster.nodes:
        #  print("OverflowLoadBalancer(): failure, no nodes")
        #  #os.flush()
        #  return True
        try:
            self.cluster.nodes
        except NameError:
            print("OverflowLoadBalancer(): failure, no nodes")
            return true
        #if not self.cluster.nodes[0].attributes:
        #  print("OverflowLoadBalancer(): failure, no attributes, using node order as priority")
        #  #os.flush()
        #  attr = False
        try:
            self.cluster.nodes[0].attributes
        except NameError:
            print("OverflowLoadBalancer(): warn, no attributes, using node order as priority")
            attr = False
        #if not self.cluster.nodes[0].attributes.priority:
        #  print("OverflowLoadBalancer(): failure, no priority attributes, using node order as priority")
        #  #os.flush()
        #  attr = False
        try:
            self.cluster.nodes[0].attributes.priority
        except NameError:
            print("OverflowLoadBalancer(): warn, no priority attributes, using node order as priority")
            attr = False        
        
        if not attr:
          while (True):
            for cur_node in self.cluster.nodes:
              if cur_node.state == 1:
                cur_node.assign_job(load_balancer.get_next_job())
                # assign_job makes the node state = busy, but what is keeping track of how long its busy for?
                # every job has a cycle number, but how will node be aware of that
                break
        else:
          while (True):
            for cur_node in sorted(self.cluster.nodes, key = attributes.priority):
               if cur_node.state == 1:
                cur_node.assign_job(load_balancer.get_next_job())
                # assign_job makes the node state = busy, but what is keeping track of how long its busy for?
                # every job has a cycle number, but how will node be aware of that
                break
