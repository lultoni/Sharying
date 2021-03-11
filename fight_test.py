from random import randint
from fight_test_save import fights, wins, losses, xp

player_won = False
player_lost = False


class Player:
    def __init__(self, hp, dmg, block, heal, ap):
        self.hp = hp
        self.dmg = dmg
        self.block = block
        self.heal = heal
        self.ap = ap


class Enemy:
    def __init__(self, hp, dmg, block, heal):
        self.hp = hp
        self.dmg = dmg
        self.block = block
        self.heal = heal


def fight():
    global fgt_tf
    fgt_tf = True
    Enemy.hp = randint(80, 120)
    Player.hp = randint(80, 120)
    Player.ap = 3
    print("type 'fhelp' for lists of commands")


def attacking():
    Player.dmg = randint(20, 30)
    Enemy.block = randint(23, 31)
    if Player.dmg > Enemy.block:
        print("The Enemy didn't focus.")
        Enemy.hp -= Player.dmg
        print(f"You dealt {Player.dmg} damage.")
    else:
        print("You missed and dealt no damage.")
        Player.ap -= 1


def blocking():
    Enemy.dmg = randint(20, 30)
    Player.block = randint(20, 30)
    if Enemy.dmg > Player.block:
        print("Your fingers slipped.")
        Player.hp -= Enemy.dmg
        print(f"You took {Enemy.dmg} damage. Hp: {Player.hp}")
    else:
        print("You blocked the attack.")
        Player.ap += 1


def healing():
    Player.hp += randint(7, 15)
    Enemy.hp += randint(10, 20)
    Player.ap += 1


def fighting_help():
    print("Fighting commands:")
    for cmd in Commands_fights.keys():
        print(f"    {cmd}")


Commands_fights = {
    "attack": attacking,
    "block": blocking,
    "heal": healing,
    "fhelp": fighting_help,
}


def print_help():
    print("Commands:")
    for cmd in Commands.keys():
        print(f"    {cmd}")


def leave():
    print("Autosaving...")
    s = open("fight_test_save.py", "w")
    s.write(f"fights = {fights}\n"
            f"wins = {wins}\n"
            f"losses = {losses}\n"
            f"xp = {xp}\n")
    s.close()
    print("Save succsesfull")
    exit()


def stats():
    print(f"fights = {fights}\n"
          f"wins = {wins}\n"
          f"losses = {losses}\n"
          f"xp = {xp}\n")


Commands = {
    'exit': leave,
    'leave': leave,
    'stats': stats,
    'help': print_help,
    'fight': fight,
}

stats()
print("type 'help' for the commands")
while True:
    fgt_tf = False
    command = input("> ").lower().split(" ")
    if command[0] in Commands:
        Commands[command[0]]()
    else:
        print("That is not an option.")
    while fgt_tf:

        if Enemy.hp <= 0:
            fgt_tf = False
            fights += 1
            wins += 1
            tmp_xp = randint(5, 10)
            xp += tmp_xp
            print(f"You won and gained {tmp_xp} xp.\nTotal xp: {xp}")
            player_won = True
        elif Player.hp <= 0:
            fgt_tf = False
            fights += 1
            losses += 1
            print("You lost")
            player_lost = True
        elif Player.ap == 0:
            blocking()
        elif player_won is False and player_lost is False:
            print(f"Ap: {Player.ap}   Hp: {Player.hp}\nEnemy Hp: {Enemy.hp}")
            command = input("> ").lower().split(" ")
            if command[0] in Commands_fights:
                Commands_fights[command[0]]()
            else:
                print("That is not an option.")
        if player_won is True or player_lost is True:
            player_won = False
            player_lost = False
