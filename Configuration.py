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
    def sim_runtime(self):
        return self.get_property("simulation_config/sim_runtime")

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

    @max_memory.setter
    def max_memory(self, val):
        self.config["jobs_config"]["max_memory"] = val


class ClusterConfig(Config):
    @property
    def num_nodes(self):
        return self.get_property("cluster_config/num_nodes")

    @property
    def homogenous(self):
        return self.get_property("cluster_config/homogenous")

    @property
    def non_homogenous_config(self):
        return self.get_property("cluster_config/non_homogenous_config")

class AlgorithmsConfig(Config):
    @property
    def algorithms(self):
        return self.get_property("algorithms")

class GlobalConfig():
    def __init__(self):
        self.cluster_config = ClusterConfig()
        self.jobs_config= JobsConfig()
        self.simulation_config = SimulationConfig()
        self.algorithms_config = AlgorithmsConfig()







