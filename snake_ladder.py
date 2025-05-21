'''
Snake and ladder Interview Ascendeum


'''
import random
import pandas as pd

players = {'player1': 0, 'player2': 0, 'player3': 0}

def snake_and_ladder(grid_size):
    history = {player: [] for player in players}
    winner = None
    grid_limit = grid_size * grid_size

    while not winner:
        for player in players:
            roll = random.randint(1, 6)
            current_pos = players[player]
            new_pos = current_pos + roll

            if new_pos == grid_limit:
                players[player] = new_pos
                history[player].append({
                    "Dice Roll History": roll,
                    "Position History": new_pos,
                    "Winner Status": "Winner"
                })
                winner = player
                break
            elif new_pos > grid_limit:
                history[player].append({
                    "Dice Roll History": roll,
                    "Position History": "NA",
                    "Winner Status": ""
                })
                continue
            else:
                players[player] = new_pos

                # Cut other players if on same square
                for opponent in players:
                    if opponent != player and players[opponent] == new_pos:
                        players[opponent] = 0

                history[player].append({
                    "Dice Roll History": roll,
                    "Position History": new_pos,
                    "Winner Status": ""
                })

    # Combine data into single loop
    df_data = []
    for player in players:
        rolls = [entry["Dice Roll History"] for entry in history[player]]
        positions = [entry["Position History"] for entry in history[player]]
        status = "Winner" if player == winner else ""
        df_data.append({
            "Player": player,
            "Dice Roll History": rolls,
            "Position History": positions,
            "Winner Status": status
        })

    return winner, pd.DataFrame(df_data)

winner, df = snake_and_ladder(3)

print(f"Winner: {winner}\n")
print(df)
