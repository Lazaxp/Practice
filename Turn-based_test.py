#Quick game practice
import random
charas = ["Knight","Mage","Javelin"]
enemies = ["Local Criminal","Hobgoblin","Demon"]
def local_criminal():
  hp1= 40
  return hp1
def knight():
  hp = 100
  basic_attack = 5
  skill1 = 10
  heal = 20
  ultimate = 30
  crit = 100
  return hp, basic_attack, skill1, heal, ultimate, crit
a = input("Welcome To My Test Turn-Based Game.\nPress Enter to Start.")
clear_screen()
def character_select():
  character = eval(input("Select your character(Type the number of your choice):\n(1) Knight - Big Base Attack\n(2) Mage - Big Base Magic and Crit\n(3) Javelin - Big Crit Rate\n\nEnter Here:\t"))
  character -= 1
  while True:
    confirm = input(f"You've Selected {charas[character]}. Is this the Character you want? (Yes/No):\t").lower()
    if confirm == "yes":
       print(f"{charas[character]} Confirmed.")
       return character      
       break
    elif confirm == "no":
       return character_select()
    else:
       print("Please Choose within the option.")
def boss_select(character):
  selection = eval(input(f"Current Character: {charas[character]}.\nSTAGE SELECT(Type the number of your choice)\n(1) - {enemies[0]}\n(2) - {enemies[1]}\n(3) - {enemies[2]}\nEnter Here:\t"))
  selection -= 1  
  while True:
    confirm = input(f"You've selected to battle with {enemies[selection]}. Are you sure? (Yes or No):\t")
    if confirm == "yes":
      print("Confirmed.")
      return selection
      break
    elif confirm == "no":
      return boss_select()
  else:
    print("Please choose within the options.")
def battle(character, selection):  
  if charas[character] == "Knight" and enemies[selection] == "Local Criminal":
    hp1 = local_criminal()
    hp, basic_attack, skill1, heal, ultimate, crit = knight()
    print("Battle Start")
    while True:
      print(f"Enemy {enemies[selection]}\n\nCurrent HP:{hp1}")
      turn = input(f"What would you like to do?:\n(1)Basic Attack - {basic_attack}DMG\t(2)Skill - {skill1}DMG\n(3)Heal Self - {heal}HP\t(4)Ultimate {ultimate}DMG\nEnter here:\t")
      if turn == "1":
        hp1 -= basic_attack
        print(f"Dealt {basic_attack} to {enemies[selection]}")
      elif turn == "2":
        hp1 -= skill1
        print(f"Dealt {skill1} to {enemies[selection]}")
      elif turn == "3":
        hp += heal
        print(f"Heals self by {heal}")
      elif turn == "4":
        hp1 -= ultimate
        print(f"Dealt {ultimate} to {enemies[selection]}")
      else:
        print("Choose a Valid Option.")
      if hp1 <= 0:
        print("Enemy Defeated")
        break
character = character_select()
selection = boss_select(character)
battle(character, selection)
