import gym
import gym_env
from stable_baselines.common import make_vec_env
from stable_baselines.common.policies import MlpPolicy, CnnPolicy
from stable_baselines import A2C, PPO2


def train_new():
    # train from the beginning
    env = make_vec_env('Robot-v0', n_envs=1)
    # n_steps default = 128
    # halving to address resource exhausted error
    model = PPO2(CnnPolicy, env, n_steps=64, verbose=1)
    model.learn(total_timesteps=1000)
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


# train_new()
continue_training()
