



#Computer (worker node)
##Pre-cond: its qualities (Power, memory)
##Post-cond: a complete node which can receive workload units and complete them, logging stats as it goe
Class ComputeNode:
  def __init__(self):
  
#Computer holding class (bag of computers with creation/management funcs)
##Pre-cond: parameters of a number of computers and their qualities
##Post-cond: the computer holding object which contains the specified computers, and a log message 
Class NodeBag:
  def __init__(self):
    
    
    
#Workload (work, stores the qualities of a job a computer will have to do)
##Pre-cond: job qualities
##Post-cond: object that defines a workload
Class Work:
  def __init__(self):
    
    
    
#WorkloadGen (generates work)
##Pre-cond: parameter sets
##Post-cond: work objects produced over the simulation period at 
Class WorkloadGen:
  def __init__(self):
  
#Balancer (algorithm implementor)
##Pre-cond: workload generator’s output stream, computer holding object’s input stream, algorithm
##Post-cond: object which runs every turn to allocate work to worker computers, logs actions
Class Balancer:
  def __init__(self):
