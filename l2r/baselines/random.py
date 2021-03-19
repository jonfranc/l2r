# ========================================================================= #
# Filename:                                                                 #
#    random.py                                                              #
#                                                                           #
# Description:                                                              # 
#    an agent that randomly chooses actions                                 #
# ========================================================================= #

from core.templates import AbstractAgent
from envs.env import RacingEnv

class RandomActionAgent(AbstractAgent):
	"""Reinforcement learning agent that simply chooses random actions.

	:param dict training_kwargs: training keyword arguments
	"""
	def __init__(self, training_kwargs):
		self.num_episodes = training_kwargs['num_episodes']

	def race(self):
		"""Demonstrative training method. 
		"""
		for e in range(self.num_episodes):
			print('='*10+f' Episode {e+1} of {self.num_episodes} '+'='*10)
			ep_reward, ep_timestep = 0, 0
			state, done = self.env.reset(), False

			while not done:
				action = self.select_action()
				state, reward, done, info = self.env.step(action)
				ep_reward += reward
				ep_timestep += 1

			print(f'Completed episode with total reward: {ep_reward}')
			print(f'Episode info: {info}\n')
		
	def select_action(self):
		"""Select a random action from the action space.

		:return: random action to take
		:rtype: numpy array
		"""
		return self.env.action_space.sample()

	def create_env(self, env_kwargs, sim_kwargs):
		"""Instantiate a racing environment

		:param dict env_kwargs: environment keyword arguments
		:param dict sim_kwargs: simulator setting keyword arguments
		"""
		self.env = RacingEnv(
			max_timesteps=env_kwargs['max_timesteps'],
			obs_delay=env_kwargs['obs_delay'],
			not_moving_timeout=env_kwargs['not_moving_timeout'],
			controller_kwargs=env_kwargs['controller_kwargs'],
			reward_pol=env_kwargs['reward_pol'],
			reward_kwargs=env_kwargs['reward_kwargs'],
			action_if_kwargs=env_kwargs['action_if_kwargs'],
			camera_if_kwargs=env_kwargs['camera_if_kwargs'],
			pose_if_kwargs=env_kwargs['pose_if_kwargs'],
			logger_kwargs=env_kwargs['pose_if_kwargs']
		)

		self.env.make(
			level=sim_kwargs['racetrack'],
			multimodal=env_kwargs['multimodal'],
			driver_params=sim_kwargs['driver_params'],
			camera_params=sim_kwargs['camera_params'],
			sensors=sim_kwargs['active_sensors']
		)
