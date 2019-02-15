import random

class job(object):
    def __init__(runtime, arrival_time, mem_reqs = 0, gpu_runtime=0):
        self.runtime = runtime #cycles
        self.arrival_time = arrival_time
        self.mem_reqs = mem_reqs
        self.gpu_runtime = gpu_runtime


def jobFactory(num_jobs, runtime_ceil=100, mem_reqs_ceil=100, runtime_seed=0, mem_seed=0, arrival_time_seed = 0):
    Jobs = []
    
    random.seed(seed)
    for i in range(0, num_jobs):
        runtime = random.randint(1, runtime_ciel)
        memory = random.randint(1, mem_reqs_ceil)
        arrival_time = random.randint(1, arrival_time_seed)
        j = Job(runtime, arrival_time, memory)
        Jobs.append(j)

    return Jobs
    
