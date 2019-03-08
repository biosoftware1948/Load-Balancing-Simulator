import load_balancer
import compute_node
import workload
from wrr import WRRBalancer
#import algs.overflow

from load_balancer import Queue

NUM_JOBS = 10000
SIM_RUNTIME = 1000
NUM_NODES = 10

def run_sim(load_balancer, cluster, jobs):
    load_balancer.assign_cluster(cluster)
    job_queue = Queue()
    for job in jobs.jobs:
        job_queue.enqueue(job)

    
    for current_time in range(0, SIM_RUNTIME):
        while(job_queue.front().arrival_time <= current_time):
            #Add jobs to load balancer as they come in
            load_balancer.add_job(job_queue.dequeue())
            #Distribute those jobs now
            #Use below to start testing algos
            load_balancer.run_load_balancing()

            #We are gonna need to gather statistics about how the algos performed as well
            #also the algos need to be able to handle busy nodes in the cluster and wait
            #as necessary

if __name__ == "__main__":
    jobs = workload.Jobs()
    jobs.createJobs(NUM_JOBS, SIM_RUNTIME)

    cluster = compute_node.Cluster(NUM_NODES, False) 
    
    print ("PRINTING JOBS")
    jobs.sortByArrival()
    for job in jobs.jobs:
        print ("job arrived at time: {0}, has cpu_load: {1}, mem_requirements: {2}".format(job.arrival_time, job.runtime, job.mem_reqs))
   
    print ("\n\nPRINTING NODES:")

    for i, node in enumerate(cluster.nodes):
        print ("Node {0} has state {1}".format(i, node.state))

    #run_sim(load_balancer.LoadBalancer(NUM_NODES), cluster, jobs)
    #run_sim(load_balancer.RandomLoadBalancer(NUM_NODES), cluster, jobs)
    run_sim(WRRBalancer(NUM_NODES), cluster, jobs)
    #run_sim(OverflowLoadBalancer(NUM_NODES), cluster, jobs)

    

