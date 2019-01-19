# Load-Balancing-Simulator

















#   Classes (rough)</br>
#Balancer (algorithm implementor) </br>
##Pre-cond: workload generator’s output stream, computer holding object’s input stream, algorithm </br>
##Post-cond: object which runs every turn to allocate work to worker computers, logs actions</br>
#Computer (worker node)</br>
##Pre-cond: its qualities (Power, memory)</br>
##Post-cond: a complete node which can receive workload units and complete them, logging stats as it goes</br>
#Workload (work, stores the qualities of a job a computer will have to do)</br>
##Pre-cond: job qualities</br>
##Post-cond: object that defines a workload</br>
#WorkloadGen (generates work)</br>
##Pre-cond: parameter sets</br>
##Post-cond: work objects produced over the simulation period at </br>
#Computer holding class (bag of computers with creation/management funcs) </br>
##Pre-cond: parameters of a number of computers and their qualities</br>
##Post-cond: the computer holding object which contains the specified computers, and a log message</br>

#   Roughest pseudocode:</br>
#PARSE/GEN PARAMETERS</br>
#SIM START</br>
##GENERATE WORKER BAG</br>
##GENERATE WORKERS</br>
##GENERATE WORKLOADGEN</br>
##GENERATE BALANCER</br>
#    
##TURN LOOP</br>
###WORKLOADGEN OBJECT INVOKED, GENERATES WORK, SENDS TO BALANCER</br>
###BALANCER SENDS WORK TO WORKER NODES</br>
###WORKER NODES COMPLETE AS MUCH OF THEIR TOTAL ALLOCATED WORK AS CAPABLE</br>
##TURN LOOP END</br></br>
#    
##CLEAN UP</br>
#SIM END</br>
