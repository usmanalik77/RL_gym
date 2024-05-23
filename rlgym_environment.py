import rlgym
import time
import readchar  # Assuming you've installed the 'readchar' library

class RLGymEnvironment(object):
    """
    A class that encapsulates interaction with an RL Gym environment,
    providing data collection and logging capabilities.
    """

    def __init__(self):
        self.env = rlgym.make()
        self.observations = []  # List to store observations
        self.rewards = []  # List to store step rewards
        self.actions = []  # List to store chosen actions

    def run(self, agent):
        """
        Runs an episode in the environment using the provided agent,
        collecting and logging observations, rewards, actions, and key presses.

        Args:
            agent (object): An object representing your reinforcement learning agent.
                It should have a `act(self, obs)` method that takes the observation
                from the environment and returns an action.
        """

        while True:
            obs = self.env.reset()
            done = False
            steps = 0
            ep_reward = 0
            t0 = time.time()
            key_presses = []  # List to store key presses during the episode

            while not done:
                # Capture key presses while the environment is active
                key = readchar.readkey()
                if key != '':  # Only record non-empty key presses
                    key_presses.append(key)

                actions = agent.act(obs)  # Replace with your agent's act method
                new_obs, reward, done, _ = self.env.step(actions)
                ep_reward += reward
                obs = new_obs
                steps += 1

                self.observations.append(obs)  # Store observation data
                self.rewards.append(reward)  # Store step reward data
                self.actions.append(actions)  # Store chosen action data

            length = time.time() - t0
            print("Step time: {:1.5f} | Episode time: {:.2f} | Episode Reward: {:.2f}".format(length / steps, length, ep_reward))

            # Clear episode-specific data after each episode
            key_presses.clear()

            # Optional: Implement logic to log or analyze collected data here
            #   e.g., save data to a file, visualize key press patterns
            #   with respect to observations, rewards, and actions
