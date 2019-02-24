# random algorithm
from random import randint

# assuming 1 job and entire cluster is sent from load balancer
def random(job, cluster):
    while (True):
        cur_node = cluster.nodes[randint(0,cluster.node_count-1)]
        if cur_node.state == 1:
            cur_node.assign_job
            # assign_job makes the node state = busy, but what is keeping track of how long its busy for?
            # every job has a cycle number, but how will node be aware of that
            break
