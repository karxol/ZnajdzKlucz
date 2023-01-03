from random import randint
from math import sqrt

game_width = 10
game_height = 10 

key_x = randint(0, game_width)
key_y = randint(0, game_height)

player_x = 0
player_y = 0
player_found_key = False
steps = 0 

distance_before_move = sqrt((key_x - player_x) ** 2 + (key_y - player_y) ** 2)

print(key_x,key_y)

while not player_found_key:
    steps +=1
    print()
    print("Mozesz isc w okreslonym kierunku jako [W/A/S/D]: ")

    move = input("dokond idzies: ")
    if move == "W":
        player_y += 1
        if player_y > game_height:
            print("sciana COFNIJ !")
            player_y = game_height

    elif move == "S":
        player_y -= 1
        if player_y < 0:
             print("sciana COFNIJ !")
             player_y = 0
            
    elif move == "A":
        player_x -= 1
        if player_x < 0:
            print("sciana COFNIJ !")
            player_x = 0 

    elif move == "D":
        player_x += 1
        if player_x > game_width:
            print("sciana COFNIJ !")
            player_x = game_width
    
    elif move == "Q":
        print(" KONIEC GRY ")
        break
    
    elif move == "-":
        print(" Nie wiem gdzie idziesz ....")



    distance_after_move = sqrt((key_x - player_x) ** 2 + (key_y - player_y) ** 2)

    if distance_before_move > distance_after_move:
        print(" ")
        print('Jesteś bliżej skarbu')
    else:
        print(" ")
        print("Oddalasz sie od skarbu :(")
    
    distance_before_move = distance_after_move



    if player_x == key_x and player_y == key_y:
        print("Odnalazłeś klucz GRATULUJE")
        print(f"Wykonałeś {steps} ruchów")
        break

    print(f"player_x: {player_x}, player_y: {player_y}\nkey_x :{key_x}, key_y :{key_y}")