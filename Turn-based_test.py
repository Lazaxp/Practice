#Quick game practice
import random
charas = [["Knight", 5 , 10 , 30 , 30, 100],["Mage", 5 , 25 , 20 , 30, 80],["Javelin", 5 , 15 , 25 , 20, 80]]
enemies = [["Local Criminal", 100],["Hobgoblin" , 200],["Demon" , 500]]
a = input("Welcome To My Test Turn-Based Game.\nPress Enter to Start.")
def character_select():
  character = eval(input("Select your character(Type the number of your choice):\n(1) Knight - Big Base Attack\n(2) Mage - Big Base Magic and Crit\n(3) Javelin - Big Crit Rate\n\nEnter Here:\t"))
  character -= 1
  while True:
    confirm = input(f"You've Selected {charas[character][0]}. Is this the Character you want? (Yes/No):\t").lower()
    if confirm == "yes":
       print(f"{charas[character][0]} Confirmed.")
       return character      
       break
    elif confirm == "no":
       return character_select(character)
    else:
       print("Please Choose within the option.")
def boss_select(character):
  selection = eval(input(f"Current Character: {charas[character][0]}.\nSTAGE SELECT(Type the number of your choice)\n(1) - {enemies[0][0]}\n(2) - {enemies[1][0]}\n(3) - {enemies[2][0]}\nEnter Here:\t"))
  selection -= 1  
  while True:
    confirm = input(f"You've selected to battle with {enemies[selection][0]}. Are you sure? (Yes or No):\t")
    if confirm == "yes":
      print("Confirmed.")
      return selection
      break
    elif confirm == "no":
      return boss_select()
  else:
    print("Please choose within the options.")
def battle(character, selection):  
    print("Battle Start")
    while True:
      print(f"Enemy {enemies[selection][0]}\n\n{enemies[selection][0]} Current HP:{enemies[selection][1]}\nYour Current HP: {charas[character][5]}")
      turn = input(f"What would you like to do?:\n(1)Basic Attack - {charas[character][1]}DMG\t(2)Skill - {charas[character][2]}DMG\n(3)Heal Self - {charas[character][3]}HP\t(4)Ultimate {charas[character][4]}DMG\nEnter here:\t")
      if turn == "1":
        enemies[selection][1] -= charas[character][1]
        print(f"Dealt Basic Attack(-{charas[character][1]}) to {enemies[selection][0]}")
      elif turn == "2":
        enemies[selection][1] -= charas[character][2]
        print(f"Dealt skill(-{charas[character][2]}) to {enemies[selection][0]}")
      elif turn == "3":
        enemies[selection][1] += charas[character][3]
        print(f"Heals self by {charas[character][3]}")
      elif turn == "4":
        enemies[selection][1] -= charas[character][4]
        print(f"Dealt Ultimate (-{charas[character][4]}) to {enemies[selection][0]}")
      else: 
        print("Choose a Valid Option.")
      if enemies[selection][1] <= 0:
        print("Enemy Defeated")
        break
      elif charas[character][5] <= 0:
        print("You have been defeated")
        r = input("Try again?:\t").lower()
        if r == yes:
          return battle()
        elif r == no:
          break
        else:
          print("Choose within the options")
character = character_select()
selection = boss_select(character)
battle(character, selection)
