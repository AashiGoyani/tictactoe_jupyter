# Tic-Tac-Toe Reinforcement Learning Experiments

This repository contains comprehensive reinforcement learning experiments analyzing how learning rates (alpha values) and role switching affect agent performance in tic-tac-toe.

## 📁 File Structure & Contents

### **Core Implementation Files**
| File | Purpose | Key Contents |
|------|---------|--------------|
| `agents.py` | Agent classes | Q-learning Agent, Human player, RandomPlayer, Teacher with optimal strategy |
| `game_logic.py` | Game mechanics | Board representation, game rules, win detection, state management |
| `measure_with_random.py` | Evaluation functions | Performance measurement against random opponents |

### **Experiment Notebooks**
| File | Purpose | Key Experiments |
|------|---------|-----------------|
| `tictactoe_experiments.ipynb` | Basic RL experiments | Alpha comparison (0.01, 0.1, 0.5, 0.99), agent vs random evaluation |
| `tictactoe_position_analysis.ipynb` | **Main analysis notebook** | Position switching experiments, role reversal analysis, comprehensive graphs |



### **Additional Files**
| File | Purpose | Contents |
|------|---------|----------|
| `README.md` | This file | Project overview and file descriptions |
| `__init__.py` | Python package marker | Makes directory a Python package |

## 🎯 Key Experiments Conducted

### **1. Alpha Value Comparison**
- **Purpose**: Test how learning rates affect agent performance
- **Alpha values tested**: 0.01, 0.1, 0.5, 0.99
- **Training**: 10,000 episodes against teachers (90% optimal play)
- **Evaluation**: Performance vs random players every 10 episodes

### **2. Position/Role Switching Analysis**
- **Agent1 (X-trained)**: Compare normal position (X) vs switched position (O)
- **Agent2 (O-trained)**: Compare normal position (O) vs switched position (X)
- **Purpose**: Understand role specialization and transfer learning

### **3. Performance Metrics**
- Win/Loss/Draw rates against random opponents
- Training performance against teachers
- Position advantage quantification
- Learning stability analysis

## 📊 Key Findings Summary

### **Optimal Learning Rate**
- **α = 0.1** provides best balance of learning speed and stability for both agents

### **Position Effects**
- **First-player advantage**: 34-43% advantage across all learning rates
- **X agent**: 37-44% performance drop when switching to second position
- **O agent**: 11-43% performance improvement when switching to first position

### **Alpha Sensitivity**
- **X agent**: Robust performance (95-96%) across all alpha values
- **O agent**: Highly sensitive (46-73% range depending on alpha)

## 🚀 How to Use This Repository

### **1. Start with the Main Analysis**
```
📊 View: tictactoe_position_analysis.ipynb (main experiments with position switching graphs)
🧪 Basic: tictactoe_experiments.ipynb (basic alpha comparison experiments)
```

### **2. Run Experiments**
```
🧪 Basic experiments: tictactoe_experiments.ipynb
🔬 Position analysis: tictactoe_position_analysis.ipynb
```

### **3. Understand Implementation**
```
🤖 Agent logic: agents.py
🎮 Game mechanics: game_logic.py
📏 Evaluation: measure_with_random.py
```

## 📈 Graph Interpretations

### **Position Advantage Graphs** (tictactoe_position_analysis.ipynb)
- **Red/Blue lines**: Agent playing in trained position
- **Green lines**: Agent playing in switched position
- **Filled areas**: Show advantage/disadvantage magnitude
- **4 subplots**: One for each alpha value (0.01, 0.1, 0.5, 0.99)

### **Performance Trends**
- **Stable lines**: Good learning with low volatility
- **Volatile lines**: Unstable learning (problematic with high alpha)
- **Higher lines**: Better win rates
- **Gaps between lines**: Position specialization strength


## 📋 Requirements

- Python 3.x
- Jupyter Notebook
- matplotlib
- numpy
- Standard Python libraries (random, csv)

## 🔍 Research Applications

This work demonstrates:
- **Hyperparameter sensitivity** in reinforcement learning
- **Position bias** in strategic games
- **Transfer learning** limitations between game roles
- **Learning rate optimization** for different player positions

Perfect for understanding RL fundamentals, game theory, and the importance of hyperparameter tuning in machine learning applications.
