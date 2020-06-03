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
from skimage import io
from skimage import color
import imutils
from scipy import stats
# from jetbot import Robot



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
    RIGHT = 2

    def __init__(self):
        super(RobotEnv, self).__init__()
        n_actions = 3
        self.action_space = spaces.Discrete(n_actions)
        self.observation_space = spaces.Box(0, 255, [224, 224, 3], dtype=np.uint8)
        self.state = None
        self.reward = 0
        self.speed = 20
        self.speed_threshold = 10
        self.image = None
        self.prev_image = None
        # self.robot = Robot()
        self.epsilon = 0.3
        self.count = 178
        self.status = None

    def step(self, action):
        """
        execute one time step within the environment

        :action: TODO
        :returns: next observation, the immediate reward, if episode is done, additional info
        """
        if action == self.LEFT or action == self.RIGHT:
            self.count += 100
            reward = 0.2
        elif action == self.STRAIGHT:
            self.count += 5
            reward = 10

        if self.count >= 956:
            self.count = 178

        image = "gym_env/envs/" + str(self.count) + ".png"
        # self.image = Image.open(image)
        # self.image = cv2.imread(image)
        self.image = io.imread(image)

        img = color.rgb2gray(self.image)
        prev_img = color.rgb2gray(self.prev_image)

        (score, diff) = compare_ssim(img, prev_img, full=True)

        placeholder = self.image
        placeholder[placeholder > 245] = 0
        flat_non_zero = placeholder[np.nonzero(placeholder)]
        val = stats.mode(flat_non_zero, axis=None)
        self.image[self.image > 245] = val[0]
        score = cv2.sumElems(self.image)
        s = sum(list(score))


        done = bool(s < 11800000)

        if not done:
            self.status = "Clear"
            # reward = 1.0
        else:
            self.status = "Blocked"
            reward = 0.0

        info = {image:s} # not required

        data = np.asarray(self.image)
        self.prev_image = self.image

        return data.astype(np.uint8), reward, done, info
        # return self.image, reward, done, info

    def reset(self):
        """ 
        called at the beginning of an episode
        reset the state of the environment to an initial state
        
        :returns: observation
        """
        self.reward = 0
        self.speed = 20
        self.count = 178

        # reset to current frame
        # self.image = Image.open('0.png')
        # self.image = cv2.imread('0.png')
        self.image = io.imread('gym_env/envs/178.png')
        self.prev_image = self.image
        # return np.asarray(self.image).astype(np.uint8)
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

# image = cv2.imread('0.png')
# print(image)

# imageA = cv2.imread("826.png")
# imageB = cv2.imread("827.png")
# graya = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
# grayb = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)

# (score, diff) = compare_ssim(graya, grayb, full=True)
# print("SSIM: {}".format(score))


# n_steps = 20
# for step in range(n_steps):
    # print("Step {}".format(step+1))
    # obs, reward, done, info = env.step(0)
    # print('obs=', obs, 'reward=', reward, 'done=', done)
    # if done:
        # print('reward=', reward)
        # break
