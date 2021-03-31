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
    focus.set('goal:sandwich object:bread_bottom')

    production_time=0.05         # production parameter settings
    #production_sd=0.1
    #production_threshold=-20

    pm_new=PMNew(alpha=0.2)


    #pm_pgc=PMPGC(goal=20)
    #MMMM occurs in a cycle, each time the cycle gets longer


    
    pm_noise=PMNoise(noise=0,baseNoise=0)


    def bread_bottom(focus='goal:sandwich object:bread_bottom'):
        print("I have a piece of bread") 
        focus.set('goal:sandwich object:cheese')

    def cheese(focus='goal:sandwich object:cheese'):          
        print("I have put cheese on the bread")      
        focus.set('goal:sandwich object:ham')

    def maple_ham(focus='goal:sandwich object:ham'):
        print('I have put maple ham on the cheese')
        print('MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM')
        focus.set('goal:sandwich object:bread_top') ###
        self.reward(-0.1)
        
    def parma_ham(focus='goal:sandwich object:ham'):
        print('I have put parma ham on the cheese')
        print('PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP')
        focus.set('goal:sandwich object:bread_top') ###
        self.reward(0.1)

    def bread_top(focus='goal:sandwich object:bread_top'): ###
        print("I have put bread on the ham")
        print("I have made a ham and cheese sandwich")
        focus.set('goal:sandwich object:bread_bottom')


tim=MyAgent()                              # name the agent
subway=MyEnvironment()                     # name the environment
subway.agent=tim                           # put the agent in the environment
ccm.log_everything(subway)                 # print out what happens in the environment


subway.run()                               # run the environment
ccm.finished()                             # stop the environment
