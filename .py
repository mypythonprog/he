money = 0
coins = {
    "quaters": 0.25,
    "dimes": 0.10,
    "nickles": 0.05,
    "pennies": 0.01,
}
# i made this coffee machine by  new skills
#

def cal(u1,insert):
    global  money
    es = MENU['espresso']['cost']
    la = MENU['latte']['cost']
    ca = MENU['cappuccino']['cost']
    if u1 == 'espresso':
        co = sum(insert)

        if co > es:

            hello = co - es
            print(f"Your change {hello}.")
            print("Enjoy your coffee!")
            money += hello
        elif co == es:
            print("Enjoy your coffee")
            money += co
        else:
            print("insert more coins")


    elif u1 == 'latte':
        co = sum(insert)
        if co > la:

          hello = co - la
          print(f"Your change {hello}.")
          print("Enjoy your coffee!")
        elif co == la:
          print("Enjoy your coffee")
        else:
            print("insert more coins")

    else:
        co = sum(insert)
        if co > ca:
            hello = co - ca
            print(f"Your change {hello}.")
            print("Enjoy your coffee!")
        elif co == ca:
            print("Enjoy your coffee")

        else:
            print("MOre coins needed.")




def suff(u):
  coins_choice = int(input("HOW many quaters ?\n"))
  coins_choice2= int(input("HOw many dimes?\n"))
  choice_choice3 = int(input("How many nickles?\n"))
  coins_choice4 = int(input("How many pennies?\n"))
  value = [coins_choice,coins_choice2,choice_choice3,coins_choice4]
  cal(u1=u,insert=value)

def is_sufficent_resources(order):

    for item in order and resources:
        if order[item] > resources[item]:
            print(f'There is no enough {item}')
            return False

    return True


def game():
    running = True
    global money


    while running :
     user = input("what do you like ? (espresso/Latte/cappunccino)\n").lower()
     if user == 'off':
       running = False
       return
     elif user == 'report':
         print(f"Water: {resources['water']}\nMilk: {resources['milk']}\nCoffee:{resources['coffee']}\nMoney:{money}")
         user = input("what do you like ? (espresso/Latte/cappunccino)\n").lower()
     elif user == 'off':
         running = False
     choice = user
     re = MENU[choice]['ingredients']


     if  is_sufficent_resources(order = re ) == False:
         suff(u=user)
         if user == 'espresso':
             resources['water'] -= MENU['espresso']['ingredients']['water']
             resources['coffee'] -= MENU['espresso']['ingredients']['coffee']


         elif user == 'latte':
             resources['water'] -= MENU['latte']['ingredients']['water']
             resources['milk'] -= MENU['latte']['ingredients']['milk']
             resources['coffee'] -= MENU['latte']['ingredients']['coffee']

         else:
             resources['water'] -= MENU['cappuccino']['ingredients']['water']
             resources['milk'] -= MENU['cappuccino']['ingredients']['milk']
             resources['coffee'] -= MENU['cappuccino']['ingredients']['coffee']
     else:
        game()







game()

