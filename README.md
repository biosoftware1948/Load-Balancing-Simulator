# Load-Balancing-Simulator

















#   Classes (rough)
#Balancer (algorithm implementor)
##Pre-cond: workload generator’s output stream, computer holding object’s input stream, algorithm
##Post-cond: object which runs every turn to allocate work to worker computers, logs actions
#Computer (worker node)
##Pre-cond: its qualities (Power, memory)
##Post-cond: a complete node which can receive workload units and complete them, logging stats as it goes
#Workload (work, stores the qualities of a job a computer will have to do)
##Pre-cond: job qualities
##Post-cond: object that defines a workload
#WorkloadGen (generates work)
##Pre-cond: parameter sets
##Post-cond: work objects produced over the simulation period at 
#Computer holding class (bag of computers with creation/management funcs) 
##Pre-cond: parameters of a number of computers and their qualities
##Post-cond: the computer holding object which contains the specified computers, and a log message

#   Roughest pseudocode:
#PARSE/GEN PARAMETERS
#SIM START
##GENERATE WORKER BAG
##GENERATE WORKERS
##GENERATE WORKLOADGEN
##GENERATE BALANCER
#    
##TURN LOOP
###WORKLOADGEN OBJECT INVOKED, GENERATES WORK, SENDS TO BALANCER
###BALANCER SENDS WORK TO WORKER NODES
###WORKER NODES COMPLETE AS MUCH OF THEIR TOTAL ALLOCATED WORK AS CAPABLE
##TURN LOOP END
#    
##CLEAN UP
#SIM END
