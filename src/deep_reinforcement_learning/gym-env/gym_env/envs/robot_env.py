import gym
from gym import error, spaces
from gym import utils
from gym.utils import seeding
from stable_baselines.common.env_checker import check_env
import numpy as np
import cv2
from PIL import Image
import random
from skimage.measure import compare_ssim
import imutils
from jetbot import Robot



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

    STRAIGHT = 0
    LEFT = 1
    #RIGHT = 2

    def __init__(self):
        super(RobotEnv, self).__init__()
        #n_actions = 3
        n_actions = 2
        self.action_space = spaces.Discrete(n_actions)
        self.observation_space = spaces.Box(0, 255, [224, 224, 3], dtype=np.uint8)
        self.state = None
        self.reward = 0
        self.speed = 20
        self.speed_threshold = 10
        self.image = None
        self.prev_image = None
        self.robot = Robot()

    def step(self, action):
        """
        execute one time step within the environment

        :action: TODO
        :returns: next observation, the immediate reward, if episode is done, additional info
        """

        if action == self.LEFT:
            self.robot.left()
            # take current frame 
            # self.image = image
        '''
        if action == self.RIGHT:
            self.robot.right()
            # take current frame
            # self.image = image
        '''
        elif action == self.STRAIGHT:
            self.robot.straight()
            # take current frame
            # self.image = image
        else:
            raise ValueError("Received invalid action={} that is not part of the action space".format(action))

        grayA = cv2.cvtColor(self.prev_image, cv2.COLOR_BGR2GRAY)
        grayB = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

        (score, diff) = compare_ssim(grayA, grayB, full=True)

        s = self.state
        # done = bool(self.speed < self.speed_threshold)
        done = bool(score > 1-epsilon && score < 1+epsilon)

        if not done:
            reward = 1.0
        else:
            reward = 0.0

        info = {self.image.filename:self.speed} # not required

        data = np.asarray(self.image)
        self.prev_image = self.image

        return data.astype(np.uint8), reward, done, info

    def reset(self):
        """ 
        called at the beginning of an episode
        reset the state of the environment to an initial state
        
        :returns: observation
        """
        self.reward = 0
        self.speed = 20

        # reset to current frame
        self.image = Image.open('nonobstacle.png')
        data = np.asarray(self.image)
        return data.astype(np.uint8)

    def render(self, mode='human'):
        """
        render the environment to the screen

        :mode: TODO
        :returns: TODO
        """
        # for visualization shouldn't be required
        pass

    def close(self):
        """TODO: Docstring for close.

        :returns: TODO
        """
        if self.viewer:
            self.viewer.close()
            self.viewer = None
        pass

env = RobotEnv()
check_env(env, warn=True)

print(env.observation_space)
print(env.action_space)
print(env.action_space.sample())

# n_steps = 20
# for step in range(n_steps):
    # print("Step {}".format(step+1))
    # obs, reward, done, info = env.step(0)
    # print('obs=', obs, 'reward=', reward, 'done=', done)
    # if done:
        # print('reward=', reward)
        # break
