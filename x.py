import os
import gym
from stable_baselines3 import PPO
from stable_baselines3.common.vec_env import DummyVecEnv
from stable_baselines3.common.evaluation import evaluate_policy
import numpy as np
environment_name='CartPole-v0'
env=gym.make(environment_name,render_mode='human')

episodes=5
for episode in range(1,episodes+1):
    state=env.reset()
    done=False
    score=0
    
    while not done:
        env.render()
        action = env.action_space.sample()
        n_state, reward, done, _, info = env.step(action)
        score += reward
        print('Episode: {} Score:{}'.format(episode, score))
env.close()