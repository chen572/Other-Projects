class Pokemon:
  
    def __init__(self, name, level, xp, type , max_health, health, is_knocked_out, version_2, version_3, version_1):
        self.name = name
        self.level = level
        self.type = type
        self.max_health = max_health                                                        #MAX HEALTH IS DETERMINED BY LEVEL
        self.health = health
        self.is_knocked_out = is_knocked_out
        self.xp = xp
        self.version_2 = version_2
        self.version_3 = version_3
        self.version_1 = version_1
    
    def __repr__(self):
        return self.name
  
    def lose_health(self, dmg):
        new_health = self.health - dmg
        self.health = new_health
     
        if self.health <= 0:
            self.knocked_out()
          
            print(self.name + " was hit for " + str(dmg) + "hp and now has 0 health " + self.name + " have been knocked out!")
      
        else:
            
            print(self.name + " was hit for " + str(dmg) + "hp and now has " + str(self.health) + "hp")
            
            return self.health 
  
    def regaining_health(self, added_health):
        if self.health >= self.max_health:
            return print(self.name + " is at his maximum health he cannot regain anymore health points")
      
        elif self.health <= 0:
            self.health = 0
            new_health = self.health + added_health
            self.health = new_health
            self.knocked_out()
        
            return print(self.name + " Has been revived with " + str(self.health) + "hp")
      
      
        new_health = self.health + added_health
        self.health = new_health
        if new_health > self.max_health:
            self.health = self.max_health
          
            return self.health, print(self.name + " has regained " + str(added_health) + "hp and now is at full health with " + str(self.health) + "hp")
        else:
            return self.health, print(self.name + " has regained " + str(added_health) + "hp and now has " + str(self.health) + "hp")
  
    def knocked_out(self):
        if self.health <= 0:
            self.is_knocked_out = True
            return self.is_knocked_out
        elif self.health > 0:
            self.is_knocked_out = False
            return self.is_knocked_out

    def attack(self, other):                                                      #FIRE > GRASS    GRASS > WATER   WATER > FIRE    ROCK > FIRE
        
        def super_effective(self):
            dmg = (self.level + 5) * 2
            other.lose_health(dmg)
            if other.health <= 0:
                print(self.name + " attack was super effective!")
                self.xp_gain()
                return
            else:
                return print(self.name + " attack was super effective!")
        
        def not_very_effective(self):
            dmg = (self.level + 5) / 2
            other.lose_health(int(dmg))
            if other.health <= 0:
                print(self.name + " attack was not very effective")
                self.xp_gain()
                return
            else:
                return print(self.name + " attack was not very effective")
        
        def normal(self):
            dmg = self.level + 5
            other.lose_health(dmg)
            if other.health <= 0:
                self.xp_gain()
                return
            else:
                return
        
        if self.is_knocked_out == False and other.health > 0:
            if self.type == 'fire' and other.type == 'grass':
                return super_effective(self)
            elif self.type == 'grass' and other.type == 'water':
                return super_effective(self)
            elif self.type == 'water' and other.type == 'fire':
                return super_effective(self)
            elif self.type == 'grass' and other.type == 'fire':
                return not_very_effective(self)
            elif self.type == 'water' and other.type == 'grass':
                return not_very_effective(self)
            elif self.type == 'fire' and other.type == 'water':
                return not_very_effective(self)
            elif self.type == 'rock' and other.type == 'fire':
                return super_effective(self)
            elif self.type == 'rock' and other.type == 'grass' or self.type == 'grass' and other.type == 'rock':
                return normal(self)
            elif self.type == 'rock' and other.type == 'water' or self.type == 'water' and other.type == 'rock':
                return normal(self)
            elif self.type == 'fire' and other.type == 'rock':
                return not_very_effective(self)
            elif self.type == 'fire' and other.type == 'fire':
                return not_very_effective(self)
            elif self.type == 'water' and other.type == 'water':
                return not_very_effective(self)
            elif self.type == 'grass' and other.type == 'grass':
                return not_very_effective(self)
            elif self.type == 'rock' and other.type == 'rock':
                return normal(self)
        elif self.is_knocked_out == False and other.health <= 0:
            return print(self.name + " cannot attack " + other.name + " because hes allready knocked out!")
        else:
            return print(self.name + " is knocked out and cannot attack!")

    def xp_gain(self):
        self.xp += 5
        print(self.name + " has gained 5 exp and now has " + str(self.xp) + " exp")
        if self.xp == 5:
            self.level_up()
        if self.xp == 15:
            self.level_up()
        if self.xp == 30:
            self.level_up()
        if self.xp == 50:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.health += 5
        if self.level == 3:
            self.evolve()
        elif self.level == 5:
            self.evolve()
        else:
            return print(self.name + " has leveled up and now is level " + str(self.level) + " with " + str(self.max_health) + " maximum health!")

    def evolve(self):
        if self.level == 3:
            self.max_health += 5
            return print(self.version_1 + " has reached level 3 and has now evolved into " + self.version_2 + " with " + str(self.max_health) + " maximum health!")
        elif self.level == 5:
            self.max_health += 10
            return print(self.version_2 + " has reached level 5 and has now evolved into " + self.version_3 + " with " + str(self.max_health) + " maximum health!")

class Trainer():
    def __init__(self, name, num_of_pokemon, num_of_potions, currently_active_pokemon):
        self.name = name
        self.num_of_pokemon = num_of_pokemon                                                                    #NUM OF POKEMON IS A LIST
        self.num_of_potions = num_of_potions
        self.currently_active_pokemon = currently_active_pokemon
    
    def change_active_pokemon(self, pokemon_num):
        if self.num_of_pokemon[pokemon_num].is_knocked_out == False:
            self.currently_active_pokemon = pokemon_num
            return print(self.name + " changed his Pokemon to " + str(self.num_of_pokemon[pokemon_num]))
        else:
            return print(self.name + " has tried to switch Pokemons to " + str(self.num_of_pokemon[pokemon_num]) + " but hes knocked out and cannot be switched to!")
    
    def use_potion(self):                                                                                       #ONLY THING MISSING IS WHEN HES ON FULL HP
        pot_1 = 5
        p = self.currently_active_pokemon
        self.num_of_pokemon[p].regaining_health(pot_1)
        self.num_of_potions -= 1
        return print(self.name + " had used a pot on " + str(self.num_of_pokemon[self.currently_active_pokemon])), print("Num of potions left " + str(self.num_of_potions))

    def t_attack(self, other):
        
        print(self.name + " has initiated an attack on " + other.name + "!")
        
        self.num_of_pokemon[self.currently_active_pokemon].attack(other.num_of_pokemon[other.currently_active_pokemon])
        return













charmander = Pokemon('Charmander', 1, 0, 'fire', 15, 15, False, 'Charmeleon', 'Charizard', 'Charmander')
bulbasaur = Pokemon('Bulbasaur', 1, 0, 'grass', 15, 15, False, 'Ivysaur', 'Venusaur', 'Bulbasaur')
squirtle = Pokemon('Squirtle', 1, 0, 'water', 15, 15, False, 'Wartortle', 'Blastoise', 'Squirtle')
geodude = Pokemon('Geodude', 1, 0, 'rock', 15, 15, False, 'Graveler', 'Onix', 'Geodude')
vulpix = Pokemon('Vulpix', 1, 0, 'fire', 15, 15, False, 'Ninetales', 'SixteenTales', 'Vulpix')
ponyta = Pokemon('Ponyta', 1, 0, 'fire', 15, 15, False, 'Rapidash', 'Mega strong totaly not invented 3rd evolotion yes', 'Ponyta')
oddish = Pokemon('Oddish', 1, 0, 'grass', 15, 15, False, 'Gloom', 'Vileplume', 'Oddish')
treecko = Pokemon('Treecko', 1, 0, 'grass', 15, 15, False, 'Grovyle', 'Sceptile', 'Treecko')
magikarp = Pokemon('Magikarp', 1, 0, 'water', 15, 15, False, 'Gyarados', 'Mega Gyarados', 'Magikarp')
wailmer = Pokemon('Wailmer', 1, 0, 'water', 15, 15, False, 'Wailord', 'Wailking', 'Wailmer')
aron = Pokemon('Aron', 1, 0, 'rock', 15, 15, False, 'Lairon', 'Aggron', 'Aron')
rhyhorn = Pokemon('Ryhorn', 1, 0, 'rock', 15, 15, False, 'Rhydon', 'Rhydongz', 'Ryhorn')

ashe = Trainer('Ashe', [charmander, bulbasaur, geodude, oddish, magikarp, aron], 5, 0)
brook = Trainer('Brook', [squirtle, vulpix, aron, treecko, wailmer, ponyta], 5, 0)
blain = Trainer('Blain', [geodude, treecko, magikarp, charmander, bulbasaur, wailmer], 5, 0)
misty = Trainer('Misty', [squirtle, wailmer, treecko, aron, vulpix, oddish], 5, 0)
brook.change_active_pokemon(2)
ashe.t_attack(brook)

brook.t_attack(ashe)
ashe.t_attack(brook)
brook.t_attack(ashe)
ashe.t_attack(brook)
brook.t_attack(ashe)
ashe.use_potion()
ashe.t_attack(brook)
brook.t_attack(ashe)
ashe.change_active_pokemon(1)
brook.t_attack(ashe)
ashe.t_attack(brook)
brook.use_potion()
ashe.t_attack(brook)
brook.t_attack(ashe)
brook.t_attack(ashe)
ashe.change_active_pokemon(5)
print(ashe.num_of_pokemon[ashe.currently_active_pokemon].level)