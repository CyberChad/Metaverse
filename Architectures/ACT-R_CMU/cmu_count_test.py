import os
import cmuactr as actr

HOME_DIR = os.getenv("HOME")
DIR_PATH = os.path.dirname(os.path.realpath(__file__))
print(DIR_PATH)

def experiment():

    actr.load_act_r_model(DIR_PATH+"/cmu_count_test.lisp")
    actr.reset()
    actr.run(10,True)

if __name__ == "__main__":
    experiment()
