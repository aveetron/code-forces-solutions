total_games = int(input())
game_result = input()

anton_won = 0
danik_won = 0

for game in game_result:
    if game == "A":
        anton_won = anton_won + 1
    elif game == "D":
        danik_won = danik_won + 1

if anton_won > danik_won:
    print("Anton")
elif anton_won < danik_won:
    print("Danik")
elif anton_won == danik_won:
    print("Friendship")