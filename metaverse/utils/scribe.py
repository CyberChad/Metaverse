import sys
from pyparsing import *
import re
import logging
import streamlit as st
import json
import pandas as pd
import numpy as np
import time
import csv
import matplotlib.pyplot as plt
import seaborn as sns


#logging.basicConfig(filename=sample.log, level=logging.INFO)

log = logging.getLogger("metaverse")

#logging.basicConfig(level=logging.DEBUG, format='%(name)s - %(levelname)s - %(message)s')

# logging.debug("This is a debug message")
# logging.info("Informational message")
# logging.error("An error has happened!")

_DEBUG_ = False

def tokenize(chars: str) -> list:
    "Convert a string of characters into a list of tokens."
    return chars.replace('(', ' ( ').replace(')', ' ) ').split()

def pprint_log(event_tree):
    import pprint
    # isrecursive = pprint.isrecursive(result.asList())
    # print("recursive?: " + str(isrecursive))

    branch_num = 1
    for branch in event_tree.asList():
        print('\n' + "branch: " + str(branch_num))
        pprint.pprint(branch)
        branch_num += 1

class Transcript(object):

    def __init__(self, filename):
        self.terminal = sys.stdout
        self.logfile = open(filename, "a")

    def write(self, message):
        self.terminal.write(message)
        self.logfile.write(message)

    def flush(self):
        # this flush method is needed for python 3 compatibility.
        # this handles the flush command by doing nothing.
        # you might want to specify some extra behavior here.
        pass

def init_states():

    #init and validate the state space

    states = [
        ("Visual", "Vis"),
        ("Production", "Prod"),
        ("Declarative", "Dec"),
        ("Goal", "Goal"),
        ("Motor", "Motor")
    ]

    myState = tm.StateSpace(states)
    print("> Describe state space")
    myState.describe()
    print("> List of states")
    print(myState.get_states())
    print("> List of state labels")
    print(myState.get_state_labels())

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


class Parser(object):

    def __init__(self, filename, type):
        self.filename = filename
        self.type = type

    def timestamps(self, line):
        return re.findall(r"+[0-9].[0=9]",line)


    def import_log(self):
        if self.type is "ACTR":
            return self.importACTR()
        elif self.type is "Soar":
            return self.importSoarCSV()
        elif self.type is "CCM":
            return self.importCCM()
        else: #Shouldn't be here!
            print(f"ERROR -- undefined parser type")

    def get_df(self, cleaned):
        if self.type is "ACTR":
            return self.get_actr_df(cleaned)
        elif self.type is "Soar":
            return self.get_soar_df(cleaned)
        elif self.type is "CCM":
            return self.get_ccm_df(cleaned)
        else: #Shouldn't be here!
            print(f"ERROR -- undefined parser type")

    def plot(self, df):
        if self.type is "ACTR":
            self.plot_actr(df)
        elif self.type is "Soar":
            self.plot_soar(df)
        elif self.type is "CCM":
            self.plot_ccm(df)
        else: #Shouldn't be here!
            print(f"ERROR -- undefined parser type")

    # *****************************************
    #             CMU ACT-R Reports
    # *****************************************

    def importACTR(self):

        log.info(f"Parser:importACTR()> importing {self.filename}")
        self.infile = open(self.filename, "r")

        # primitives
        NL = Suppress(LineEnd())
        alpha_nums = Word(alphanums)
        dash = Literal("-")
        dash_alpha_nums = Combine(dash + OneOrMore(alpha_nums))
        alpha_nums_dash = Combine(alphanums+ZeroOrMore(dash_alpha_nums))
        simple_punc = Word("-./_:*+=")
        nums_dot = nums | simple_punc
        numbers = Word(nums)
        time_stamp = Combine(OneOrMore(numbers)+Literal(".")+OneOrMore(numbers))
        time_stamp.setResultsName("time")
        counter = Literal("[STEP]")
        goal = Literal("GOAL")
        goal.setResultsName("GOAL")
        declarative = Literal("DECLARATIVE")
        declarative.setResultsName("DM")
        procedural = Literal("PROCEDURAL")
        procedural.setResultsName("PM")
        vision = Literal("VISION")
        vision.setResultsName("VISION")
        motor = Literal("MOTOR")
        motor.setResultsName("MOTOR")
        module = goal | declarative | procedural | vision | motor
        module.setResultsName("module")

        #token = Combine(OneOrMore(alpha_nums) + ZeroOrMore(simple_punc) + ZeroOrMore(Literal('-')) + ZeroOrMore(alpha_nums))
        identifier = Combine(OneOrMore(alpha_nums_dash))
        token = time_stamp | identifier
        event = Combine(time_stamp + OneOrMore(identifier))
        # TODO: Forward() declaration for recursive match
        comment = Literal("\"") + OneOrMore(token) + Literal("\"")
        simple_param = alphanums | simple_punc
        tokenlist = Group(OneOrMore(token))
        eventlist = Group(OneOrMore(event))

        event1 = Group(time_stamp + module + OneOrMore(alpha_nums))
        event2 = Group(counter + time_stamp)
        event3 = event1 | event2

        log.info(f"Parser.importACTR(): generating token tree")

        results = ""

        for line in self.infile.readlines():
            log.debug(f"Scanning line: {line}")
            #for match in event1.scanString(line):
            for match in event3.scanString(line):
                #print(f"Including: {line}")
                results += line



        #return event1.parseString(results)
        return results

    def get_actr_df(self, cleaned):

        print("--------------------------")
        print("Cleaned Log")
        print("--------------------------")

        #print(cleaned)
        buffers = []
        data = []
        timers = []
        csv_outfile = 'actr_data.csv'

        fdout = open(csv_outfile, 'w')

        last_time = 0.0

        writer = csv.writer(fdout, lineterminator='\n')

        num_pm = 0
        total_pm = 0
        num_wm = 0
        total_wm = 0
        num_dm = 0
        total_dm = 0
        num_perc = 0
        total_perc = 0
        num_motor = 0
        total_motor = 0

        trace = []

        timer = 0.00

        for line in self.infile.readlines():
            log.debug(f"Scanning line: {line}")

        for line in cleaned.split('\n'):
            if line is not None:
                tokens = line.split()
                if tokens and "[STEP]" in tokens[0]:
                    timer = tokens[1]
                    print(f"{timer} {num_wm} {num_pm} {num_dm} {num_perc} {num_motor}")

                    data.append({
                        'timer' : str(timer),
                        'WorkingMem' : str(num_wm),
                        'ProcMem' : str(num_pm),
                        'DecMem' : str(num_dm),
                        'Vision': str(num_perc),
                        'Motor': str(num_motor)
                    })
                    num_wm = 0
                    num_dm = 0
                    num_pm = 0
                    num_perc = 0
                    num_motor = 0
                elif len(tokens) > 2:
                    timer = tokens[0]
                    buffer = tokens[1]
                    command = tokens[2]
                    if len(tokens) > 3:
                        target = tokens[3]
                    else:
                        target = None
                    if "GOAL" in buffer:
                        num_wm += 1
                        total_wm += 1
                    elif "PROCEDURAL" in buffer:
                        num_pm += 1
                        total_pm += 1
                    elif "DECLARATIVE" in buffer:
                        num_dm += 1
                        total_dm += 1
                    elif "VISION" in line:
                        num_perc += 1
                        total_perc += 1
                    elif "MOTOR" in line:
                        num_motor += 1
                        total_motor += 1


                    #writer.writerow([timer,buffer,command,target])
                    #writer.writerow([timer, buffer, command, target])

                    # data.append({
                    #     'timer' : str(timer),
                    #     'buffer' : str(buffer),
                    #     'command' : str(command),
                    #     'target' : str(target)
                    # })
                    #
                    # buffers.append(tokens[1])

        print(f"Working Mem Total: {total_wm}")
        print(f"Production Mem Total: {total_pm}")
        print(f"Declarative Mem Total: {total_dm}")
        print(f"Perception Total: {total_perc}")
        print(f"Motor Total: {total_motor}")

        data_file = 'actr_data.json'

        with open('actr_data.json', 'w') as outfile:
            json.dump(data, outfile)

        df = pd.read_json(data_file)

        return df

    def plot_actr(self, df, title="Default Title"):

        print("================================")
        print("           Stats")
        print("================================")

        print(df.describe())

        plt.figure()
        df.plot(x="timer")
        plt.legend(loc='best')
        plt.title(title)
        #ax = sns.countplot(x="timer", data=df)
        ax = sns.lineplot(x="timer", data=df)

        # print(df)

        # df2 = df.drop("timer", 1)
        # plt.hist(x=df2)
        # plt.legend(loc='best')
        plt.show()


        #df["command"].hist(by=df["buffer"])
        #df2 = pd.Series(df["buffer"],index=df["timer"])
        #plt.show()


        # buff_grp = df.groupby("buffer").count()
        # #ax = sns.countplot(x="timer",hue="buffer", data=df)
        # ax = sns.lineplot(x="timer", y="buffer", data=df)
        # plt.show()
        # df.plot(figsize=(15,4))
        # df.plot(subplots=True, figsize=(15, 6))
        # df.plot(y=["buffer", "command"], figsize=(15, 4))
        # #df.plot(x="R", y=["F10.7", "Dst"], style='.')
        # plt.show()


    # *****************************************
    #             Soar Reports
    # *****************************************

    def importSoar(self):

        log.info(f"Parser:importSoar()> importing {self.filename}")
        self.infile = open(self.filename, "r")

        # primitives
        NL = Suppress(LineEnd())
        alpha_nums = Word(alphanums)
        dash = Literal("-")
        dash_alpha_nums = Combine(dash + OneOrMore(alpha_nums))
        alpha_nums_dash = Combine(alphanums+ZeroOrMore(dash_alpha_nums))
        simple_punc = Word("-./_:*+=")
        nums_dot = nums | simple_punc
        numbers = Word(nums)
        time_stamp = Combine(OneOrMore(numbers)+Literal(".")+OneOrMore(numbers))
        time_stamp.setResultsName("STEP")
        wm_add = Literal("=>WM")
        wm_remove = Literal("<=WM")
        procedural = wm_remove | wm_add
        goal = Literal("GOAL")
        goal.setResultsName("GOAL")
        declarative = Literal("DECLARATIVE")
        declarative.setResultsName("DM")
        #procedural = Literal("PROCEDURAL")
        #procedural.setResultsName("PM")
        module = goal | declarative | procedural
        module.setResultsName("module")

        #token = Combine(OneOrMore(alpha_nums) + ZeroOrMore(simple_punc) + ZeroOrMore(Literal('-')) + ZeroOrMore(alpha_nums))
        identifier = Combine(OneOrMore(alpha_nums_dash))
        token = time_stamp | identifier
        event = Combine(time_stamp + OneOrMore(identifier))
        # TODO: Forward() declaration for recursive match
        comment = Literal("\"") + OneOrMore(token) + Literal("\"")
        simple_param = alphanums | simple_punc
        tokenlist = Group(OneOrMore(token))
        eventlist = Group(OneOrMore(event))

        event1 = Group(time_stamp + module + OneOrMore(alpha_nums))
        event2 = Group(procedural + OneOrMore(alpha_nums))

        log.info(f"Parser.importSoar(): generating token tree")

        results = ""

        num_pm = 0
        total_pm = 0
        num_wm = 0
        total_wm = 0
        num_dm = 0
        total_dm = 0
        num_perc = 0
        total_perc = 0
        num_motor = 0
        total_motor = 0

        trace = []

        for line in self.infile.readlines():
            log.debug(f"Scanning line: {line}")
            if ("=>WM" in line) or ("<=WM" in line):
                num_wm += 1
                total_wm += 1
            elif "Firing" in line:
                num_pm += 1
                total_pm += 1
            elif ("^store" in line) or ("^retrieve" in line):
                num_dm += 1
                total_dm += 1
            elif "input-link" in line:
                num_perc += 1
                total_perc += 1
            elif "output-link" in line:
                num_motor +=1
                total_motor += 1
            elif "<<STEP" in line:
                tokens = tokenize(line)
                print(f"{tokens[1]}: {num_wm} {num_pm} {num_dm} {num_perc} {num_motor}")
                num_wm = 0
                num_dm = 0
                num_pm = 0
                num_perc = 0
                num_motor = 0

        print(f"Working Mem Total: {total_wm}")
        print(f"Production Mem Total: {total_pm}")
        print(f"Declarative Mem Total: {total_dm}")
        print(f"Perception Total: {total_perc}")
        print(f"Motor Total: {total_motor}")

        #return event1.parseString(results)
        return results

    def importSoarCSV(self):

        log.info(f"Parser:importSoarCSV()> importing {self.filename}")
        self.infile = open(self.filename, "r")

        result = ""
        copy = False

        for line in self.infile.readlines():
            #log.debug(f"Scanning line: {line}")

            if "START-CSV" in line:
                copy = True
            elif "END-CSV" in line:
                copy = False

            if copy and ("START-CSV" not in line) and ("firing_count" not in line):

                result += line

        #return event1.parseString(results)
        print(f"CSV RESULTS:\n\n{result}")

        return result

    def get_soar_df(self, cleaned):

        print("--------------------------")
        print("Cleaned Log")
        print("--------------------------")

        #print(cleaned)
        buffers = []
        data = []
        csv_outfile = 'soar_data.csv'

        fdout = open(csv_outfile, 'w')

        writer = csv.writer(fdout, lineterminator='\n')

        timer = 0.000

        for line in cleaned.split('\n'):
            if line is not None:
                tokens = line.split(",")
                if len(tokens) > 3:
                    wm_changes = tokens[3]
                    #writer.writerow([timer,wm_changes])

                    data.append({
                        'timer' : str(format(timer, '.2f')),
                        'changes' : str(wm_changes)
                    })
                    print(f"Timer: {format(timer, '.2f')}, Changes: {wm_changes}")
                timer += 0.05

            #data[tokens[0]] = []
            #print(data)

        #print(f"All buffers: {buffers}")

        print(f"JSONified:{data}")

        data_file = 'soar_data.json'

        with open('soar_data.json', 'w') as outfile:
            json.dump(data, outfile)

        df = pd.read_json(data_file)

        return df

    def plot_soar(self, df):

        print("================================")
        print("           Stats")
        print("================================")

        print(df)


        plt.figure()
        df.plot(x="timer")
        plt.legend(loc='best')
        plt.title(title)
        #ax = sns.countplot(x="timer", data=df)
        ax = sns.lineplot(x="timer", data=df)

    # *****************************************
    #             CCM ACT-R Reports
    # *****************************************

    def importCCM(self):

        log.info(f"Parser:importCCM()> importing {self.filename}")
        self.infile = open(self.filename, "r")

        # primitives
        NL = Suppress(LineEnd())
        alpha_nums = Word(alphanums)
        dash = Literal("-")
        dash_alpha_nums = Combine(dash + OneOrMore(alpha_nums))
        alpha_nums_dash = Combine(alphanums+ZeroOrMore(dash_alpha_nums))
        simple_punc = Word("-./_:*+=")
        nums_dot = nums | simple_punc
        numbers = Word(nums)
        time_stamp = Combine(OneOrMore(numbers)+Literal(".")+OneOrMore(numbers))
        time_stamp.setResultsName("time")
        goal = Literal("goal.chunk")
        goal.setResultsName("GOAL")
        declarative = Literal("memory.busy")
        declarative.setResultsName("DM")
        procedural = Literal("production")
        procedural.setResultsName("PM")
        perception = Literal("perception.chunk")
        perception.setResultsName("VISION")
        motor = Literal("motor")
        perception.setResultsName("MOTOR")
        module = goal | declarative | procedural | perception | motor
        module.setResultsName("module")

        #token = Combine(OneOrMore(alpha_nums) + ZeroOrMore(simple_punc) + ZeroOrMore(Literal('-')) + ZeroOrMore(alpha_nums))
        identifier = Combine(OneOrMore(alpha_nums_dash))
        token = time_stamp | identifier
        event = Combine(time_stamp + OneOrMore(identifier))
        # TODO: Forward() declaration for recursive match
        comment = Literal("\"") + OneOrMore(token) + Literal("\"")
        simple_param = alphanums | simple_punc
        tokenlist = Group(OneOrMore(token))
        eventlist = Group(OneOrMore(event))

        event1 = Group(time_stamp + module + OneOrMore(alpha_nums))

        log.info(f"Parser.importCCM(): generating token tree")

        results = ""

        for line in self.infile.readlines():
            log.debug(f"Scanning line: {line}")
            for match in event1.scanString(line):
                results += line

        #return event1.parseString(results)
        return results

    def get_ccm_df(self, cleaned):

        print("--------------------------")
        print("Cleaned Log")
        print("--------------------------")

        #print(cleaned)
        buffers = []
        data = []
        csv_outfile = 'ccm_data.csv'

        fdout = open(csv_outfile, 'w')

        writer = csv.writer(fdout, lineterminator='\n')

        for line in cleaned.split('\n'):
            if line is not None:
                tokens = line.split()
                if len(tokens) > 2:
                    timer = tokens[0]
                    buffer = tokens[1]
                    command = tokens[2]

                    writer.writerow([timer,buffer,command])

                    data.append({
                        'timer' : str(timer),
                        'buffer' : str(buffer),
                        'command' : str(command)
                    })

                    buffers.append(tokens[1])
            #print(f"Timer: {timer}, Buffer: {buffer}, Command: {command}, Target: {target}")

            #data[tokens[0]] = []
            #print(data)

        #print(f"All buffers: {buffers}")

        #print(f"JSONified:{data}")

        data_file = 'ccm_data.json'

        with open('ccm_data.json', 'w') as outfile:
            json.dump(data, outfile)

        df = pd.read_json(data_file)

        return df

    def plot_ccm(self, df):

        print("================================")
        print("           Stats")
        print("================================")

        print(df)

def test_actr():

    actr_count_log = "cmu_count_test.log"
    actr_cart_log = "cmu_cartpole.log"
    actr_beacon_log = "cmu_beacons.log"

    # parser = Parser(actr_count_log, "ACTR")
    # cleaned = parser.importACTR()
    # df = parser.get_actr_df(cleaned)
    # parser.plot_actr(df, "CMU ACT-R Counting")

    # parser = Parser(actr_cart_log, "ACTR")
    # cleaned = parser.importACTR()
    # df = parser.get_actr_df(cleaned)
    # parser.plot_actr(df, "CMU ACT-R Cartpole")

    parser = Parser(actr_beacon_log, "ACTR")
    cleaned = parser.importACTR()
    df = parser.get_actr_df(cleaned)
    parser.plot_actr(df, "CMU ACT-R SC2-Beacons")

def test_soar():

    #soar_logfile = "/home/chad/Dropbox/Metaverse/metaverse/experiments/results/soar_cartpole_20210308-174857.log"
    #soar_logfile = "soar_counting_example.log"
    soar_logfile = "soar_cartpole_example.log"

    parser = Parser(soar_logfile, "Soar")
    #cleaned = parser.importSoarCSV()
    cleaned = parser.importSoar()
    soar_df = parser.get_soar_df(cleaned)
    parser.plot_soar(soar_df)

def test_ccm():

    ccm_logfile = "/home/chad/Dropbox/Metaverse/metaverse/experiments/results/ccm_cartpole_20210308-210739.log"
    #ccm_logfile = "/home/chad/Dropbox/Metaverse/metaverse/experiments/results/ccm_count_test_20210308-202253.log"

    parser = Parser(ccm_logfile, "CCM")
    cleaned = parser.importCCM()
    ccm_df = parser.get_ccm_df(cleaned)
    parser.plot_soar(ccm_df)

def test_df():

    '''
    Test cases for Pandas data structures and algorithms
    From https://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html

    '''

    # s = pd.Series([1, 3, 5, np.nan, 6, 8])
    # print(s)
    #
    # dates = pd.date_range("20130101", periods=6)
    # print(dates)
    # df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))
    #
    # print(df.head())
    # print(df.tail(3))
    # print(df.describe())
    #
    # print(df.sort_index(axis=1, ascending=False))
    # print(df.sort_values(by="B"))
    # print(df["A"])
    #
    # Cross section by row
    # print(df[0:3])
    #
    # Select multi-axis by label
    # print(df.loc[:, ["A", "B"]])
    #
    # Select by integer slices
    # print(df.iloc[3:5, 0:2])
    #
    # Boolean Indexing
    # print(df[df["A"] > 0])

    # Stats
    # print(df.mean()) #across all columns
    # print (df.mean(1)) #across all rows

    # Histogrammin'
    # s = pd.Series(np.random.randint(0, 7, size=10))
    # print(s.value_counts())

    # **** Time Series ****
    # rng = pd.date_range("1/1/2012", periods=100, freq="S")
    # ts = pd.Series(np.random.randint(0, 500, len(rng)), index=rng)
    # ts.resample("5Min").sum() #resampling seconds into 5-minute intervals
    # print(ts)

    # Converting between period and time span representation
    # rng = pd.date_range("1/1/2012", periods=5, freq="M")
    # ts = pd.Series(np.random.randn(len(rng)), index=rng)
    # ps = ts.to_period()
    # print(ps)

    #***** Plotting ****
    # import matplotlib.pyplot as plt #using pyplot vs default matplotlib API
    # plt.close("all")
    # ts = pd.Series(np.random.randn(1000), index=pd.date_range("1/1/2000", periods=1000))
    # ts = ts.cumsum()
    # ts.plot()

    #df plot method allows plotting with columns as labels
    ts = pd.Series(np.random.randn(1000), index=pd.date_range("1/1/2000", periods=1000))
    ts = ts.cumsum()
    df = pd.DataFrame(np.random.randn(1000, 4), index = ts.index, columns = ["A", "B", "C", "D"])
    df = df.cumsum()
    plt.figure()
    df.plot()
    plt.legend(loc='best')
    plt.show()

if __name__ == '__main__':

    test_df()

    test_actr()

    #test_soar()

    #test_ccm()


