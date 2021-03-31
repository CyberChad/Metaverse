#################### ham cheese production model ###################

# this is the simplest type of act-r model
# it uses only the production system and one buffer
# the buffer represents the focus of thought
# we call it the focus buffer but it is often called the task buffer
# productions fire if they match the focus buffer
# each production changes the contents of focus buffer so a different production will fire on the next cycle


import ccm      
log=ccm.log()   

from ccm.lib.actr import *  

class MyEnvironment(ccm.Model):
    something=ccm.Model(isa='something',state='not_done')


class MyAgent(ACTR):

    focus=Buffer()
    DMbuffer=Buffer() 

    DM=Memory(DMbuffer,threshold=0,maximum_time=20,finst_size=50,finst_time=1000) # latency controls the relationship between activation and recall
        
    DMNoise(DM,noise=0.0)
    DMBaseLevel(DM,decay=0.5)  

    focus.set('task:sandwich object:bread_bottom')
    
    DM.add('condiment:mustard ordered:yes')
##    DM.add('condiment:ketchup ordered:yes')
##    DM.add('condiment:mayonaise ordered:no')
##    DM.add('condiment:siracha ordered:yes')

    def bread_bottom(focus='task:sandwich object:bread_bottom'):
        print("I have a piece of bread") 
        focus.set('task:sandwich object:cheese')

    def cheese(focus='task:sandwich object:cheese'):          
        print("I have put cheese on the bread")      
        focus.set('task:sandwich object:ham')

    def ham(focus='task:sandwich object:ham'):
        print("I have put  ham on the cheese")
        focus.set('task:sandwich object:condiment') ###

    def condiment_DM_request(focus='task:sandwich object:condiment'):
        print("recalling the condiment")
        DM.request('condiment:?condiment')
        focus.set('task:recall') 

    def DM_retrieve(focus='task:recall',DMbuffer='condiment:?condiment ordered:?ordered'): 
        print("I recall.......")                            
        print(condiment)
        print("is a ....")
        print(ordered)
        DMbuffer.set('state:empty')
        focus.set('task:sandwich object:condiment')

    def forgot(focus='task:recall', DM='error:True',DMbuffer=None):
        print("I recall they wanted.......")
        print ("I got nothing")
        focus.set('task:sandwich object:bread_top')

    def bread_top(focus='task:sandwich object:bread_top'): ###
        print("I have put bread on the ham")
        print("I have made a ham and cheese sandwich")
        focus.set('task:sandwich object:none')


tim=MyAgent()                              # name the agent
subway=MyEnvironment()                     # name the environment
subway.agent=tim                           # put the agent in the environment
ccm.log_everything(subway)                 # print out what happens in the environment

subway.run()                               # run the environment
ccm.finished()                             # stop the environment
