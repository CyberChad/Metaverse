import os
import subprocess
import time
import threading

#ACTR_CCMSuite includes
#import ccm
#from ccm.lib.actr import *

#ACTR_Jakdot includes
#import pyactr as actr

#ACTR_CMU includes



#Soar includes
from Architectures.SOAR.pysoarlib import *

#DEBUG = True


# *********** ACT-R Stuff **********************

# #class Count(ACTR):
#
#     goal = Buffer()
#     retrieve = Buffer()
#     memory = Memory(retrieve)
#
#     def init():
#         print("<<< ACT-R Init >>>")
#         memory.add('count 0 1')
#         memory.add('count 1 2')
#         memory.add('count 2 3')
#         memory.add('count 3 4')
#         memory.add('count 4 5')
#         # memory.add('count 5 6')
#         # memory.add('count 6 7')
#         # memory.add('count 7 8')
#         # memory.add('count 8 9')
#         # memory.add('count 9 10')
#
#     def start(goal='countFrom ?start ?end starting'):
#         print("<<< ACT-R start >>>")
#         memory.request('count ?start ?next')
#         goal.set('countFrom ?start ?end counting')
#         #testtime.sleep(0.05)
#
#
#     def increment(goal='countFrom ?x !?x counting',
#                   retrieve='count ?x ?next'):
#         print("<<< ACT-R increment >>>")
#         print(x)
#         memory.request('count ?next ?nextNext')
#         goal.modify(_1=next)
#
#     def stop(goal='countFrom ?x ?x counting'):
#         print("<<< ACT-R stop >>>")
#         print(x)
#         goal.set('countFrom ?x ?x stop')
#
#
#
# #class MotorModule(ccm.Model):
# #    pass

# *************** Jakdot ACT-R Stuff *****************

# def test_jakdot(start,end):
#
#     counting = actr.ACTRModel()
#
#     #Each chunk type should be defined first.
#     actr.chunktype("countOrder", ("first", "second"))
#     #Chunk type is defined as (name, attributes)
#
#     #Attributes are written as an iterable (above) or as a string, separated by comma:
#     actr.chunktype("countOrder", "first, second")
#
#     dm = counting.decmem
#     #this creates declarative memory
#
#     dm.add(actr.chunkstring(string="\
#         isa countOrder\
#         first 0\
#         second 1"))
#
#     dm.add(actr.chunkstring(string="\
#         isa countOrder\
#         first 1\
#         second 2"))
#     dm.add(actr.chunkstring(string="\
#         isa countOrder\
#         first 2\
#         second 3"))
#     dm.add(actr.chunkstring(string="\
#         isa countOrder\
#         first 3\
#         second 4"))
#     dm.add(actr.chunkstring(string="\
#         isa countOrder\
#         first 4\
#         second 5"))
#
#     #creating goal buffer
#     actr.chunktype("countFrom", ("start", "end", "count"))
#
#     #production rules follow; using productionstring, they are similar to Lisp ACT-R
#
#     counting.productionstring(name="start", string="""
#         =g>
#         isa countFrom
#         start =x
#         count None
#         ==>
#         =g>
#         isa countFrom
#         count =x
#         +retrieval>
#         isa countOrder
#         first =x""")
#
#     counting.productionstring(name="increment", string="""
#         =g>
#         isa     countFrom
#         count       =x
#         end         ~=x
#         =retrieval>
#         isa     countOrder
#         first       =x
#         second      =y
#         ==>
#         =g>
#         isa     countFrom
#         count       =y
#         +retrieval>
#         isa     countOrder
#         first       =y""")
#
#     counting.productionstring(name="stop", string="""
#         =g>
#         isa     countFrom
#         count       =x
#         end         =x
#         ==>
#         ~g>""")
#
#     #adding stuff to goal buffer
#     numrange_chunk = "isa countFrom start {} end {}".format(start,end)
#     #counting.goal.add(actr.chunkstring(string="isa countFrom start 0 end 5"))
#     #counting.goal.add(actr.chunkstring(numrange_chunk))
#     counting.goal.add(actr.chunkstring(string="isa countFrom start {} end {}".format(start,end)))
#
#     x = counting.simulation()
#
#     print("{{{{{ START JAKDOT-R }}}}}")
#     x.run()
#     print("{{{{{ END JAKDOT-R }}}}}")

##### ******* Soar Stuff *************

class SimpleConnector(AgentConnector):
    def __init__(self, agent):
        print("[[[ Soar created ]]]")
        AgentConnector.__init__(self, agent)
        self.add_output_command("increase-number")
        self.num = SoarWME("number", 0)

    def on_input_phase(self, input_link):
        print("[[[ Soar on_input_phase ]]]")
        if not self.num.is_added():
            self.num.add_to_wm(input_link)
        else:
            self.num.update_wm()

    def on_init_soar(self):
        print("[[[ Soar on_init_soar ]]]")
        self.num.remove_from_wm()

    def on_output_event(self, command_name, root_id):
        print("[[[ Soar on_output_event ]]]")
        if command_name == "increase-number":
            self.process_increase_command(root_id)
    
    def process_increase_command(self, root_id):
        print("[[[ Soar process_increase_command ]]]")
        number = root_id.GetChildInt("number")
        if number:
            self.num.set_value(self.num.val + number)
        root_id.AddStatusComplete()



def test_ccmactr(start,end):
    # init ACT-R_CCMSuite counting agent
    model = Count()
    #model.goal.set('countFrom 0 5 starting')
    model.goal.set('countFrom {} {} starting'.format(start,end))
    # log = ccm.log(screen=True)
    ccm.log_everything(model)
    # model.log = log
    model.run()



import cmuactr as cmuactr
def test_cmuactr(start, end):

    #start ACTR_CMU service....

    os.system("echo Starting ACT-R CMU....")
    os.system("")
    list_files = subprocess.run(["ls", "-l"])
    print("The exit code was: %d" % list_files.returncode)

    path_to_CMU = "../../../CMU_ACT-R"
    launch_CMU_cmd = "run-act-r.command"

    #os.system("../../../CMU_ACT-R/run-act-r.command")

    time.sleep(2)

    cmuactr.load_act_r_model("/home/user/github/Metaverse/Architectures/ACT-R_CMU/cmu_count_test.lisp")
    cmuactr.reset()
    cmuactr.run(10,True)



def test_soar(start,end):

    print("[[[ Write {} and {} to config file ]]]".format(start,end))

    time.sleep(2)

    agent = SoarAgent(config_filename="soar_test_counting.config", write_to_stdout=True)
    agent.add_connector("simple", SimpleConnector(agent))
    agent.connect()
    agent.execute_command("run "+str(end))
    agent.kill()

if __name__ == "__main__":

    start = 1
    end = 6
    #run in serial

    #test_ccmactr(start,end)
    #test_cmuactr(start,end)
    time.sleep(3)
    #test_jakdot(start,end)
    test_soar(start, end)

    #run in parallel
    #actr_thread = threading.Thread(target=test_cmuactr(start,end))
    #time.sleep(5)
    #soar_thread = threading.Thread(target=test_soar(start,end))
    # jakdot_thread = threading.Thread(target=test_jakdot(start,end))



