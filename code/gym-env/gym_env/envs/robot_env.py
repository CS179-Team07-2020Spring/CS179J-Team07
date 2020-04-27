import gym
from gym import error, spaces
from gym import utils
from gym.utils import seeding

class RobotEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    @TODO
    def __init__(self):
        super(RobotEnv, self).__init__()

    def step(self, action):
        """
        execute one time step within the environment

        :action: TODO
        :returns: observation, reward, done, info
        """
        return observation, reward, done, info

    def reset(self):
        """ 
        called at the beginning of an episode
        reset the state of the environment to an initial state
        
        :returns: observation
        """
        return observation


    def render(self, mode='human'):
        """
        render the environment to the screen

        :mode: TODO
        :returns: TODO
        """
        pass


    def close(self):
        """TODO: Docstring for close.

        :returns: TODO
        """
        pass
