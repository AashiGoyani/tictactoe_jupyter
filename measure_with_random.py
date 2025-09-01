"""
Training Functions for Tic-Tac-Toe RL
Contains evaluation functions for measuring agent performance.
"""

from game_logic import play, PLAYER_X, PLAYER_O, EMPTY
from agents import RandomPlayer, Agent

def measure_performance_vs_random(agent1, agent2, games=100):
    """
    Measure performance of two agents vs random players like og.py
    Returns [P1-Win, P1-Lose, P1-Draw, P2-Win, P2-Lose, P2-Draw] probabilities
    """
    # Save original settings
    epsilon1 = agent1.epsilon
    epsilon2 = agent2.epsilon
    learning1 = agent1.learning
    learning2 = agent2.learning
    
    # Set agents to pure exploitation mode
    agent1.epsilon = 0
    agent2.epsilon = 0
    agent1.learning = False
    agent2.learning = False
    
    # Create random agents
    r1 = Agent(PLAYER_X, learning=False)
    r2 = Agent(PLAYER_O, learning=False)
    r1.epsilon = 1
    r2.epsilon = 1
    
    probs = [0, 0, 0, 0, 0, 0]
    
    # Test agent1 vs random agent2
    for _ in range(games):
        winner = play(agent1, r2)
        if winner == PLAYER_X:
            probs[0] += 1.0 / games  # P1-Win
        elif winner == PLAYER_O:
            probs[1] += 1.0 / games  # P1-Lose
        else:
            probs[2] += 1.0 / games  # P1-Draw
    
    # Test random agent1 vs agent2
    for _ in range(games):
        winner = play(r1, agent2)
        if winner == PLAYER_O:
            probs[3] += 1.0 / games  # P2-Win
        elif winner == PLAYER_X:
            probs[4] += 1.0 / games  # P2-Lose
        else:
            probs[5] += 1.0 / games  # P2-Draw
    
    # Restore original settings
    agent1.epsilon = epsilon1
    agent2.epsilon = epsilon2
    agent1.learning = learning1
    agent2.learning = learning2
    
    return probs