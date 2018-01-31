# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 12:10:12 2018

@author: yeimy_p
"""



import matlab.engine
import matplotlib.pyplot as plt






class ConnectionMatlab:
    
    
    
    def __init__(self):
        self.data = []
        self.ResultSimulation = {}
        
    
    
    
    def plotResults(self,x,y):     
         plt.figure(1)
         plt.plot(x,y)
         plt.show();
       
        
       
    
    
    def Openconnection(self):         
        eng = matlab.engine.start_matlab()
        ret = eng.sqrt(4.0)        
        if(ret==2.0):
            print('Run connection---Done!', ret)        
            self.eng = eng; 
            
            
            
        
        
    def LoadInputData(self, inputData):
        eng = self.eng 
        cad = "load('"+inputData+"')"
        print (cad)
        eng.eval(cad,nargout=0);
        var =eng.workspace['var']
               
        print ("\n")  
        print("var:__",var)
        print('setInputData---Done!') 
        
        
        
    # simulation 1
    def runSimulation(self,model, times):
    
        print("runSimulation" );    
       
        eng = self.eng   
        eng.eval("sim('"+model+"')");  
        
        StartTime = times["StartTime"];          
        StopTime  = times["StopTime"];         
        N =  len(times["StartTime"])
        
        for n in range(0,N):    
            
            
           cad =cad ="set_param('"+model+"','StartTime','"+ str(StartTime[n])+"', 'StopTime' ,'"+ str(StopTime[n])+"')";        
          
           print ("--",  cad)
           
           # set Parameter 
           eng.eval(cad,nargout=0)
           
           print ("'StartTime:'",  eng.get_param(model,'StartTime') )
           print ("'StopTime:'",  eng.get_param(model,'StopTime') )            
           
           
           # run Simulation 
           eng.eval("sim('"+model+"')");         
           
           var={}
           var=eng.workspace['ScopeData'] 
           print ("ScopeData:", "\n\n:",var) 
        
            
           # run algorithmus
           self.runAlgorithmus(var)
            
           
           print ("\n")  
           
        
    def runAlgorithmus(self,var):
        x = var['time']
        y = var['signals']['values']
        #print ('ScopeData: ', var,"\n\n")   
        self.plotResults(x,y) 
        
        
           
     # simulation 2  with input data     
    def runSimulationInput(self,model):           
        eng = self.eng  
        eng.eval("sim('"+model+"')");
        
        
        var =eng.workspace['ScopeData']
        x = var['time']
        y = var['signals']['values']
        self.plotResults(x,y) 
    
    
   
    
    def CloseConnection(self):         
        self.eng.quit()
        print('Close connection---Done!')        
           
            
    
 
   
    



























































