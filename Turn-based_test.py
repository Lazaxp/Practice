#Quick game practice
import random

charas = {"Knight":{ "Basic_attack" : 10 , "Skill" : 15 ,"heal" : 30 , "ultimate" : 30, "HP" : 100},
          "Mage":{ "Basic_attack" : 5 , "Skill" : 25 ,"heal" : 20 , "ultimate" : 35, "HP" : 70},
          "Javelin":{ "Basic_attack" : 15 , "Skill" : 10 ,"heal" : 20 , "ultimate" : 20, "HP" : 80}}

enemies = {
  "Local criminal":{"HP": 100},
  "Hobgoblin":{"HP" : 200},
  "Demon":{"HP" : 500}}

a = input("Welcome To My Test Turn-Based Game.\nPress Enter to Start.")

def character_select():
  while True:
    character = input("Select your character:\nKnight - Big Base Attack\nMage - Big Base Magic and Crit\nJavelin - Big Crit Rate\n\nEnter Here:\t").capitalize()
    if character in charas:
        confirm = input(f"You've Selected {character}. Is this the Character you want? (Yes/No):\t").lower()
        if confirm == "yes":
           print(f"{character} Confirmed.")
           return character      
           break
        elif confirm == "no":
           return character_select() 
        else:
         print("Please Choose within the option.")
    else:
      print("\n\nInvalid Option.\n\n")
      continue
      
def boss_select(character):
  while True:
    print(f"Current Character: {character}\nSTAGE SELECT:\nLocal Criminal - Easy\nHobgoblin - Medium\nDemon - Hard\n")
    selection = input("Enter Here:\t").capitalize()
    if selection in enemies:
      confirm = input(f"You've selected to battle with {selection}. Are you sure? (Yes or No):\t")
      if confirm == "yes":
        print("Confirmed.")
        return selection
        break
      elif confirm == "no":
        return boss_select()
      else:
        print("Please choose within the options.")
    else:
      print("\n\nInvalid Option.\n\n")
    
def battle(character, selection):  
    print("\n\nBattle Start")
    while True:
      print(f"Enemy {selection}\n\n{selection} Current HP: {enemies.get(selection).get('HP')}\nYour Current HP: {charas.get(character).get('HP')}")
      turn = input(f"What would you like to do?:\n(1)Basic Attack - {charas.get(character).get('Basic_attack')}DMG\t(2)Skill - {charas.get(character).get('Skill')}DMG\n(3)Heal Self - {charas.get(character).get('heal')}HP\t(4)Ultimate {charas.get(character).get('ultimate')}DMG\nEnter here:\t")
      if turn == "1":
        enemies[selection]["HP"] -= charas[character]["Basic_attack"]
        print(f"Dealt Basic Attack(-{charas[character]['Basic_attack']}) to {selection}")
      elif turn == "2":
        enemies[selection]["HP"] -= charas[character]["Skill"]
        print(f"Dealt skill(-{charas[character]['Skill']}) to {selection}")
      elif turn == "3":
        enemies[selection]["HP"] += charas[character]["heal"]
        print(f"Heals self by {charas[character]['heal']}")
      elif turn == "4":
        enemies[selection]["HP"] -= charas[character]["ultimate"]
        print(f"Dealt Ultimate (-{charas[character]['ultimate']}) to {selection}")
      else: 
        print("Choose a Valid Option.")
      if enemies[selection]["HP"] <= 0:
        print("Enemy Defeated")
        break
      elif charas[character]["HP"] <= 0:
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
