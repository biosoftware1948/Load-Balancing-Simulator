import load_balancer
import compute_node
import workload
from wrr import WRRBalancer
from algs.overflow import OverflowLoadBalancer

from load_balancer import Queue

NUM_JOBS = 30#10000
SIM_RUNTIME = 1000#1000
NUM_NODES = 2#10

def run_sim(load_balancer, cluster, jobs):
    load_balancer.assign_cluster(cluster)
    job_queue = Queue()
    for job in jobs.jobs:
        job_queue.enqueue(job)

    
    for current_time in range(0, SIM_RUNTIME):
        while( (not job_queue.isEmpty()) and (job_queue.front().arrival_time <= current_time)): # need to check isEmpty before front()
            #Add jobs to load balancer as they come in
            load_balancer.add_job(job_queue.dequeue())
            #Distribute those jobs now
            #Use below to start testing algos
            load_balancer.run_load_balancing() #should this be run only for each added job, or each time step?
        cluster.do_work()

    #do we set it to end when all the work is done? currently runs until SIM_RUNTIME

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

    print("\nrun random load balancer")
    run_sim(load_balancer.RandomLoadBalancer(NUM_NODES), cluster, jobs)
    print("metrics: ")
    cluster.get_cluster_statistics()
    cluster.reset_metrics()

    print("\nrun Weighted Round robin load balancer")
    run_sim(WRRBalancer(NUM_NODES), cluster, jobs)
    print("metrics: ")
    cluster.get_cluster_statistics()
    cluster.reset_metrics()

    print("\nrun Overflow load balancer")
    run_sim(OverflowLoadBalancer(NUM_NODES), cluster, jobs)
    print("metrics: ")
    cluster.get_cluster_statistics()
    cluster.reset_metrics() 