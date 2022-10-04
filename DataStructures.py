import requests
import json 

# Pokemon info (JSON): https://github.com/fanzeyi/pokemon.json/blob/master/pokedex.json

# x = 5
# with open("json.txt", "w+") as outfile:
  # json.dump(x, outfile)

with open('pokemon.json', 'r') as outfile:
  data = json.load(outfile)

class baseStats:
  def __init__(self, base):
    self.base = base
    self.hp = base["HP"]
    self.attack = base["Attack"]
    self.defense = base["Defense"]
    self.spAttack = base["Sp. Attack"]
    self.spDefense = base["Sp. Defense"]
    self.speed = base["Speed"]

  def setStat(self, statType, statChange):
    self.base[statType] = statChange
    print("HP: " + str(self.base[statType]))

  def setAllStats(self, base):
    self.base = base
    print("self.base[HP]: " + str(self.base["HP"]))
    
class Pokedex:
  def __init__(self, id, language):
    self.data = data
    self.id = id - 1
    self.language = language
    self.base = self.data[self.id]["base"]
    self.stats = baseStats(self.base)

  def getPokemon(self):
    pokemon = self.data[self.id]["name"][self.language]
    return pokemon

  def getStat(self, statType):
    print(self.base["HP"])
    print(self.base)
    return self.base[statType]
    
  def getAllStats(self):
    return self.stats.base

  def setStat(self, statType, statChange):
    self.stats.setStat(statType, statChange)

  def setAllStats(self, base):
    self.stats.setAllStats(base)
    
  def definePokemon(id, data):
    pass

  def updatePokemon(id, data):
    pass

id = int(input("Id: "))
language = input("Language: ")

pokemon = Pokedex(id, language)
print(pokemon.getPokemon())
print(pokemon.getAllStats())
print(pokemon.getStat("HP"))
pokemon.setStat("HP", 50)
pokemon.setAllStats({'HP': 60, 'Attack': 62, 'Defense': 63, 'Sp. Attack': 80, 'Sp. Defense': 80, 'Speed': 60})
print(pokemon.getAllStats())
print(pokemon.getStat("HP"))

      
  
  


