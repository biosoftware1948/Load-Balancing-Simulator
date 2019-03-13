import load_balancer
import compute_node
import workload
#from algs.wrr import WRRBalancer
#from algs.overflow import OverflowLoadBalancer
#from algs.source_dest_hash import S_D_HashLoadBalancer
from load_balancer import Queue
import lc
import wrr
import source_dest_hash
from Configuration import GlobalConfig
import sys

DEBUG = True

def pretty_box_print(name):
    print_width = 80
    box = "#" * print_width
    print ("\n" + box)
    algo_string = "running algorithm " + name
    print ("#" + algo_string.center(print_width-2, ' ') + "#")
    print (box + "\n")

def run_sim(load_balancer, cluster, jobs, runtime):
    load_balancer.assign_cluster(cluster)
    job_queue = Queue()
    for job in jobs.jobs:
        job_queue.enqueue(job)
    
    for current_time in range(0, runtime):
        while( (not job_queue.isEmpty()) and (job_queue.front().arrival_time <= current_time)): # need to check isEmpty before front()
            #Add jobs to load balancer as they come in
            load_balancer.add_job(job_queue.dequeue())
            #Distribute those jobs now
            #Use below to start testing algos
            load_balancer.run_load_balancing() #should this be run only for each added job, or each time step?
        cluster.do_work(current_time)

    #do we set it to end when all the work is done? currently runs until SIM_RUNTIME

            #We are gonna need to gather statistics about how the algos performed as well
            #also the algos need to be able to handle busy nodes in the cluster and wait
            #as necessary

if __name__ == "__main__":
    config = GlobalConfig()

    jobs = workload.Jobs()
    jobs.createJobs(config.jobs_config.num_jobs, config.simulation_config.runtime, config.jobs_config.max_runtime, config.jobs_config.max_memory)
    jobs.sortByArrival()
    
    cluster = compute_node.Cluster(config.cluster_config.num_nodes, config.cluster_config.homogenous) 
    
    if (config.jobs_config.print_jobs):
        pretty_box_print("PRINTING JOBS")
        for job in jobs.jobs:
            print ("job arrived at time: {0}, has cpu_load: {1}, mem_requirements: {2}".format(job.arrival_time, job.runtime, job.mem_reqs))
    if(config.cluster_config.print_cluster):
        pretty_box_print("PRINTING NODES")
        for i, node in enumerate(cluster.nodes):
            print ("Node {0} has state {1}".format(i, node.state))


    for i, algo in enumerate(config.algorithms_config.algorithms):
        pretty_box_print(algo["class_name"])
        load_balancer_ = getattr(globals()[algo["file_name"]], str(algo["class_name"]))
        load_balancer_instance = load_balancer_(config.cluster_config.num_nodes)
        try:
            run_sim(load_balancer_instance, cluster, jobs, config.simulation_config.runtime)
            print("metrics: ")
            cluster.get_cluster_statistics()
            cluster.reset()
        except Exception as e:
            #catch the error with this algo and keep going 
            #regardless
            if DEBUG:
                raise
            pass