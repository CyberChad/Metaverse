def readFile(file):
    f = open(file, "r")  # here we open file "input.txt". Second argument used to identify that we want to read file
    # Note: if you want to write to the file use "w" as second argument

    for line in f.readlines():  # read lines
        print(line)

    f.close()  # It's important to close the file to free up any system resources.


def writeFile(fileName):
    logging.info('Calling write file')

    if len(fileName) is 0:
        logging.warning("file is null")

    f = open(file, "a")

    for i in range(5):
        f.write(i)

    f.close()


def to_use_in_separate_process(*args):
    print(args)

    # check args before using them:
    if len(args) > 1:
        subprocess.call((args[0], args[1]))
        print('subprocess called')


def checkIfProcessRunning(processName):
    '''
    Check if there is any running process that contains the given name processName.
    '''
    # Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False


def check_process_image(self, procName):
    imgName = "act-r-64"
    notResponding = 'Not Responding'

    r = checkIfProcessRunning(imgName)

    if not r:
        print('%s: No such process, starting...' % (imgName))
        print("Starting CMU ACT-R Dispatcher...")
        #
        # pid = os.fork()
        # if pid:
        #     #parent
        #     time.sleep(10)
        # else:
        #     #child
        #     #subprocess.call(CMUACTR_PATH + "run-act-r.command")
        #     p = Process(target=to_use_in_separate_process, args=(CMUACTR_PATH+'run-act-r.command'))
        #     p.run()
        #     #p.start()


    else:
        print('%s: process is already running.' % (imgName))
