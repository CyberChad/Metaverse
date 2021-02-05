


class MetaLoader(object):

    def __init__(self, name="default", arch=None, env=None):
        print("initializing new Model: "+name)
        self.name = name
        self.arch = arch
        self.env = env

        self._initArch()
        self._initEnv()

    def _initArch(self):

        if self.arch is None:
            #throw a warning
            print("Warning: no Architecture defined for "+self.name)
            pass

        #pass the architecture name to Metamind factory

    def _initEnv(self):

        if self.env is None:
            # throw a warning
            print("Warning: no Environment defined for " + self.name)
            pass

        # pass the Environment name to Metamind factory

        #put some assertions in here

    def initModel(self):

        # *************************************
        # Load CMC MetaModel
        # *************************************

        print("Loading CMC Metamodel...")
        ecoreFile = "metamind.ecore"
        ecoreTree = loadFromXML(ecoreFile)

        modelFile = "Counting.metamind"
        modelTree = loadFromXML(modelFile)

        # import Architectures.metamind as metamind
        import metaverse.metamind as mm
        factory = mm.factory

        # *** Init Model ***

        model = factory.createModel()
        model.name = "test1"

        # *** Init Environments ***
        environment = factory.createEnvironment()

        # *** Init Memory ***
        dm = factory.createDeclarativeMemory()
        model.modules.append(dm)

        # *** Init Motor Interface ***
        motor = factory.createMotor()
        model.modules.append(motor)

        # *** Init Motor Interface ***
        vision = factory.createVisual()
        model.modules.append(vision)

        testenv = factory.createEnvironment()
        model.environment.append(testenv)






