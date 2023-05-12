import multiprocessing

from src.constants import *
from src.agent import q_learning_agent


# Define the main train function
def train(obstacles, bonus_cells, start_pos, target_pos):
    # Create a process pool with the number of agents
    with multiprocessing.Pool(n_agents) as pool:
        # Use starmap to asynchronously call the q_learning_agent function for each agent ID using the given inputs
        results = pool.starmap(q_learning_agent, [(agent_id, obstacles, bonus_cells, start_pos, target_pos) for agent_id in agent_ids])

    # Sort the results by the agent's total_reward (performance) in descending order
    # and extract the best path from the agent with the highest total_reward
    best_path = sorted(results, key=lambda x: x[0], reverse=True)[0][2]

    # Return the best path found by the agents
    return best_path
