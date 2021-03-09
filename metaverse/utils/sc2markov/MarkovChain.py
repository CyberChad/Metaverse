import numpy as np
import random as rm
import transitionMatrix as tm

import json
import os
import csv

DEBUG = True

directory = 'D:\Development\sc2jsons'

outfile = 'output_gameevts_id.csv'

fdout = open(outfile,'w')

writer = csv.writer(fdout, lineterminator='\n')

def init_states():

    #init and validate the state space

    states = [
        ("CameraSave", "CamS"),
        ("CameraUpdate", "CamU"),
        ("Cmd", "Cmd"),
        ("CmdUpdateTargetPoint", "CmdTP"),
        ("CmdUpdateTargetUnit", "CmdTU"),
        ("CommandManagerState", "CmdMS"),
        ("ControlGroupUpdate", "Ctrl"),
        ("GameUserLeave", "UsrL"),
        ("SelectionDelta", "SelDel"),
        ("TriggerSoundLengthSync", "TgrSLS"),
        ("UserFinishedLoadingSync", "UsrS"),
        ("UserOptions", "UsrO")
    ]

    myState = tm.StateSpace(states)
    print("> Describe state space")
    myState.describe()
    print("> List of states")
    print(myState.get_states())
    print("> List of state labels")
    print(myState.get_state_labels())

def check_matrix():
    if sum(transitionMatrix[0])+sum(transitionMatrix[1])+sum(transitionMatrix[1]) != 3:
        print("Somewhere, something went wrong. Transition matrix, perhaps?")
    else: print("All is gonna be okay, you should move on!! ;)")

def activity_forecast(days):
    # Choose the starting state
    activityToday = "Sleep"
    activityList = [activityToday]
    i = 0
    prob = 1
    while i != days:
        if activityToday == "Sleep":
            change = np.random.choice(transitionName[0],replace=True,p=transitionMatrix[0])
            if change == "SS":
                prob = prob * 0.2
                activityList.append("Sleep")
                pass
            elif change == "SR":
                prob = prob * 0.6
                activityToday = "Run"
                activityList.append("Run")
            else:
                prob = prob * 0.2
                activityToday = "Icecream"
                activityList.append("Icecream")
        elif activityToday == "Run":
            change = np.random.choice(transitionName[1],replace=True,p=transitionMatrix[1])
            if change == "RR":
                prob = prob * 0.5
                activityList.append("Run")
                pass
            elif change == "RS":
                prob = prob * 0.2
                activityToday = "Sleep"
                activityList.append("Sleep")
            else:
                prob = prob * 0.3
                activityToday = "Icecream"
                activityList.append("Icecream")
        elif activityToday == "Icecream":
            change = np.random.choice(transitionName[2],replace=True,p=transitionMatrix[2])
            if change == "II":
                prob = prob * 0.1
                activityList.append("Icecream")
                pass
            elif change == "IS":
                prob = prob * 0.2
                activityToday = "Sleep"
                activityList.append("Sleep")
            else:
                prob = prob * 0.7
                activityToday = "Run"
                activityList.append("Run")
        i += 1
    return activityList

def activity_list():
    # To save every activityList
    list_activity = []
    count = 0

    # `Range` starts from the first count up until but excluding the last count
    for iterations in range(1,10000):
            list_activity.append(activity_forecast(2))

    # Check out all the `activityList` we collected
    #print(list_activity)

    # Iterate through the list to get a count of all activities ending in state:'Run'
    for smaller_list in list_activity:
        if(smaller_list[2] == "Run"):
            count += 1

    # Calculate the probability of starting from state:'Sleep' and ending at state:'Run'
    percentage = (count/10000) * 100
    print("The probability of starting at state:'Sleep' and ending at state:'Run'= " + str(percentage) + "%")

def game_events_id():

  #loop through all files in given directory

  for infile in os.listdir(directory):

    if infile.endswith(".json"): #make sure we're dealing with a json file
      print("Now processing: "+infile)
      fd = open(directory+'\\'+infile, encoding='utf8') #to handle international characters in map files

      datastore = json.load(fd)

      #get header data

      #header = datastore['Header']
      #metadata = datastore['Metadata']
      #struct = metadata.get('Struct')
      #players = struct.get('Players')

      gameevts = datastore.get('GameEvts')

      #get player APM and MMR

      #events = gameevts.get('GameEvts')

      total = len(gameevts)

      if DEBUG: print("total game events in file: " + str(total))

      #if exists write to CSV file
      for event in gameevts:
        evtstruct = event.get('Struct')
        evtid = evtstruct.get('id')
        evtloop = evtstruct.get('loop')
        evtname = evtstruct.get('name')
        evtuser = evtstruct.get('userid')
        evtuserid = evtuser.get('userId')

        if DEBUG: print("Event loop: "+str(evtloop))
        if DEBUG: print("Event user id: " + str(evtuserid))
        if DEBUG: print("Event id: " + str(evtid))
        if DEBUG: print("Event name: " + evtname)

        #line = str(apm) + ',' + str(mmr)

        writer.writerow([evtloop,evtuserid,evtid,evtname])

    break #for infile...


# function to get unique values
def unique_list(states, DEBUG=False):
    # insert the list to the set
    if DEBUG: print("States: ", states)
    unsorted_list = set(states)
    if DEBUG: print("New list set: ", unsorted_list)
    list_set = sorted(unsorted_list)
    if DEBUG: print("Sorted list set: ", list_set)
    # convert the set to the list
    unique_list = list(list_set)

    if DEBUG: print("List of unique states: ", unique_list)

    return unique_list

def transition_matrix(transitions, DEBUG=False):

    # Sample from https://stackoverflow.com/questions/46657221/generating-markov-transition-matrix-in-python

    # the following code takes a list such as
    # [1,1,2,6,8,5,5,7,8,8,1,1,4,5,5,0,0,0,1,1,4,4,5,1,3,3,4,5,4,1,1]
    # with states labeled as successive integers starting with 0
    # and returns a transition matrix, M,
    # where M[i][j] is the probability of transitioning from i to j

    uniques = unique_list(transitions)
    num_unique = len(uniques)

    if DEBUG: print("number of unique transitions: "+str(num_unique))

    #dict = '104', '49', '14', '101', '29', '27', '28', '105', '56', '7', '103', '5']

    #n = 1 + max(transitions)  # number of states

    #n = num_unique + 1  # number of states
    n = num_unique  # number of states

    M = [[0] * n for _ in range(n)]

    for (s_i, s_j) in zip(transitions, transitions[1:]):
        i = uniques.index(s_i)
        j = uniques.index(s_j)
        M[i][j] += 1

    # now convert to probabilities:
    for row in M:
        s = sum(row)
        if s > 0:
            row[:] = [f / s for f in row]
    return M

# test:


if __name__ == "__main__":

    #game_events_id()
    directory = '..\\Environments\\StarCraft2'
    infile = 'output_gameevts_id.csv'
    fd = open(directory + '\\' + infile, encoding='utf8')

    #print(states)

    #states = [1, 1, 2, 6, 8, 5, 5, 7, 8, 8, 1, 1, 4, 5, 5, 0, 0, 0, 1, 1, 4, 4, 5, 1, 3, 3, 4, 5, 4, 1, 1]
    states = fd.read().splitlines()
    uniques = unique_list(states, True)
    print(uniques)
    matrix = transition_matrix(states, True)

    #printer header

    ix=0

    for row in matrix:
        #print(uniques[ix], end='\t')
        print('\t'.join('{0:.2f}'.format(x) for x in row))
        ix += 1
