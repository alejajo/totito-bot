#############
### main ####
#############

import utis
import time

def main():
    name = "Alejandro"
    player_id = utis.register(name)
    print(player_id)

    my_turn = utis.is_my_turn(player_id)

    while not my_turn:
        time.sleep(3)
        my_turn = utis.is_my_turn(player_id)

    print("Its my turn, continue in game   ")
    print(my_turn)

if __name__ == "___main___":
      main()