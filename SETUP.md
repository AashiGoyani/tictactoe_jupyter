# Setup Instructions

## Quick Start

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd tictactoe_jupyter
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run Jupyter Notebook**
   ```bash
   jupyter notebook
   ```

4. **Start with the main analysis**
   - Open `tictactoe_position_analysis.ipynb` for complete experiments
   - Open `tictactoe_experiments.ipynb` for basic experiments

## Project Structure
```
tictactoe_jupyter/
├── agents.py                           # RL agents implementation
├── game_logic.py                       # Tic-tac-toe game mechanics  
├── measure_with_random.py              # Performance evaluation
├── tictactoe_experiments.ipynb         # Basic alpha comparison
├── tictactoe_position_analysis.ipynb   # Position switching analysis
├── README.md                           # Project documentation
├── requirements.txt                    # Python dependencies
└── .gitignore                          # Git ignore rules
```

## Key Features

- **Q-learning agents** with configurable learning rates
- **Position switching analysis** (role reversal experiments)
- **Alpha comparison** across multiple learning rates
- **Interactive gameplay** against trained agents
- **Comprehensive visualizations** of learning curves

## Results Summary

- **Optimal learning rate**: α = 0.1 for both agents
- **First-player advantage**: 34-43% across all settings
- **Role switching effects**: X suffers penalty, O benefits from switching
- **Learning stability**: Higher alphas cause volatility, especially for O agent
