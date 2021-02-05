import os
import cmuactr as actr
import time

HOME_DIR = os.getenv("HOME")
DIR_PATH = os.path.dirname(os.path.realpath(__file__))
print(DIR_PATH)

import sys

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

class CmuExperiment():

    def __init__(self):
        self.unittest()

    def unittest(self):
        timestr = time.strftime("%Y%m%d-%H%M%S")
        self.start("testoutput_" + timestr + ".log")
        self.experiment()
        self.stop()

    def start(filename):
        """Start transcript, appending print output to given filename"""
        sys.stdout = Transcript(filename)

    def stop():
        """Stop transcript and return print functionality to normal"""
        sys.stdout.logfile.close()
        sys.stdout = sys.stdout.terminal

    def experiment():

        actr.load_act_r_model(DIR_PATH+"/cmu_count_test.lisp")
        actr.reset()
        actr.record_history("buffer-trace")
        actr.record_history("goal")
        actr.record_history("retrieval-history")

        actr.run(1,True)

        actr.stop_recording_history("buffer-trace")
        actr.stop_recording_history("goal")
        trace_buffer = actr.get_history_data("buffer-trace")
        trace_goal = actr.get_history_data("goal")

        print("*** BUFFER TRACE ***")
        print(trace_buffer)
        #print(trace_goal)

        print("*** ACTIVATION TRACE ***")
        print(actr.print_activation_trace("first 0.6"))

        actr.save_history_data("go  al", "../../history_output.json")

if __name__ == "__main__":

    timestr = time.strftime("%Y%m%d-%H%M%S")

    CmuExperiment.start("testoutput_"+timestr+".log")
    CmuExperiment.experiment()
    CmuExperiment.stop()

