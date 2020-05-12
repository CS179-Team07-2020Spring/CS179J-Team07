from gym.envs.registration import register

register(
        id='Robot-v0',
        entry_point='gym_env.envs:RobotEnv'
        max_episode_steps=200
        reward_threshold=195.0
)
