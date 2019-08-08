#from __future__ import print_function

import logging
import sys

from pysc2.agents import base_agent
from pysc2.lib import actions

#sys.path.append('../../')

from ccm import model
from ccm.lib.actr import *

from ccm import *

class Addition(ACTR):
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
        print sum

    def incrementSum(goal='add ?num1 ?num2 count:?count!?num2 sum:?sum',
                     retrieve='count ?sum ?next'):
        goal.modify(sum=next)
        memory.request('count ?count ?n2')

    def incrementCount(goal='add ?num1 ?num2 count:?count sum:?sum',
                       retrieve='count ?count ?next'):
        goal.modify(count=next)
        memory.request('count ?sum ?n2')


#model = Addition()
#model.goal.set('add 5 2 count:None sum:None')
#model.run()


def sum_two_numbers(a, b):
    return a + b            # return result to the function caller

c = sum_two_numbers(3, 12)  # assign result of function execution to variable 'c'


def fib(n):
    """This is documentation string for function. It'll be available by fib.__doc__()
    Return a list containing the Fibonacci series up to n."""
    result = []
    a = 1
    b = 1
    while a < n:
        result.append(a)
        tmp_var = b
        b = a + b
        a = tmp_var
    return result


class SimpleAgent(base_agent.BaseAgent):
    def step(self, obs):
        super(SimpleAgent, self).step(obs)

        return actions.FunctionCall(actions.FUNCTIONS.no_op.id, [])

# holds the different cognitive architectures that we have available
class Architectures:
    def __init__(self, cogArchConfig):
        self.cogArchConfig = cogArchConfig #holds the configuration file



# the environments we can test our agents in
class Environments:
    def __init__(self, envConfig):
        self.envConfig = envConfig #holds the configuration file



class Utilities:

    def readFile(file):

        f = open(file, "r")   # here we open file "input.txt". Second argument used to identify that we want to read file
                                     # Note: if you want to write to the file use "w" as second argument

        for line in f.readlines():   # read lines
            print(line)

        f.close()                   # It's important to close the file to free up any system resources.

    def writeFile(fileName):

        logging.info('Calling write file')

        if len(fileName) is 0:
            logging.warning("file is null")

        f = open(file, "a")

        for i in range(5):
            f.write(i)

        f.close()




if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    print(fib(10))
    model = Addition()
    model.goal.set('add 5 2 count:None sum:None')
    model.run()




