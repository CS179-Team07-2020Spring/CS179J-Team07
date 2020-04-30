import gym
from gym import error, spaces
from gym import utils
from gym.utils import seeding

class RobotEnv(gym.Env):
    """
    Observation:
        Type: Box(3)
        Num     Observation     Min     Max
        0       Red             0       255
        1       Green           0       255
        2       Blue            0       255

    Actions:
        Type: Discrete(3)
        Num     Action
        0       Go straight
        1       Turn left
        2       Turn right

    Reward:
        1 for every step taken without slowing down

    Episode Termination:
        Robot comes to a stop
        Speed slows down

    """
    metadata = {'render.modes': ['human']}

    @TODO
    def __init__(self):
        super(RobotEnv, self).__init__()
        n_actions = 3
        self.action_space = spaces.Discrete(n_actions)
        self.observation_space = spaces.Box(0, 255, [height, width, 3])

    def step(self, action):
        """
        execute one time step within the environment

        :action: TODO
        :returns: next observation, the immediate reward, if episode is done, additional info
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
