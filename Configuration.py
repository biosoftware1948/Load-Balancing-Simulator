import json

class Config(object):
    def __init__(self):
        self.config = None

    def __load_json(self):
        with open("config.json") as f:
            self.config =  json.load(f)

    def get_property(self, property_name):
        if self.config == None:
            self.__load_json()

        key_list = property_name.split("/")

        val = self.config
        for key in key_list:
            try:
                val = val[key]
            except KeyError:
                return None
        return val


class SimulationConfig(Config):
    @property
    def runtime(self):
        return self.get_property("simulation_config/sim_runtime")

    def print_properties(self):
        print("sim_runtime: "+str(self.runtime))

class JobsConfig(Config):
    @property
    def num_jobs(self):
        return self.get_property("jobs_config/num_jobs")

    @property
    def max_runtime(self):
        return self.get_property("jobs_config/max_runtime")

    @property
    def max_memory(self):
        return self.get_property("jobs_config/max_memory")

    @property
    def print_jobs(self):
        return self.get_property("jobs_config/print_jobs")

    @max_memory.setter
    def max_memory(self, val):
        self.config["jobs_config"]["max_memory"] = val

    def print_properties(self):
        print("num_jobs: "+str(self.num_jobs)+", max_runtime: "+str(self.max_runtime)+", max_memory: "+str(self.max_memory)+", print_jobs: "+str(self.print_jobs))

class ClusterConfig(Config):
    @property
    def num_nodes(self):
        return self.get_property("cluster_config/num_nodes")

    @property
    def homogenous(self):
        return self.get_property("cluster_config/homogenous")

    @property
    def config_type(self):  #name for a specific pre-written config to use
        return self.get_property("cluster_config/config_type")

    @property
    def non_homogenous_config(self):
        return self.get_property("cluster_config/non_homogenous_config")

    @property
    def print_cluster(self):
        return self.get_property("cluster_config/print_cluster")

    def print_properties(self):
        print("num_nodes: "+str(self.num_nodes)+", homogenous: "+str(self.homogenous))

class AlgorithmsConfig(Config):
    @property
    def algorithms(self):
        return self.get_property("algorithms")

    def print_properties(self):
        print("algorithms"+str(self.algorithms))

class GlobalConfig():
    def __init__(self):
        self.cluster_config = ClusterConfig()
        self.jobs_config= JobsConfig()
        self.simulation_config = SimulationConfig()
        self.algorithms_config = AlgorithmsConfig()







