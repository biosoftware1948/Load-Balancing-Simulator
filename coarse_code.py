#these are as much intended to flesh out ideas as be the basis for future functional code

#Computer (worker node, created by the node generator)
##Pre-cond: its qualities (Power, memory)
##Post-cond: a complete node which can receive workload units and complete them, logging stats as it goes
Class ComputeNode:
  def __init__(self,cpu,mem):
    self.cpu = cpu #"power" more than actual CPU cycles/time
    self.mem = mem
  def compute():
    
  
#Computer holding class (bag of computers with creation/management funcs)
##Pre-cond: parameters of a number of computers and their qualities
##Post-cond: the computer holding object which contains the specified computers, and a log message 
Class NodeGen:
  def __init__(self,number,qualities): #need to add something to make sure this is formatted correctly
    self.count = number
    self.nodes = set();
    for i in range(number):
      nodes = nodes | ComputeNode(qualities(i).cpu,qualities(i).mem) #I made this a bag but that can obvs change
      
    
#Workload (work, stores the qualities of a job a computer will have to do)
##Pre-cond: job qualities
##Post-cond: object that defines a workload
Class Work:
  def __init__(self,diff,length): #"difficulty" being fraction of 1 time period (turn) to compute 1 unit of length
    self.diff = diff
    self.length = length
    
    
#WorkloadGen (generates work)
##Pre-cond: parameter sets
##Post-cond: work objects produced over the simulation period at 
Class WorkloadGen:
  def __init__(self,parameters):
    #need to add a check for good formatting
    self.parameters = parameters
  
  def generate(): #make some work(s)
  
#Balancer (algorithm implementor)
##Pre-cond: workload generator’s output stream, computer holding object’s input stream, algorithm
##Post-cond: object which runs every turn to allocate work to worker computers, logs actions
Class Balancer:
  def __init__(self,workgen,nodegen,algorithm) #the alg gets passed in here
    self.workgen = workgen
    self.nodes = list()
    for x in nodegen.nodes:
      self.nodes = self.nodes + x
    self.alg = algorithm
    
def core_sim(length,node_params,work_params,alg): 
  #initialize logfile here
  
  node_gen = NodeGen(node_params.num,node_params.qualities)
  #node_gen generates the nodes as it self-constructs
  work_gen = WorkloadGen(work_params)
  balancer = Balancer(node_gen,work_gen,alg)
  
  #loop though the simulation
  for turn in range(length):
    work_gen.generate()
    
    
