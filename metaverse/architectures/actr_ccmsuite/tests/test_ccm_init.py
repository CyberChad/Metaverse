import ccm

from ccm.lib.actr import *

class client():
    pass

class Agent(ACTR):
    goal = Buffer()

    def init():
        goal.set("test")

    def test(goal="test"):
        print("Python ACT-R installation up and running")

        print("The hard part is over :-)")
        goal.set("stop")

    def stop_production(goal="stop"):
        self.stop()

class MyEnvironment(ccm.Model):
    pass

if __name__ == "__main__":


    model = Agent()
    model.goal.set('add 5 2 count:None sum:None')
    model.run()

    empty_environment = MyEnvironment()
    empty_environment.agent = model

    # ccm.log_everything(empty_environment)
    ccm.log_everything(model)

    # empty_environment.run()

    # ccm.finished()