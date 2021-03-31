import metaverse.architectures.soar.pysoarlib
import metaverse.architectures.soar.SoarLibs
from metaverse.architectures.soar.pysoarlib import \
    AgentConnector,\
    SoarAgent,\
    SoarWME

class SimpleConnector(AgentConnector):
    def __init__(self, agent):
        AgentConnector.__init__(self, agent)
        # self.add_output_command("increase-number")
        # self.num = SoarWME("number", 0)
        #self.target = SoarWME("target", 10)

    def on_input_phase(self, input_link):
        pass
        # if not self.num.is_added():
        #     self.num.add_to_wm(input_link)
        # else:
        #     self.num.update_wm()

    def on_init_soar(self):
        pass
        # self.num.remove_from_wm()

    def on_output_event(self, command_name, root_id):
        pass
        # if command_name == "increase-number":
        #     self.process_increase_command(root_id)
    
    # def process_increase_command(self, root_id):
    #     number = root_id.GetChildInt("number")
    #     if number:
    #         self.num.set_value(self.num.val + number)
    #     root_id.AddStatusComplete()

agent = SoarAgent(config_filename="soar_memory_test.config", write_to_stdout=True)
#agent = SoarAgent(write_to_stdout=True)
agent.add_connector("simple", SimpleConnector(agent))
agent.connect()

agent.execute_command("watch 5")
agent.execute_command("stats -t")
agent.execute_command("smem --set learning on")

#agent.execute_command("smem --add {(@A1 ^name alice ^friend @B1) (@B1 ^name bob ^friend @A1 @C4) (@C4 ^name charley)}")
#agent.execute_command("smem --add {(A1 ^name alice ^friend B1) (B1 ^name bob ^friend A1 C4) (C4 ^name charley)}")

#agent.execute_command("sp {ncb (state <s> ^superstate nil ^smem.command <cmd>) --> (<cmd> ^retrieve @B1)}")

agent.execute_command("run 20 -p")
agent.execute_command("print @")
agent.execute_command("print --depth 10 L1")
#agent.execute_command("smem --stats")


# for i in range(0,12):
#     agent.execute_command("run 1") #runs for 12 decision cycles

agent.kill()
