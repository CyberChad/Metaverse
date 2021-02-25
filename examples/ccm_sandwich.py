#################### ham cheese production model ###################

# this is the simplest type of act-r model
# it uses only the production system and one buffer
# the buffer represents the focus of thought
# we call it the focus buffer but it is often called the goal buffer
# productions fire if they match the focus buffer
# each production changes the contents of focus buffer so a different production will fire on the next cycle


import ccm

log = ccm.log()

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
    focus = Buffer()

    def init():
        focus.set('goal:sandwich object:bread')

    def bread_bottom(focus='goal:sandwich object:bread'):  # if focus buffer has this chunk then....
        print("I have a piece of bread")  # print
        focus.set('goal:sandwich object:cheese')  # change chunk in focus buffer

    def ham(focus='goal:sandwich object:ham'):
        print("I have put  ham on the cheese")
        focus.set('goal:sandwich object:bread_top')

    def cheese(focus='goal:sandwich object:cheese'):  # the rest of the productions are the same
        print("I have put cheese on the bread")  # but carry out different actions
        focus.set('goal:sandwich object:ham')


    def bread_top(focus='goal:sandwich object:bread_top'):
        print("I have put bread on the ham")
        print("I have made a ham and cheese sandwich")
        focus.set('goal:stop')

    ##    def stop_production(focus='goal:stop'):


##        self.stop()                                          # stop the agent

tim = MyAgent()  # name the agent
subway = MyEnvironment()  # name the environment
subway.agent = tim  # put the agent in the environment
ccm.log_everything(subway)  # print out what happens in the environment

subway.run()  # run the environment
ccm.finished()  # stop the environment