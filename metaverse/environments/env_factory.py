"""Interface for virtual environments. Currently supporting:
OpenAI Gym:
    CartPole
    MountainCar
    LunarLander

StarCraft mini-games:
    move to beacon
    collect mineral shards
    defeat roaches
"""


# the environments we can test our agents in
class Environments:
    def __init__(self, envConfig):
        self.envConfig = envConfig #holds the configuration file

class StarcraftEnvironment():
    pass

class Environment():



    def __init__(self):
        self.actions = []
        self.observations = []

    def getActionSpace(self):

        return self.actions


    def getObservations(self):

        return self.observations