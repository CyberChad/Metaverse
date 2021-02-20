import sys
from pyparsing import *
import re
import logging

#logging.basicConfig(filename=sample.log, level=logging.INFO)

# logging.debug("This is a debug message")
# logging.info("Informational message")
# logging.error("An error has happened!")

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

class Parser(object):

    def __init__(self, filename):
        self.filename = filename

    def timestamps(self, line):
        return re.findall(r"+[0-9].[0=9]",line)


    def importACTR(self):

        print(f"Parser importing: {self.filename}")
        self.infile = open(self.filename, "r")

        data = {}



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
        declarative = Literal("DECLARATIVE")
        declarative.setResultsName("DM")
        procedural = Literal("PROCEDURAL")
        procedural.setResultsName("PM")
        module = declarative | procedural
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

        print(f"Parser.importACTR(): generating token tree")

        results = ""

        for line in self.infile.readlines():
            print(f"Scanning line: {line}")
            for match in event1.scanString(line):
                results += line

        #return event1.parseString(results)
        return results


if __name__ == '__main__':

    logfile = "/home/chad/Dropbox/Metaverse/metaverse/experiments/results/cmu_count_test_20210209-145541.log"

    parser = Parser(logfile)

    cleaned = parser.importACTR()

    #print(cleaned)

    infile = open(parser.filename, "r")

    data = {}

    for line in cleaned.split('\n'):
        #print(line)
        tokens = line.split()
        print(tokens)
        #data[tokens[0]] = []
        #print(data)
    #
    #
    # print(tree.asXML())

