import os
import metaverse.architectures.actr_cmu.cmuactr_sorted as actr

import json

HOME_DIR = os.getenv("HOME")
DIR_PATH = os.path.dirname(os.path.realpath(__file__))
print(DIR_PATH)

def test_system_controls():

    print("--Testing output trace--")

def experiment():

    actr.load_act_r_model(DIR_PATH+"/command_tests.lisp")
    actr.reset()
    #actr.run(10,True)

    for i in range(10):
        print("event: "+str(i))
        actr.run_n_events(1)


def test_meta_commands():
    print("test meta commands")
    actr.reset()

def test_reporting():
    print("-- test reporting --")

    actr.print_activation_trace(600)

    print("-- pprintchunks --")
    actr.pprint_chunks()

    print("*** PRINT ALL PRODUCTIONS ***")

    print(str(actr.all_productions()))

    print("-- PRINT ALL BUFFERS --")

    print(str(actr.buffers()))

def test_buffers():

    print("-- print buffers --")

    actr.buffers()

def test_chunks():

    print("-- pprintchunks --")
    actr.pprint_chunks()


def test_global_params():
    print("-- sgp --")
    actr.get_parameter_value("sgp")

def test_run_system():

    actr.load_act_r_model(DIR_PATH+"/command_tests.lisp")
    actr.reset()
    #actr.run(1,True) #run in real time for 1 second, stop when out of events
    actr.run_full_time(1, True) #run in real time until out of time

def test_event_schedule():

    #actr.current_model()
    actr.call_command("define-model", "foo")
    actr.reset()
    actr.run(1,True)

def test_generate_model():


    actr.call_command("clear-all")
    actr.reset()

    actr.call_command("define-model", "blarg")
    actr.call_command("sgp", ":esc t :bll .5 :ol t :er t :lf 0")
    actr.define_chunks("chunk-type game-state cart_pos cart_vel pole_pos pole_vel state")
    actr.call_command("declare-buffer-usage", "goal game-state :all")

    device = '("motor" "keyboard")'

    print("trying to install device: "+device)

    #actr.call_command("define-device", "motor keyboard")
    curr_devices = actr.call_command("current-devices", "motor")
    print("current devices: " + str(curr_devices))
    defined_devices = actr.call_command("defined-devices")
    print("defined devices: "+str(defined_devices))

    print("--- init productions ---")

    #actr.current_connection.evaluate("(p start => isa game-state ==> =goal> state play)")


    print("--init goal_focus --")
    m = actr.call_command('define-model blarg')
    print(m)
    actr.mp_models()
    #actr.set_current_model("blarg")

    print("current model: "+str(actr.current_model()))
    actr.goal_focus(actr.define_chunks(['isa', 'game-state', 'state', 'one', 'two', 'three']))

    prod_str = ['start','=goal>','state', 'start', '==>','=goal>','state','play']

    prodname = actr.call_command('p end =goal> isa game-state state start ==> =goal> state play')

    print("new production: "+str(prodname))


    prods = actr.all_productions()
    print("all productions: "+str(prods))



    #actr.install_device(device)


if __name__ == "__main__":

    #actr.current_connection.evaluate_single("p", ['dug','if'],['==>'],['then'])

    experiment()

    test_meta_commands()

    test_reporting()

    #test_run_system()

    #test_event_schedule()

    #test_generate_model()




