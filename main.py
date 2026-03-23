import textwrap as text
import time
import random

running = True

class Player:
    # stats
    name: str = ''
    xp: int = 0
    hp: int = 100
    attack: int = 10
    luck: int = 3
    gold: int = 200

    inventory = []

    # name : [description, power, ability, value]
    possible_player_inventory = {
        'green stone' : ['This stone can be combined with other stones to become more powerful', 5, 'none', 60],
        'red stone' : ['This stone can be combined with other stones to become more powerful', 7, 'none', 70],
        }

class Enemy:
    # id : [name, type, attack, hp, ability]
    enemies = {
        0 : ['witch', 'unique', 10, 50, None]
    }

def show_inventory(inventory):
    for index, inventory_item in enumerate(inventory,1):
        print(f'{index}> {inventory_item}')
    # for index, item in enumerate(inventory,1):
    #     print(f'{index}> {item}')

def battle(enemy):
    battling = True
    print('\nWould you like to equip any of the following?\n')
    show_inventory(Player.inventory)
    equipped = int(input())
    if len(Player.inventory) > 0:
        item_name = Player.inventory[equipped-1]
        player_bonus_dmg = Player.possible_player_inventory[item_name][1]
        print(f'bonus dmg = {player_bonus_dmg}')

    while battling and Player.hp > 0 and enemy[3] > 0:
        # Player attack
        player_roll = random.randrange(1,7)
        print(f'You attack the {enemy[0]}')
        player_damage = Player.attack + player_roll + player_bonus_dmg
        enemy[3] -= player_damage
        print(f'You did {player_damage} damage to the {enemy[0]}')
        print(enemy)
        time.sleep(3)

        if Player.hp > 0:
            # Enemy attack
            enemy_roll = random.randrange(1,7)
            print(f'The {enemy[0]} attacks you!')
            enemy_damage = enemy[2] + enemy_roll
            Player.hp -= enemy_damage
            print(f'The {enemy[0]} did {enemy_damage} damage to you')
            print(Player.hp)
            time.sleep(3)


def intro_machine():
    global running
    dd = text.dedent

    Player.name = input(dd('''
            Greetings traveller!
            Please tell me your name!
                           
            '''))
    print(dd(f'''
             {Player.name}! What a fine strong name!
             I need your help catching the village witch!
             '''))
    player_choice = int(input(dd('''
            What say ye? Up for adventure?
                             
            1> ye
            2> nay
                             
            ''')))
    if int(player_choice) == 1:
        page = int(input(dd(f'''
        So, {Player.name}, welcome to the village of Woodsbury. 
        An evil witch lives in a house on the hill through the Enchanted Oaks northwards.
        There is also another village eastwards that I hear sells charms and weapons.
        Which way should I point you?

        1> Hunt for the witch northwards
        2> Shop for gear in the east village
''')))
        return page
    else:
         running = False


def adventuring(page):
    global running
    dd = text.dedent
    
    
    def shop_menu():
       for_sale = ''
       for index, item in enumerate(list(Player.possible_player_inventory.keys())):
           for_sale += f'{index}: {item} {Player.possible_player_inventory[item][3]}gp \n'
       return for_sale
           

    died_message = dd(f'''
        You died.
        
        << Final Stats >>
        Name: {Player.name}
        xp: {Player.xp}
        hp: {Player.hp}
        attack: {Player.attack}
        luck: {Player.luck}
        gold: {Player.gold}
''')
    

    if page == 1:
        page = print(died_message)
    elif page == 2:
        page = int(input(dd('''
            You arrived at the village of Gooberton.
                             
            3> Shop for gear 
            4> Leave to return to Woodsbury            
            ''')))
    elif page == 3:
        choice = int(input(dd(f'''
"Welcome to the shop, whatchu want?"

The options are: 
{shop_menu()}             
            ''')))
        if choice not in range(0,len(Player.possible_player_inventory)):
            print('Pick one of the available choices!')
            page = 3
        else:
            item_name = list(Player.possible_player_inventory.keys())[choice]
            if Player.possible_player_inventory[item_name][3] > Player.gold:
                print('You aint got the jink, cutter!')
                page = 2
            else:
                Player.gold -= Player.possible_player_inventory[item_name][3]
                Player.inventory.append(item_name)
                print(dd(f'''
                      You sucessfully bought a {item_name}!
                      New gold balance: {Player.gold}
                    '''))
                page = 2
    elif page == 4:
        page = int(input(dd('''
            You have returned to Woodsbury.
            Would you like to hunt that witch?

            5> yes
            2> no, return to Gooberton         
            ''')))
    elif page == 5:
        page = int(input(dd('''
            You have chased down the witch.
            Battle her, or run?

            6> battle her
            7> no, run back to Gooberton         
            ''')))
    elif page == 6:
        battle(Enemy.enemies[0])
        if Player.hp > 0:
            page = 7
        else:
            page = 1
    elif page == 7:
        page = int(input(dd('''
            You have defeated the witch! congratulations!         
            ''')))
    return page
        

page = intro_machine()
while running:
    page = adventuring(page)