import gym
import gym_env
from stable_baselines.common import make_vec_env
from stable_baselines.common.policies import MlpPolicy
from stable_baselines.common.policies import CnnPolicy
from stable_baselines import A2C

env = make_vec_env('Robot-v0', n_envs=4)
model = A2C(CnnPolicy, env, verbose=1)
model.learn(total_timesteps=100)
model.save("a2c-robot")
del model
model = A2C.load("a2c-robot")
print("load")
obs = env.reset()
while True:
    action, _states = model.predict(obs)
    obs, rewards, dones, info = env.step(action)
    print(action, info)
