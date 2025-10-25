#Quick game practice
import random

charas = {
          "Knight":{ "Basic_attack" : 10 , "Skill" : 15 ,"heal" : 30 , "ultimate" : 30, "HP" : 100},
          "Mage":{ "Basic_attack" : 5 , "Skill" : 25 ,"heal" : 20 , "ultimate" : 35, "HP" : 70},
          "Javelin":{ "Basic_attack" : 15 , "Skill" : 10 ,"heal" : 20 , "ultimate" : 20, "HP" : 80}}

enemies = {
  "Local criminal":{"Basehp": 100,"HP": 100, "Basic Attack" : 5,"Skill" :10,"Ultimate":15},
  "Hobgoblin":{"Basehp":200,"HP" : 200, "Basic Attack" : 10,"Skill" :15,"Ultimate":30},
  "Demon":{"Basehp":500,"HP" : 500, "Basic Attack" : 10,"Skill" :25,"Ultimate":50}}

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
    print(f"\nCurrent Character: {character}\n\nSTAGE SELECT:\n\nLocal_Criminal - Easy\nHobgoblin - Medium\nDemon - Hard\n")
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
    
def battle(character, selection, action, dmg):  
    print("\n\nBattle Start")
    while True:
      print(f"Enemy {selection}\n\n{selection} Current HP: {enemies.get(selection).get('HP')}\nYour Current HP: {charas.get(character).get('HP')}")
      turn = input(f"\nWhat would you like to do?:\n\n(1)Basic Attack - {charas.get(character).get('Basic_attack')}DMG\t(2)Skill - {charas.get(character).get('Skill')}DMG\n(3)Heal Self - {charas.get(character).get('heal')}HP\t(4)Ultimate {charas.get(character).get('ultimate')}DMG\nEnter here:\t")
      if turn == "1":
        enemies[selection]["HP"] -= charas[character]["Basic_attack"]
        print(f"\n\nDealt Ultimate (-{charas[character]['ultimate']}) to {selection}\n\n{selection} used {action}! Dealt {enemies[selection][action]} to {character} HP:{charas[character]['HP']}\n\n")
        charas[character]["HP"] -= dmg
      elif turn == "2":
        enemies[selection]["HP"] -= charas[character]["Skill"]
        print(f"\n\nDealt Ultimate (-{charas[character]['ultimate']}) to {selection}\n\n{selection} used {action}! Dealt {enemies[selection][action]} to {character} HP:{charas[character]['HP']}\n\n")
        charas[character]["HP"] -= dmg
      elif turn == "3":
        charas[character]["HP"] += charas[character]["heal"]
        if charas[character]["HP"] > 100:
          charas[character]["HP"] = 100
          print(f"\n\nHeals self by {charas[character]['heal']}\n\n{selection} used {action}! Dealt {enemies[selection][action]}\n\n")
          charas[character]["HP"] -= dmg
      elif turn == "4":
        enemies[selection]["HP"] -= charas[character]["ultimate"]
        print(f"\n\nDealt Ultimate (-{charas[character]['ultimate']}) to {selection}\n\n{selection} used {action}! Dealt {enemies[selection][action]} to {character} HP:{charas[character]['HP']}\n\n")
        charas[character]["HP"] -= dmg
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

def enemy_behaviour(selection):
  if enemies[selection]["HP"] <= enemies[selection]["Basehp"]//3:
    action = "Ultimate"
    dmg = enemies[selection]["Ultimate"]
    return action, dmg
  else: 
    if random.randint (1,2) < 2:
      action = "Basic Attack"
      dmg = enemies[selection]['Basic Attack']
      return action, dmg
    else:
      action = "Skill"
      dmg = enemies[selection]['Skill']
      return action, dmg
character = character_select()
selection = boss_select(character)
action, dmg = enemy_behaviour(selection)
battle(character, selection, action, dmg) 
