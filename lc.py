# least connection algorithm
#   - alg won't work! it assumes every node has a list property, "connections," that keeps track of the current jobs on node
#   - our current implementation assumes every node has only 1 job, not multiple

# assuming 1 job and entire cluster is sent from load balancer
def leastConnections(job, cluster):
    cur_node = cluster.nodes[0]
    for node in cluster.nodes:
        if len(node.connections) < len(cur_node.connections):
            least_connected = node.connections

    cur_node.assignjob()
    # assign_job makes the node state = busy, but what is keeping track of how long its busy for?
    # every job has a cycle number, but how will node be aware of that

