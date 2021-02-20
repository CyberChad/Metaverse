def initializeAddition(goal='add ?num1 ?num2 count:None?count sum:None?sum'):
    goal.modify(count=0, sum=num1)
    memory.request('count ?num1 ?next')

def incrementSum(goal='add ?num1 ?num2 count:?count!?num2 sum:?sum',
                 retrieve='count ?sum ?next'):
    goal.modify(sum=next)
    memory.request('count ?count ?n2')


def incrementCount(goal='add ?num1 ?num2 count:?count sum:?sum',
                   retrieve='count ?count ?next'):
    goal.modify(count=next)
    memory.request('count ?sum ?n2')

def terminateAddition(goal='add ?num1 ?num2 count:?num2 sum:?sum'):
    goal.set('result ?sum')
    print(sum)
    # goal.set('add 5 2 count:None sum:None')