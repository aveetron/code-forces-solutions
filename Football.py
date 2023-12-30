players = input()
total = 0
last_player = players[0]

for player in players:
    if total == 7:
        break
    else:
        pass

    if player == last_player:
        total = total + 1
    else:
        total = 1
        last_player = player

if total == 7:
    print("YES")
else:
    print("NO")
    
