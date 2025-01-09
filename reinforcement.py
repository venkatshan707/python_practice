import gym
import numpy as np
import warnings
import time

# # Sleep for 3 seconds to simulate a delay before running the code
# time.sleep(0.3)

# Suppress specific deprecation warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

# Load the environment with render mode specified
env = gym.make('CartPole-v1', render_mode="human")

# Initialize the environment to get the initial state
state = env.reset()
print (state)
print(state[0])

# Print the state space and action space
print("State space:", env.observation_space)
print("Action space:", env.action_space)

# Simple policy to move based on pole angle
def simple_policy(state):
    # The state is of the form [cart position, cart velocity, pole angle, pole angular velocity]
    pole_angle = state[2]
    
    # If the pole angle is positive (tilting right), move right (action 1), otherwise move left (action 0)
    if pole_angle > 0:
        return 1  # Move right
    else:
        return 0  # Move left

# Run a few steps in the environment using the simple policy
for _ in range(1000):
    time.sleep(1)  # Slow down the simulation so you can visualize it better
    env.render()  # Render the environment for visualization
    
    # Get the action based on the simple policy
    action = simple_policy(state[0])
    
    # Take a step in the environment
    step_result = env.step(action)
    
    # Check the number of values returned and unpack accordingly
    if len(step_result) == 4:
        next_state, reward, done, info = step_result
        terminated = False
    else:
        next_state, reward, done, truncated, info = step_result
        terminated = done or truncated
    
    # Print relevant information for debugging
    print(f"Action: {action}, Reward: {reward}, Next State: {next_state}, Done: {done}, Info: {info}")
    
    # Reset the environment if the episode is finished
    if terminated:
        state = env.reset()

env.close()  # Close the environment when done
