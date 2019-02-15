import load_balancer
import compute_node
import workload


if __name__ == "__main__":
    NUM_JOBS = 100
    jobs = workload.Jobs()
    jobs.createJobs(NUM_JOBS)
    #jobs.sortByArrival()

    NUM_NODES = 10
    cluster = compute_node.Cluster(NUM_NODES) 
    
    print "PRINTING JOBS"
    for i, job in enumerate(jobs.jobs):
        print "job number {0}, arrived at {1}, has cpu_load: {2}".format(i, job.arrival_time, job.runtime)
   

    print "\n\nPRINTING NODES:"
    for i, node in enumerate(cluster.nodes):
        print "Node {0} has state {1}".format(i, node.state)
    

