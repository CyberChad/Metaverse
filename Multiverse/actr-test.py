import ccm

from ccm.lib.actr import *
class Testing(ACTR):
    goal = Buffer()

    def init():
        goal.set("test")

    def test(goal="test"):
        print "Python ACT-R installation up and running"

        print "The hard part is over :-)"
        goal.set("stop")

    def stop_production(goal="stop"):
        self.stop()

class MyEnvironment(ccm.Model):
    pass

if __name__ == "__main__":
    testing = Testing()
    empty_environment = MyEnvironment()
    empty_environment.agent = testing
    ccm.log_everything(empty_environment)
    empty_environment.run()
    ccm.finished()