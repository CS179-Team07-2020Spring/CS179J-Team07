import gym
import gym_env
from stable_baselines.common import make_vec_env
from stable_baselines.common.policies import MlpPolicy, CnnPolicy
from stable_baselines import A2C, PPO2
import imutils
from skimage.measure import compare_ssim
import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from skimage import io
from skimage import color


def train_new():
    # train from the beginning
    env = make_vec_env('Robot-v0', n_envs=1)
    # n_steps default = 128
    # halving to address resource exhausted error
    model = PPO2(MlpPolicy, env, verbose=1)
    model.learn(total_timesteps=5000)
    model.save("ppo-robot")
    obs = env.reset()
    while True:
        action, _states = model.predict(obs)
        obs, rewards, done, info = env.step(action)
        print(action, rewards, info)
        if done:
            break


def continue_training():
    # continue training from previous trained model
    env = make_vec_env('Robot-v0', n_envs=1)
    model = PPO2.load("ppo-robot")
    model.set_env(env)
    model.learn(total_timesteps=1000)
    model.save("ppo-robot")
    obs = env.reset()
    while True:
        action, _states = model.predict(obs)
        obs, rewards, done, info = env.step(action)
        print(action, rewards, info)
        if done:
            break

def getSum(image):
    image = cv2.imread("gym_env/envs/" + image + ".png")
    plt.hist(np.ndarray.flatten(image))
    placeholder = image
    placeholder[placeholder > 245] = 0
    flat_non_zero = placeholder[np.nonzero(placeholder)]
    val = stats.mode(flat_non_zero, axis = None)
    image[image > 245] = val[0]
    plt.hist(np.ndarray.flatten(image))
    plt.show()
    score = cv2.sumElems(image)
    s = sum(list(score))
    return s, val[0]

def getScore(image1, image2):
    image1 = io.imread("gym_env/envs/" + image1 + ".png")
    image2 = io.imread("gym_env/envs/" + image2 + ".png")
    img1 = color.rgb2gray(image1)
    img2 = color.rgb2gray(image2)
    (score, diff) = compare_ssim(img1, img2, full=True)
    return score


# print(getSum("115"))
# print(getScore("233", "238"))
# train_new()
# continue_training()

