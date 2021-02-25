#################### ham cheese production model ###################

# this is the simplest type of act-r model
# it uses only the production system and one buffer
# the buffer represents the focus of thought
# we call it the focus buffer but it is often called the goal buffer
# productions fire if they match the focus buffer
# each production changes the contents of focus buffer so a different production will fire on the next cycle


import ccm      
log=ccm.log()   

from ccm.lib.actr import *  

#####
# Python ACT-R requires an environment
# but in this case we will not be using anything in the environment
# so we 'pass' on putting things in there

class MyEnvironment(ccm.Model):
    pass

#####
# create an act-r agent

class MyAgent(ACTR):
    
    focus=Buffer()
    DMbuffer=Buffer() # create a buffer for the declarative memory (henceforth DM)

    DM=Memory(DMbuffer)  # create DM and connect it to its buffer 

    focus.set('goal:sandwich object:bread_bottom')

    DM.add('cheese:swiss')
    DM.add("condiment:mustard")
    DM.add("condiment:ketchup")

    # DM.add('condiment:ketchup')

    def bread_bottom(focus='goal:sandwich object:bread_bottom'):
        print("I have a piece of bread") 
        focus.set('goal:sandwich object:cheese')

    def cheese(focus='goal:sandwich object:cheese'):          
        print("I have put cheese on the bread")      
        focus.set('goal:sandwich object:ham')

    def ham(focus='goal:sandwich object:ham'):
        print("I have put  ham on the cheese")
        focus.set('goal:sandwich object:condiment') ###

    def condiment(focus='goal:sandwich object:condiment'):
        print("recalling the condiment")
        DM.request('condiment:?') # retrieve a chunk from DM into the DM buffer
        focus.set('goal:recall') 

    def recall(focus='goal:recall', DMbuffer='condiment:?'): # match to DMbuffer as well
        print("I recall they wanted.......")                            
        #print(f"{condiment}")
        print("i have put the condiment on the sandwich")
        focus.set('goal:sandwich object:bread_top')

    def bread_top(focus='goal:sandwich object:bread_top'): ###
        print("I have put bread on the ham")
        print("I have made a ham and cheese sandwich")
        focus.set('goal:sandwich object:none')


tim=MyAgent()                              # name the agent
subway=MyEnvironment()                     # name the environment
subway.agent=tim                           # put the agent in the environment
ccm.log_everything(subway)                 # print out what happens in the environment

subway.run()                               # run the environment
ccm.finished()                             # stop the environment
