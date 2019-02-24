# least connection algorithm

# assuming 1 job and entire cluster is sent from load balancer
def leastConnections(job, cluster):
    cur_node = cluster.nodes[0]
    for node in cluster.nodes:
        if node.connections < cur_node.connections:
            least_connected = node.connections

    cur_node.assignjob()
    # assign_job makes the node state = busy, but what is keeping track of how long its busy for?
    # every job has a cycle number, but how will node be aware of that

