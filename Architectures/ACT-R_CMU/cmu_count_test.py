
import cmuactr as actr

def experiment():

    actr.load_act_r_model("/home/user/github/Metaverse/Architectures/ACT-R_CMU/cmu_count_test.lisp")
    actr.reset()
    actr.run(10,True)



if __name__ == "__main__":
    experiment()
