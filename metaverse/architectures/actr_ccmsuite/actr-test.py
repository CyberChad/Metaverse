import ccm

from ccm.lib.actr import *

class client():
    pass

class Agent(ACTR):
    goal = Buffer()

    def init():
        goal.set("test")

    def test(goal="test"):
        print("Python ACT-R_CMU installation up and running")

        print("The hard part is over :-)")
        goal.set("stop")

    def stop_production(goal="stop"):
        self.stop()

class MyEnvironment(ccm.Model):
    pass

if __name__ == "__main__":

    test_agent = Agent()

    empty_environment = MyEnvironment()

    empty_environment.agent = test_agent

    ccm.log_everything(empty_environment)

    empty_environment.run()

    ccm.finished()