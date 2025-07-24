def player(prev_play, opponent_history=[], play_order={}):
    if not prev_play:
        prev_play = 'R'
    
    opponent_history.append(prev_play)
    
    # Assume opponent will play paper initially (as in the article)
    prediction = 'P'
    
    # If we have enough data (at least 5 moves), start analyzing patterns
    if len(opponent_history) > 4:
        # Record the last 5 moves pattern
        last_five = "".join(opponent_history[-5:])
        play_order[last_five] = play_order.get(last_five, 0) + 1
        
        # Create potential plays based on last 4 moves
        potential_plays = [
            "".join([*opponent_history[-4:], v]) 
            for v in ['R', 'P', 'S']
        ]
        
        # Get the frequency of each potential play
        sub_order = {
            k: play_order[k]
            for k in potential_plays if k in play_order
        }
        
        # If we have data on potential plays, make prediction
        if sub_order:
            prediction = max(sub_order, key=sub_order.get)[-1:]
    
    # Counter the predicted move
    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
    return ideal_response[prediction] 