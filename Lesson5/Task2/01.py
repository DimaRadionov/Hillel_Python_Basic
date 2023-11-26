chess_players = {
    "Carlsen, Magnus": 1865,
    "Firouzja, Alireza": 2804,
    "Ding, Liren": 2799,
    "Caruana, Fabiano": 1792,
    "Nepomniachtchi, Ian": 2773
}

new_chess_players = {value: f"{name.split(', ')[0]} {name.split(', ')[1][0]}."
                     for name, value in chess_players.items() if value > 2000}

print(new_chess_players)
