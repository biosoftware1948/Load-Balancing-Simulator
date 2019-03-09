import random

class job(object):
    def __init__(self, runtime, arrival_time, mem_reqs = 0, gpu_runtime=0):
        self.runtime = runtime #cycles
        self.arrival_time = arrival_time
        self.mem_reqs = mem_reqs
        self.gpu_runtime = gpu_runtime

    def __str__(self):
        return "Job: runtime = "+str(self.runtime)+", arrived: "+str(self.arrival_time)+", mem: " +str(self.mem_reqs) + "gpu "+str(self.gpu_runtime)


class Jobs(object):
    def __init__(self):
        self.jobs = []

    def sortByArrival(self):
        self.jobs.sort(key=lambda x: x.arrival_time)

    def sortByRuntime(self):
        self.jobs.sort(key=lambda x: x.runtime)

    def sortByMem(self):
        self.jobs.sort(key=lambda x: x.mem_reqs)

    def createJobs(self, num_jobs, arrival_time_ciel=100, runtime_ceil=100, mem_reqs_ceil=100,runtime_seed=0, mem_seed=0, arrival_time_seed = 0):
        random.seed(0)
        for i in range(0, num_jobs):
            runtime = random.randint(1, runtime_ceil)
            memory = random.randint(1, mem_reqs_ceil)
            arrival_time = random.randint(1, arrival_time_ciel)
            j = job(runtime, arrival_time, memory)
            self.jobs.append(j)

    
