import random
digResults = ["weapon","snake", "scorpion", 3, 5, 1, "money", "money", "snake", "medkit"]
expResults = ["trader","shoes","money",12, "wolf", "wolf", "wolf", "medstim","wolf", "wolf", "wolf", "weapon", "tnt", "wolf", "wolf", "alpha wolf"]
scavResults = ["money", "lava", "money","","","","","","","","","","", "turboShovel", "mugger", "mugger", "medstim", "dead animal", "landmine", "weapon", "weapon", "weapon", "weapon", "weapon"]
impDigResults = ["weapon", "scorpion", 3, 5, 1, "money", "money", "medstim"]
inescapable = ["snake", "wolf", "alpha wolf"]
health = 10
food = 0
stimHealth = health
money = 0
hasTurbo = False
hasWeapon = False
hasShoes = False
hasVial = False
hasBoom = False
hasKey = False
hasMap = False
hasStim = False
hasVial = False
hasPass = False
async def input_async(prompt=""):
    return await browser_input(prompt)
async def restart():
      global masMap
      global hasKey
      global hasBoom
      global hasShoes
      global hasWeapon
      global money
      global food
      global health
      global hasTurbo
      print("Restarting...")
      health = 10
      food = 0
      money = 0
      hasWeapon = False
      hasShoes = False
      hasBoom = False
      hasKey = False
      hasTurbo = False
      hasMap = False
      print("Welcome to ...")
      print("DIG IT o yea")
      print("Try to escape the forest!")
      ask()
      return
    def scavenge():
      global health
      global money
      global hasWeapon
      global food
      global hasShoes
      global hasStim
      global hasVial
      global hasPass
      global hasTurbo
      #canada
      #in loving memory of all the people in 9/11
      res = scavResults[random.randint(0,len(digResults)-1)]
      if str(res) != res:
        print("You found some food.")
        food += res
        ask()
        return
      else:
        if res == "":
          print("You found nothing, and you are injured from scavenging. -2 health.")
          health -= 2
          ask()
          return
        if res == "money":
          if random.randint(0,10) == 0:
            print("You found 50 dollars in scrap. You also found a strange vial. You drink it, because you're stupid, and you feel very cold.")
            hasVial = True
          else:
            print("You found 50 dollars in scrap.")
          money += 50
          ask()
          return
        if res == "lava":
          yn = await input_async("You come across a lava lake. Would you like to swim in it? y/n")
          n = yn == "n" or yn == "y"
          a = hasVial and yn == "y"
          b = yn == "n"
          c = not hasVial and yn == "y"
          if a:
            print("You take a swim in the lava lake, somehow unburnt. You find an engraving that says a series of numbers.")
            hasPass = True
          if b:
            print("You decide to avoid the risk.")
          if c:
            print("You jump into the lava, and are scorced! You barely escape with your life.")
            health = 1
          ask()
          return
        if res == "medstim":
          print("You found a medkit and stimpack combo. You are at full health and are energized!")
          if health < 10:
            health = 10
          hasStim = True
          ask()
          return
        if res=="weapon":
          print("You found a weapon.")
          hasWeapon = True
          ask()
          return
        if res=="turboShovel":
          print("You found a better shovel.")
          hasTurbo = True
          ask()
          return
        if res == "dead animal":
          ans = print("You found a dead animal. Wound you like to eat it? y/n")
          if ans == "y":
            if random.randint(0,1) == 1:
              print("It was rotten.")
              health -= 5
            else:
              print("It was delicious!")
              health += 10
          elif not ans == "n":
            print("Um, no I guess?.")
          ask()
          return
        if res == "landmine":
          print("You stepped on a landmine!")
          health -= 10
          ask()
          return
        print("You encountered a "+res+".")
        if res == "mugger":
          inp = await input_async("Would you like to fight, pay him or run?")
          if inp.lower() == "pay":
            money = 0
            print("You paid him off. He left you alone after that.")
            ask()
            return
        else:
          inp = await input_async("Would you like to fight or run?")
        if inp=="fight":
          if hasWeapon:
            print("You defeat the creature, but your weapon breaks. You found $20.")
            money += 20
            hasWeapon = False
            ask()
            return
          else:
            print("u got COOKED")
            health -= 3
            ask()
            return
        if inp == "run":
          for i in range(len(inescapable)):
            if res == inescapable[i] and not hasShoes:
              print("ur 2 slow lol")
              health -= 4
              ask()
              return
          print("You escaped!")
          ask()
          return
        print("You just typed nonsense to annoy the program, didn't you? Well, GET TROLLED -5 health")
        health -= 5
        ask()
        return
      
async def dig():
  global health
  global money
  global hasWeapon
  global food
  global hasShoes
  if hasTurbo:
    res = impDigResults[random.randint(0,len(impDigResults)-1)]
  else:
    res = digResults[random.randint(0,len(digResults)-1)]
  if str(res) != res:
    print("You found some food.")
    found = False
    food += res
    ask()
    return
  else:
    if res == "medstim":
      print("You found a medkit and stimpack combo. You are at full health and are energized!")
      if health < 10:
        health = 10
      hasStim = True
      ask()
      return
    if res == "":
      print("You found nothing, and you are tired from digging. -1 health.")
      health -= 1
      ask()
      return
    if res == "money":
      print("You found ten dollars.")
      money += 10
      ask()
      return
    if res == "medkit":
      print("You found a medkit. You are at full health!")
      if health < 10:
        health = 10
      ask()
      return
    if res=="weapon":
      print("You found a weapon.")
      hasWeapon = True
      ask()
      return
    print("You encountered a "+res+".")
    inp = await input_async("Would you like to fight or run?")
    if inp=="fight":
      if hasWeapon:
        print("You defeat the creature, but your weapon breaks. You found $20.")
        money += 20
        hasWeapon = False
        ask()
        return
      else:
        print("u got COOKED")
        health -= 3
        ask()
        return
    if inp == "run":
      for i in range(len(inescapable)):
        if res == inescapable[i] and not hasShoes:
          print("ur 2 slow lol")
          health -= 4
          ask()
          return
      print("You escaped!")
      ask()
      return
    print("You just typed nonsense to annoy the program, didn't you? Well, GET TROLLED -5 health")
    health -= 5
    ask()
    return
          
async def eat():
  global health
  global food
  if food == 0:
    print("You don't have any food.")
  else:
    print("You ate some food. You healed " + str(food))
  health += food
  food = 0
  ask()
async def explore():
  global health
  global money
  global food
  global hasWeapon
  global hasShoes
  global hasBoom
  global hasMap
  global hasKey
  res = expResults[random.randint(0,len(expResults)-1)]
  if str(res) != res:
    found = False
    food += res
    ask()
    return
  else:
    if res == "medstim":
      print("You found a medkit and stimpack combo. You are at full health and are energized!")
      if health < 10:
        health = 10
      hasStim = True
      ask()
      return
    if res == "money":
      print("You found thirty dollars.")
      money += 30
      ask()
      return
    if res == "trader":
      print("You found a trader. You can buy food from him.")
      yn = await input_async("10:1 ratio, y/n?")
      if yn == "y":
        while True:
          if money < 10:
            break
          money -= 10
          food += 3
      elif yn !="n":
        print("...what?")
      ask()
      return
    if res=="weapon":
      print("You found a weapon.")
      hasWeapon = True
      ask()
      return
    if res=="shoes":
      print("You found some shoes.")
      hasShoes = True
      ask()
      return
    if res=="tnt":
      print("You found some TNT.")
      hasBoom = True
      if random.randint(1,5) == 1:
        print("You found a map wrapped around it.")
        hasMap = True
      ask()
      return
    print("You encountered a "+res+".")
    inp = await input_async("Would you like to fight or run?")
    if inp=="fight":
      if res == "alpha wolf":
          if hasBoom:
            print("You destroy the Alpha Wolf in a spectacular explosion! You found $50 and a key.")
            money += 50
            hasBoom = False
            hasKey = True
            ask()
            return
          else:
            print("u got COOKED")
            health -= 5
            ask()
            return
      else:
          if hasWeapon:
            print("You defeat the creature, but your weapon breaks. You found $30.")
            money += 30
            hasWeapon = False
            ask()
            return
          else:
            print("u got COOKED")
            health -= 5
            ask()
            return
    if inp == "run":
      for i in range(len(inescapable)):
        if res == inescapable[i] and not hasShoes:
          hasShoes = False
          print("ur 2 slow lol")
          health -= 6
          ask()
          return
      if hasShoes:
        print("Your shoes wore out.")
        hasShoes = False
      print("You escaped!")
      ask()
      return
    print("You just typed nonsense to annoy the program, didn't you? Well, GET TROLLED -5 health")
    health -= 5
    ask()
    return
async def escape():
  a = food >= 40
  b = health >= 20
  c = hasMap
  d = hasKey
  e = money >= 60
  if not c:
    print("You wander endlessly before giving up.")
    ask()
    return
  if not b:
    print("You don't feel confident going in your current state.")
    ask()
    return
  if not d:
    print("You eventually come to a gate, but it needs a key.")
    ask()
    return
  if not hasPass:
    print("It also needs a code.")
    ask()
    return
  if not a:
    print("You feel like food will be vital, and you don't have much right now...")
    ask()
    return
  if not e:
    print("You would feel better with some money...")
    ask()
    return
  print("You escaped!")
async def ask():
  global money
  global health
  global hasStim
  global food
  global hasKey
  global hasMap
  global stimHealth
  if health <= 0:
    await input_async("You died! Restarting...")
    restart()
    return
  print("Health: "+str(health)+ ", Money: " +str(money)+", Food: " + str(food))
  if health < stimHealth and hasStim:
    health = stimHealth
    hasStim = False
    print("You dodged the health decrease.")
  stimHealth = health
  inp = await input_async("Would you like to dig, explore, scavenge, escape, or eat?")
  if inp == "dig":
    dig()
    return
  if inp == "scavenge":
    scavenge()
    return
  if inp == "escape":
    escape()
    return
  if inp == "explore":
    explore()
    return
  if inp == "eat":
    eat()
    return
  print("Sorry, I don't understand. Could you have typed a capital by accident?")
  ask()
  return
async def main():
    print("Welcome to ...")
    print("DIG IT o yea")
    print("Try to escape the forest!")
    ask()    
