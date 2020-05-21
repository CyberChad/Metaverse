import ccm
from ccm import model
from ccm.lib.actr import *

class ActrAgent(ACTR):
    goal = Buffer()
    retrieve = Buffer()
    memory = Memory(retrieve)



    def init():
        memory.add('count 0 1')
        memory.add('count 1 2')
        memory.add('count 2 3')
        memory.add('count 3 4')
        memory.add('count 4 5')
        memory.add('count 5 6')
        memory.add('count 6 7')
        memory.add('count 7 8')

    def initializeAddition(goal='add ?num1 ?num2 count:None?count sum:None?sum'):
        goal.modify(count=0, sum=num1)
        memory.request('count ?num1 ?next')

    def terminateAddition(goal='add ?num1 ?num2 count:?num2 sum:?sum'):
        goal.set('result ?sum')
        print(sum)
        goal.set('add 5 2 count:None sum:None')

    def incrementSum(goal='add ?num1 ?num2 count:?count!?num2 sum:?sum',
                     retrieve='count ?sum ?next'):
        goal.modify(sum=next)
        memory.request('count ?count ?n2')

    def incrementCount(goal='add ?num1 ?num2 count:?count sum:?sum',
                       retrieve='count ?count ?next'):
        goal.modify(count=next)
        memory.request('count ?sum ?n2')

class MotorModule(ccm.Model):
    pass


if __name__ == "__main__":

    # init ACT-R agent player
    model = ActrAgent()
    model.goal.set('add 5 2 count:None sum:None')
    model.run()