from lib.villager import *

def make_characters(player_count=3, villager_count=3, existing_names=[]):

    # Create players
    players = []
    player_names = list(existing_names)

    for i in range(player_count):
        players.append(Villager(player_names))

    # Create villagers
    villagers = []
    villager_names = list(player_names)

    for i in range(villager_count):
        villagers.append(Villager(villager_names))

    # Create player bonds
    player_names = list(set(player_names)-set(existing_names))
    for c in players:
        c.create_player_bond(player_names, villager_names)

    # Create villager to player bonds
    for c in villagers:
        c.create_villager_bond(player_names)

    # Create villager bonds
    for c in villagers:
        c.create_villager_bond(villager_names)

    villager_names = list((set(villager_names)-set(player_names))-set(existing_names))

    print('Players:', player_names, 'New Villagers:', villager_names, 'Old Villagers:', existing_names)
    print()

    for c in players + villagers:
        c.print()
   
def get_input():
    print('How many player characters to generate: ', end='')
    PCs = int(input())
    print('How many non-player characters to generate: ', end='')
    NPCs = int(input())
    print('Enter any existing villagers, seperated by space: ', end='')
    old_villagers = input().split(' ')
    old_villagers = list(set([x for x in old_villagers if x != '']))

    make_characters(PCs, NPCs, old_villagers)

get_input()
