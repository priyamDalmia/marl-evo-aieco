import os
import sys
from ai_economist import foundation
import numpy as np
import pdb
import matplotlib.pyplot as plt 
sys.path.append(os.getcwd())
from data import plotting

""" A simple scenario.
"""

# CONFIG for the free market economy!
env_config = {
        # SCENARIO class
        'scenario_name': 'layout_from_file/simple_wood_and_stone',
        # COMPONENTS
        'components': [
            ('Build', {'skill_dist': "pareto", 'payment_max_skill_multiplier':3}),
            ('ContinuousDoubleAuction', {'max_num_orders': 5}),
            ('Gather', {}),
            ],
        # SCENARIO CLASS ARGUMENTS 
        'env_layout_file': 'quadrant_25x25_20each_30clump.txt',
        'starting_agent_coin': 10,
        'fixed_four_skill_and_loc': True,
        # STANDARD ARGUMENTS 
        'n_agents': 4,
        'world_size': [25, 25],
        'episode_length': 1000,
        # MULTI-ACTION MODE
        'multi_action_mode_agents': False,
        'multi_action_mode_planner': True,
        # OBSERVATION PRE-PROC
        'flatten_observations': False,
        'flatten_masks': True,
        }

def sample_random_action(agent, mask):
    """Sample random UNMASKED action(s) for agent."""
    # Return a list of actions: 1 for each action subspace
    if agent.multi_action_mode:
        split_masks = np.split(mask, agent.action_spaces.cumsum()[:-1])
        return [np.random.choice(np.arange(len(m_)), p=m_/m_.sum()) for m_ in split_masks]

    # Return a single action
    else:
        return np.random.choice(np.arange(agent.action_spaces), p=mask/mask.sum())

def sample_random_actions(env, obs):
    """Samples random UNMASKED actions for each agent in obs."""
        
    actions = {
        a_idx: sample_random_action(env.get_agent(a_idx), a_obs['action_mask'])
        for a_idx, a_obs in obs.items()
    }

    return actions

def render(env):
    breakpoint()
    fig, ax = plt.subplots(1, 1, figsize=(10, 10))
    plotting.plot_env_state(env, ax)
    ax.set_aspect('equal')


if __name__ == "__main__":
    # Initalize Env instance
    env = foundation.make_env_instance(**env_config)
    print("ENV OBJECT: ",env)
    # get agents from the env
    agent_0 = env.get_agent(0)
    # reset the environment
    obs = env.reset()
    actions = sample_random_actions(env, obs)
    obs, rew, done, info = env.step(actions)
    render(env)
    


