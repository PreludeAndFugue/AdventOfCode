#!python3

'''
459 players; last marble is worth 71790 points
'''

from collections import defaultdict

PLAYERS = 459
MARBLES = 71790
SPECIAL = 23


def find_new_index(game, current_marble):
    current_marble_index = game.index(current_marble)
    new_index = (current_marble_index + 2) % len(game)
    if new_index == 0:
        return len(game)
    else:
        return new_index
        
        
def get_player_no(i, total=PLAYERS):
    player_no = i % total
    if player_no == 0:
        return total
    else:
        return player_no


def main():
    pass
    
    
def test():
    game = [0]
    current_marble = 0
    players = defaultdict(list)
    for i in range(1, 26):
        
        if i % 23 == 0:
            player_no = get_player_no(i, 9)
            players[player_no].append(i)
        
        new_index = find_new_index(game, current_marble)
        game.insert(new_index, i)
        current_marble = i
        print(get_player_no(i, 9), game)
        
    print(players)
    
    
if __name__ == '__main__':
    main()
    
    test()
