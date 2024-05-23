from rlgym_environment import RLGymEnvironment

env = RLGymEnvironment()

class MyAgent(object):
    def __init__(self):
        # ... your agent's initialization code

    def act(self, obs):
        # ... your agent's logic to choose an action based on observation 'obs'
        return action


agent = MyAgent()
env.run(agent)
