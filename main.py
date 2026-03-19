import textwrap as text

running = True

class Player:
    # stats
    name: str = ''
    xp: int = 0
    hp: int = 100
    attack: int = 5
    luck: int = 3
    gold: int = 200

    inventory = []

    # name : [description, power, ability, value]
    possible_player_inventory = {
        'green stone' : ['This stone can be combined with other stones to become more powerful', 1, 'none', 60],
        'red stone' : ['This stone can be combined with other stones to become more powerful', 1, 'none', 70],
        }

class Enemy:

    # name : [type, attack, hp, ability]
    enemies = {
        'witch' : ['unique', 10, 50, None]
    }


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

            5> yes
            2> no, return to Gooberton         
            ''')))
    return page
        

page = intro_machine()
while running:
    page = adventuring(page)