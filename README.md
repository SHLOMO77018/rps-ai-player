# Rock Paper Scissors - Machine Learning Challenge

This project implements an intelligent Rock Paper Scissors player that can defeat four different AI bots with a win rate of at least 60% against each.

## 🎯 Challenge Overview

The goal is to create a program that plays Rock, Paper, Scissors against four different bots:
- **Quincy**: Repeats a fixed pattern (R, R, P, P, S)
- **Abbey**: Analyzes pairs of moves to predict opponent's next move
- **Kris**: Always counters the opponent's last move
- **Mrugesh**: Counters the most frequent move in the last 10 plays

## 🧠 Solution Approach

The solution uses a **Markov Chain** approach inspired by [this Medium article](https://medium.com/%40sri.hartini/rock-paper-scissors-in-python-5173ab69ca7a):

### How It Works

1. **Pattern Recognition**: Analyzes the last 5 moves of the opponent
2. **Frequency Analysis**: Tracks how often different move sequences occur
3. **Prediction**: Predicts the opponent's next move based on historical patterns
4. **Counter Strategy**: Plays the move that beats the predicted move

### Key Features

- **Adaptive Learning**: Learns opponent patterns during gameplay
- **Markov Chain Model**: Uses 5-move sequences for prediction
- **Fallback Strategy**: Uses intelligent assumptions when insufficient data

## 📊 Performance Results

| Bot | Win Rate | Strategy |
|-----|----------|----------|
| Quincy | 99.7% | Pattern recognition of fixed sequence |
| Abbey | 61.2% | Markov chain analysis of move pairs |
| Kris | 95.9% | Unpredictable cycling pattern |
| Mrugesh | 83.7% | Frequency analysis counter |

## 🚀 Usage

### Running the Game

```bash
python main.py
```

This will play 1000 games against each bot and display the results.

### Testing

```bash
python -m unittest test_module -v
```

Runs the unit tests to verify all bots are defeated with ≥60% win rate.

### Interactive Play

Uncomment the following line in `main.py` to play interactively:

```python
play(human, abbey, 20, verbose=True)
```

## 📁 Project Structure

```
├── RPS.py              # Main player function
├── RPS_game.py         # Game engine and bot implementations
├── main.py             # Entry point and testing
├── test_module.py      # Unit tests
└── README.md           # This file
```

## 🔧 Technical Details

### Player Function

The main `player()` function in `RPS.py` implements the Markov chain strategy:

```python
def player(prev_play, opponent_history=[], play_order={}):
    # Initialize with assumption that opponent plays 'R' first
    if not prev_play:
        prev_play = 'R'
    
    opponent_history.append(prev_play)
    
    # Assume opponent will play paper initially
    prediction = 'P'
    
    # Analyze patterns when we have enough data
    if len(opponent_history) > 4:
        # Record 5-move patterns
        last_five = "".join(opponent_history[-5:])
        play_order[last_five] = play_order.get(last_five, 0) + 1
        
        # Predict next move based on 4-move sequences
        potential_plays = [
            "".join([*opponent_history[-4:], v]) 
            for v in ['R', 'P', 'S']
        ]
        
        # Choose most frequent pattern
        sub_order = {
            k: play_order[k]
            for k in potential_plays if k in play_order
        }
        
        if sub_order:
            prediction = max(sub_order, key=sub_order.get)[-1:]
    
    # Counter the predicted move
    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
    return ideal_response[prediction]
```

### Bot Strategies

1. **Quincy**: Fixed pattern `["R", "R", "P", "P", "S"]` - easily predictable
2. **Abbey**: Analyzes move pairs using Markov chains - most sophisticated
3. **Kris**: Simple counter to last move - vulnerable to unpredictable patterns
4. **Mrugesh**: Counters most frequent move in last 10 - vulnerable to balanced play

## 🎓 Learning Outcomes

This project demonstrates:
- **Pattern Recognition**: Identifying and exploiting opponent weaknesses
- **Markov Chains**: Using historical data for prediction
- **Game Theory**: Developing counter-strategies
- **Machine Learning**: Adaptive algorithms that learn during gameplay

## 📚 References

- [Rock Paper Scissors in Python - Medium Article](https://medium.com/%40sri.hartini/rock-paper-scissors-in-python-5173ab69ca7a)
- FreeCodeCamp Machine Learning with Python Certification

## 🤝 Contributing

Feel free to submit issues and enhancement requests!

## 📄 License

This project is part of the FreeCodeCamp Machine Learning curriculum.
