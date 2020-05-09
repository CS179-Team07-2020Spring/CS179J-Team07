import gym
from gym import error, spaces
from gym import utils
from gym.utils import seeding
from stable_baselines.common.env_checker import check_env
import numpy as np
import cv2
from PIL import Image


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
        Speed falls under the threshold

    """
    metadata = {'render.modes': ['human']}

    def __init__(self):
        super(RobotEnv, self).__init__()
        n_actions = 3
        self.action_space = spaces.Discrete(n_actions)
        self.observation_space = spaces.Box(0, 255, [224, 224, 3], dtype=np.uint8)
        self.state = None
        self.reward = 0
        self.speed = 0
        self.speed_threshold = 10

    def step(self, action):
        """
        execute one time step within the environment

        :action: TODO
        :returns: next observation, the immediate reward, if episode is done, additional info
        """
        if action is not None:
            # turn left
            # go straight
            # turn right
            pass

        s = self.state
        reward = 1 if self.speed > self.speed_threshold else 0
        done = bool(self.speed < self.speed_threshold)

        # get next frame
        # np_imageData = np.asarray('frame.jpg')

        info = {} # not required

        image = Image.open('image1.png')
        data = np.asarray(image)

        return data.astype(np.uint8), reward, done, info

    def reset(self):
        """ 
        called at the beginning of an episode
        reset the state of the environment to an initial state
        
        :returns: observation
        """
        self.reward = 0

        # reset to current frame
        # np_imageData =  np.asarray('image1.png')
        image = Image.open('image1.png')
        # print(image.size)
        data = np.asarray(image)
        return data.astype(np.uint8)

    def render(self, mode='human'):
        """
        render the environment to the screen

        :mode: TODO
        :returns: TODO
        """

    def close(self):
        """TODO: Docstring for close.

        :returns: TODO
        """
        if self.viewer:
            self.viewer.close()
            self.viewer = None

env = RobotEnv()
check_env(env, warn=True)
