from src.constants import *
from src.utils import *


# Main Q-learning agent function
def q_learning_agent(agent_id, obstacles, bonus_cells, start_pos, target_pos):
    # Initialize exploration factor, maximum reward, and best path
    epsilon = 0.9
    max_reward = -2147483648
    best_path = []

    # Initialize Q-table with zeros
    q_table = np.zeros(grid_size + (num_bonus_cells + 1,) + (len(actions),)).copy()

    # Loop through multiple episodes
    for episode in range(n_episodes_for_each_agent):
        # Display episode number
        if episode % 1000 == 0 or episode == n_episodes_for_each_agent - 1:
            print(f'(Agent {agent_id}) Episode {episode + 1}/{n_episodes_for_each_agent}')

        # Initialize start state
        state = start_pos + (0,)
        state_pos = start_pos

        # Create a set to store collected bonuses
        collected_bonuses = set()
        # Initialize total_reward and path
        total_reward = 0
        path = []

        # Keep running the episode until the target is reached and all bonuses are collected
        while not(state[:2] == target_pos and len(collected_bonuses) == num_bonus_cells) and len(path) < 10000:
            # Choose an action based on the current state and Q-table values
            action = choose_action(state, q_table, epsilon)
            # Calculate the next state after taking the action
            next_state = get_next_state(state, action, obstacles, len(collected_bonuses))
            next_state_pos = next_state[:2]

            # Determine the reward
            if next_state_pos == target_pos and len(collected_bonuses) == num_bonus_cells:
                reward = 100
            elif next_state_pos in obstacles or next_state_pos == state_pos:
                reward = -20
            elif next_state_pos in bonus_cells and next_state_pos not in collected_bonuses:
                reward = 5

                # Add the bonus cell to the collected bonuses set
                collected_bonuses.add(next_state_pos)
            else:
                reward = -1

            # Update the Q-value using the Q-learning update equation
            q_old = q_table[state + (actions.index(action),)]
            q_next_max = np.max(q_table[next_state])
            q_table[state + (actions.index(action),)] = q_old + alpha * (reward + gamma * q_next_max - q_old)

            # Update the current state, total_reward, and path
            state = next_state
            state_pos = state[:2]

            total_reward += reward

            path.append(state_pos)

        # Update max_reward and best_path if the current episode has better performance
        max_reward = max(max_reward, total_reward)

        if total_reward == max_reward:
            best_path = path

        # Update epsilon (decrease exploration as the agent learns)
        epsilon = max(epsilon * 0.99, 0.2)

    # Return the maximum reward, Q-table, and best path
    return max_reward, q_table, best_path
