import logging
import gym.envs.registration import register

logger = logging.getLogger(__name__)

register(
        id='Robot-v0',
        entry_point='gym_env.envs:RobotEnv'
)
