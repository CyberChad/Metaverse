#from __future__ import print_function

import logging
import sys

#***************** Problem Formulation *****************

'''
1. The state representation. These are the attributes and values that are used to describe the different
states of the problem.

2. The initial state creation. An operator will generate the state where the problem solving starts. 

3. State elaboration rules. These rules elaborate the state with additional structures that aren’t
fundamental to the state (they aren’t created and deleted by operator application rules), but are
derived from the core aspect of the state. Thus, they are entailments that are useful abstractions,
often making it possible to create simpler rules for proposing and comparing operators.

4. The operator proposal rules. These are the rules that propose the legal state transformations that can
be made toward solving the problem. We can define this as classes of operators:

Eg: A -> A, A -> B, B -> A

5. The operator application rules. These are the rules that transform the state when an operator is
selected.

6. The operator and state monitoring rules. These are optional rules that print out the operator as it
applies and prints out the current state.

7. The desired state recognition rule. This is a rule that notices when one of the desired states is
achieved.

8. The search control rules. These are optional rules that prefer the selection of one operator over
another. Their purpose is to avoid useless operators and/or direct the search toward the desired
state. Theoretically you could encode enough rules so that the correct operator is always selected for
each state. However, you would have had to already solved the problem yourself to figure out those
rules. Our goal is to have the program solve the problem, using only knowledge available from the
problem statement and possibly some general knowledge about problem solving. Therefore, search
control will be restricted to general problem solving heuristics.
'''


class Agent(ACTR):
    focus = Buffer()
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

        focus.set('add 5 2 count:None sum:None')

    def initializeAddition(focus='add ?num1 ?num2 count:None?count sum:None?sum'):
        #print "initializeAddition"
        focus.modify(count=0, sum=num1)
        memory.request('count ?num1 ?next')

    def terminateAddition(focus='add ?num1 ?num2 count:?num2 sum:?sum'):
        #print "terminateAddition"
        focus.set('result ?sum')
        #print sum

    def incrementSum(focus='add ?num1 ?num2 count:?count!?num2 sum:?sum',
                     retrieve='count ?sum ?next'):
        #print "incrementSum"
        focus.modify(sum=next)
        memory.request('count ?count ?n2')

    def incrementCount(focus='add ?num1 ?num2 count:?count sum:?sum',
                       retrieve='count ?count ?next'):
        #print "incrementCount"
        focus.modify(count=next)
        memory.request('count ?sum ?n2')


#model = Addition()
#model.goal.set('add 5 2 count:None sum:None')
#model.run()


def sum_two_numbers(a, b):
    return a + b            # return result to the function caller

c = sum_two_numbers(3, 12)  # assign result of function execution to variable 'c'






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

class StarcraftEnvironment(Model):
    pass

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
    #print(fib(10))

    player = Agent()

    empty_env = StarcraftEnvironment()
    empty_env.agent = player
    log_everything(empty_env)

    empty_env.run()




