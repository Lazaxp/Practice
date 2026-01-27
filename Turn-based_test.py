#Quick game practice
import random, os, time
def cls(n):
  time.sleep(0.5+n)
  os.system("cls")
ability_points = {"ba" : "Inf", "skill" : 30, "heal" : 20, "ulti" : 15}
charas = {
          "Knight":{ "Basic_attack" : 10 , "Skill" : 15 ,"heal" : 30 , "ultimate" : 30, "HP" : 100, "crit" : 40, "critdmg" : 2},
          "Mage":{ "Basic_attack" : 5 , "Skill" : 25 ,"heal" : 20 , "ultimate" : 35, "HP" : 70, "crit" : 60, "critdmg" : 1.8},
          "Javelin":{ "Basic_attack" : 15 , "Skill" : 10 ,"heal" : 20 , "ultimate" : 20, "HP" : 80, "crit" : 80, "critdmg" : 1.2}}
enemies = {
  "Local criminal":{"Basehp": 100,"HP": 100, "Basic Attack" : 5,"Skill" :10,"Ultimate":15},
  "Hobgoblin":{"Basehp":200,"HP" : 200, "Basic Attack" : 10,"Skill" :15,"Ultimate":30},
  "Demon":{"Basehp":500,"HP" : 500, "Basic Attack" : 10,"Skill" :25,"Ultimate":50}}

a = input("Welcome To My Test Turn-Based Game.\nPress Enter to Start.")

def character_select():
  while True:
    os.system("cls")
    character = input("Select your character:\nKnight - Big Base Attack\nMage - Big Base Magic and Crit\nJavelin - Big Crit Rate\n\nEnter Here:\t").capitalize()
    if character in charas:
        confirm = input(f"You've Selected {character}. Is this the Character you want? (Yes/No):\t").lower()
        if confirm == "yes":
           print(f"{character} Confirmed.")
           return character      
           break
        elif confirm == "no":
           os.system("cls")
           return character_select() 
        else:
           os.system("cls")
           print("Please Choose within the option.")
          
    else:
      print("\n\nInvalid Option.\n\n")
      continue
      
def boss_select(character):
  while True:
    os.system("cls")
    print(f"\nCurrent Character: {character}\n\nSTAGE SELECT:\n\nLocal_Criminal - Easy\nHobgoblin - Medium\nDemon - Hard\n")
    selection = input("Enter Here:\t").capitalize()
    if selection in enemies:
      confirm = input(f"You've selected to battle with {selection}. Are you sure? (Yes or No):\t")
      if confirm == "yes":
        os.system("cls")
        print("Confirmed.")
        return selection
      elif confirm == "no":
        os.system("cls")
        return boss_select()
      else:
        os.system("cls")
        print("Please choose within the options.")
        
    else:
      os.system("cls")
      print("\n\nInvalid Option.\n\n")
    
def battle(character, selection, action, dmg, crithit):  
  print("Battle Start")
  time.sleep(0.5)
  while True:
    cls(1.1)
    print(f"Enemy {selection}\n\n{selection} Current HP: {enemies.get(selection).get('HP')}\nYour Current HP: {charas.get(character).get('HP')}")
    turn = input(f"\nWhat would you like to do?:\n\n(1)Basic Attack - {charas.get(character).get('Basic_attack')}DMG - AP: {ability_points['ba']}\t(2)Skill - {charas.get(character).get('Skill')}DMG - AP: {ability_points['skill']}\n(3)Heal Self - {charas.get(character).get('heal')}HP - AP: {ability_points['heal']}'\t(4)Ultimate {charas.get(character).get('ultimate')}DMG - AP: {ability_points['ulti']}\nEnter here:\t")
    if turn == "1": 
      cls(0)      
      enemies[selection]["HP"] -= charas[character]["Basic_attack"]
      if crithit == True:        
        enemies[selection]["HP"] -= charas[character]["crit"]
        print(f"\n\nCritical Hit! Dealt Basic Attack (-{charas[character]['Skill']+charas[character]['crit']}) to {selection}\n")
        time.sleep(0.5)
        print("\n{selection} used {action}! Dealt {enemies[selection][action]} to {character} HP:{charas[character]['HP']}\n\n")
      else:
        print(f"\n\nDealt Basic Attack (-{charas[character]['Skill']}) to {selection}\n")
        time.sleep(0.5)
        print(f"\n{selection} used {action}! Dealt {enemies[selection][action]} to {character} HP:{charas[character]['HP']}\n\n")
      charas[character]["HP"] -= dmg
    elif turn == "2":
      cls(0)
      enemies[selection]["HP"] -= charas[character]["Skill"]
      if ability_points["skill"] == 0:
        print("Can't do that!")
        cls(1)
      elif crithit == True:
        enemies[selection]["HP"] -= charas[character]["crit"]
        print(f"\n\nCritical Hit! Dealt Skill (-{charas[character]['Skill']+charas[character]['crit']}) to {selection}\n")
        time.sleep(0.5)
        print(f"\n{selection} used {action}! Dealt {enemies[selection][action]} to {character} HP:{charas[character]['HP']}\n\n")
      else:
        print(f"\n\nDealt Skill (-{charas[character]['Basic_attack']}) to {selection}\n")
        time.sleep(0.5)
        print(f"\n{selection} used {action}! Dealt {enemies[selection][action]} to {character} HP:{charas[character]['HP']}\n\n")
      charas[character]["HP"] -= dmg
      ability_points["skill"] -= 1
    elif turn == "3":
      cls(0)
      charas[character]["HP"] += charas[character]["heal"]
      if ability_points("skill") == 0:
        print("Can't do that!")
        cls(1)
        if charas[character]["HP"] > 100:
          charas[character]["HP"] = 100
        print(f"\n\nHeals self by {charas[character]['heal']}\n")
        time.sleep(0.5)
        print(f"\n{selection} used {action}! Dealt {enemies[selection][action]}\n\n")
      charas[character]["HP"] -= dmg
      ability_points["heal"] -= 1
    elif turn == "4":
      cls(0)
      enemies[selection]["HP"] -= charas[character]["ultimate"]
      if ability_points["ulti"] == 0:
        print("Can't do that!")
        cls(1)
      elif crithit == True:
        enemies[selection]["HP"] -= charas[character]["crit"]
        print(f"\n\nCritical Hit! Dealt Ultimate(-{charas[character]['ultimate']+charas[character]['crit']}) to {selection}\n")
        time.sleep(0.5)
        print(f"\n{selection} used {action}! Dealt {enemies[selection][action]} to {character} HP:{charas[character]['HP']}\n\n")
      else:
        print(f"\n\nDealt Ultimate(-{charas[character]['ultimate']}) to {selection}\n")
        time.sleep(0.5)
        print(f"\n{selection} used {action}! Dealt {enemies[selection][action]} to {character} HP:{charas[character]['HP']}\n\n")
        charas[character]["HP"] -= dmg   
        ability_points["ulti"] -= 1   
    else: 
        print("Choose a Valid Option.")

    if enemies[selection]["HP"] <= 0:
      cls(0)
      print("Enemy Defeated")
      break
    elif charas[character]["HP"] <= 0:
      cls(0)
      print("You have been defeated")
      r = input("Try again?:\t").lower()
      if r == "yes":
        return battle()
      elif r == "no":
        break
      else:
        print("Choose within the options")
      cls(0)
def enemy_behaviour(selection):
  if random.randint(1,25) == 1:
    action = "Ultimate"
    dmg = enemies[selection]["Ultimate"]
    return action, dmg
  else: 
    if random.randint (1,3) != 2:
      action = "Basic Attack"
      dmg = enemies[selection]['Basic Attack']
      return action, dmg
    else:
      action = "Skill"
      dmg = enemies[selection]['Skill']
      return action, dmg    
def critical(character):
  x = random.randint(charas[character]["crit"]-20, charas[character]["crit"])
  chance = 0+x      
  if chance == 100:
    chance = 0
    crithit = True
    return crithit
  else:
    crithit = False
    return crithit
character = character_select()
selection = boss_select(character)
action, dmg = enemy_behaviour(selection)
crithit = critical(character)
count = battle(character, selection, action, dmg, crithit) 


