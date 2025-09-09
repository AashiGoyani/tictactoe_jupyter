# Role Switch Comparison: 10K vs 100K Training

## What is Role Switching?
- **Agent X**: Trained to play first, tested playing second
- **Agent O**: Trained to play second, tested playing first
- **Purpose**: See how well agents adapt to opposite positions

## Visual Analysis: Training Comparison Graphs

### 100K Training Results (Extended Training)

#### Agent X Position Advantage - 100K Training
![Agent X 100K Training](./photos/agent_x_100k_training.png)

**Key Visual Observations (100K Training - Agent X):**
- **α = 0.01**: 43% final advantage - extremely stable red line, consistent green line
- **α = 0.1**: 42% final advantage - quick convergence with occasional performance dips
- **α = 0.5**: 42% final advantage - moderate volatility throughout training
- **α = 0.99**: 34% final advantage - high volatility, best second-position performance

#### Agent O Position Analysis - 100K Training  
![Agent O 100K Training](./photos/agent_o_100k_training.png)

**Key Visual Observations (100K Training - Agent O):**
- **α = 0.01**: 12% position benefit - blue line reaches 80%+, exceptional normal position development
- **α = 0.1**: 12% position benefit - consistent performance in both positions
- **α = 0.5**: 39% position benefit - balanced improvement across positions
- **α = 0.99**: 48% position benefit - highest adaptability gain, volatile patterns

### 10K Training Results (Standard Training)

#### Agent X Position Advantage - 10K Training
![Agent X 10K Training](./photos/agent_x_10k_training.png)

**Key Visual Observations (10K Training - Agent X):**
- **α = 0.01**: 40% final advantage - still converging, not fully specialized
- **α = 0.1**: 34% final advantage - near complete convergence
- **α = 0.5**: 12% final advantage - quick learning but less stable
- **α = 0.99**: 36% final advantage - high volatility, rapid adaptation

#### Agent O Position Analysis - 10K Training
![Agent O 10K Training](./photos/agent_o_10k_training.png)

**Key Visual Observations (10K Training - Agent O):**
- **α = 0.01**: 33% position benefit - gradual improvement, not fully developed
- **α = 0.1**: 21% position benefit - good balance, stable learning curve
- **α = 0.5**: 33% position benefit - moderate development with some volatility
- **α = 0.99**: 34% position benefit - quick adaptation with high volatility

### Visual Comparison: 100K vs 10K Training

**Key Differences Visible in Graphs:**

1. **Stability**: 100K training shows smoother, more stable convergence patterns
2. **Performance Gaps**: Extended training creates larger position advantages
3. **Convergence**: 10K training often shows incomplete learning, especially for α = 0.01
4. **Volatility**: α = 0.99 maintains high volatility regardless of training duration

## Agent X (First Player) Role Switch Analysis

### Normal Position (Playing First) vs Role Switch (Playing Second)

| Learning Rate | Training Duration | Normal Position | Role Switch | Advantage Lost |
|---------------|-------------------|-----------------|-------------|----------------|
| **α = 0.01**  | 10K episodes     | ~85%           | ~55%        | **30%**        |
|               | 100K episodes    | ~95%           | ~50%        | **45%** ⬇️     |
| **α = 0.1**   | 10K episodes     | ~90%           | ~60%        | **30%**        |
|               | 100K episodes    | ~95%           | ~55%        | **40%** ⬇️     |
| **α = 0.5**   | 10K episodes     | ~85%           | ~58%        | **27%**        |
|               | 100K episodes    | ~90%           | ~55%        | **35%** ⬇️     |
| **α = 0.99**  | 10K episodes     | ~80%           | ~55%        | **25%**        |
|               | 100K episodes    | ~85%           | ~60%        | **25%** ➡️     |




### Key Findings for Agent X:
- **Extended training makes X MORE specialized** (worse at role switching)
- **Exception**: α = 0.99 maintains same adaptability
- **Best role switcher**: α = 0.99 (60% when playing second)
- **Worst role switcher**: α = 0.01 with 100K training (only 50%)

## Agent O (Second Player) Role Switch Analysis

### Normal Position (Playing Second) vs Role Switch (Playing First)

| Learning Rate | Training Duration | Normal Position | Role Switch | Benefit Gained |
|---------------|-------------------|-----------------|-------------|----------------|
| **α = 0.01**  | 10K episodes     | ~65%           | ~85%        | **+20%**       |
|               | 100K episodes    | ~80%           | ~90%        | **+10%** ⬇️    |
| **α = 0.1**   | 10K episodes     | ~60%           | ~80%        | **+20%**       |
|               | 100K episodes    | ~65%           | ~85%        | **+20%** ➡️    |
| **α = 0.5**   | 10K episodes     | ~55%           | ~75%        | **+20%**       |
|               | 100K episodes    | ~60%           | ~80%        | **+20%** ➡️    |
| **α = 0.99**  | 10K episodes     | ~50%           | ~80%        | **+30%**       |
|               | 100K episodes    | ~55%           | ~85%        | **+30%** ➡️    |

### Key Findings for Agent O:
- **O agents LOVE playing first** (big performance boost)
- **Extended training maintains role switch benefits**
- **Exception**: α = 0.01 gets so good at normal position that first-move benefit shrinks
- **Best role switcher**: α = 0.99 (+30% improvement)

## Direct Comparison: 10K vs 100K Training Effects

### Agent X Adaptability Impact
```
Role Switch Performance (Playing Second):

10K Training:    100K Training:
α=0.01: 55% ──→  α=0.01: 50% ⬇️ (Less adaptable)
α=0.1:  60% ──→  α=0.1:  55% ⬇️ (Less adaptable)  
α=0.5:  58% ──→  α=0.5:  55% ⬇️ (Less adaptable)
α=0.99: 55% ──→  α=0.99: 60% ⬆️ (More adaptable)
```

### Agent O Adaptability Impact
```
Role Switch Performance (Playing First):

10K Training:    100K Training:
α=0.01: 85% ──→  α=0.01: 90% ⬆️ (Better at both!)
α=0.1:  80% ──→  α=0.1:  85% ⬆️ (Improved)
α=0.5:  75% ──→  α=0.5:  80% ⬆️ (Improved)
α=0.99: 80% ──→  α=0.99: 85% ⬆️ (Improved)
```

## Summary: Extended Training Effects on Role Switching

### Agent X (First Player):
- **Extended training makes X more specialized** = worse at role switching
- **Trade-off**: Better at normal position, worse at adaptation
- **Only exception**: α = 0.99 becomes more adaptable with extended training

### Agent O (Second Player):
- **Extended training helps O in BOTH positions**
- **No trade-off**: Better at normal position AND better at role switching
- **Consistent benefit**: All learning rates improve with extended training

