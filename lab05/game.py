class Item:
    def __init__(self, name, rarity="common", description=""):
        self.name = name
        self.description = description
        self.rarity = rarity
        self._ownership = ""

    def pick_up(self, character: str) -> str:
        self._ownership = character
        return f"{self.name} is now owned by {character}"

    def throw_away(self) -> str:
        self._ownership = ""
        return f"{self.name} has been thrown away"

    def use(self) -> str:
        if self._ownership:
            return f"{self.name} is used"
        return ""

    def __str__(self):
        return f"{self.name} (Rarity: {self.rarity}, Description: {self.description})"
    
class Weapon(Item):
    def __init__(self, name, damage, weapon_type, rarity="common"):
        super().__init__(name, rarity)
        self.damage = damage
        self.type = weapon_type
        self.active = False
        self.attack_modifier = 1.0 if rarity != "legendary" else 1.15

    def equip(self):
        self.active = True
        return f"{self.name} is equipped"

    def use(self):
        if self.active:
            return f"{self.name} is used, dealing {self.damage * self.attack_modifier} damage"
        return ""

    def __str__(self):
        return f"{self.name} (Weapon: {self.type}, Damage: {self.damage}, Rarity: {self.rarity})"
    
class Shield(Item):
    def __init__(self, name, defense, broken=False, rarity="common"):
        super().__init__(name, rarity)
        self.defense = defense
        self.broken = broken
        self.active = False
        self.defense_modifier = 1.0 if rarity != "legendary" else 1.10

    def equip(self):
        self.active = True
        return f"{self.name} is equipped"

    def use(self):
        if self.active:
            modifier = 0.5 if self.broken else 1.0
            return f"{self.name} is used, blocking {self.defense * self.defense_modifier * modifier} damage"
        return ""

    def __str__(self):
        return f"{self.name} (Shield, Defense: {self.defense}, Rarity: {self.rarity}, Broken: {self.broken})"
    

class Potion(Item):
    def __init__(self, name, potion_type, value, effective_time, rarity="common"):
        super().__init__(name, rarity)
        self.potion_type = potion_type
        self.value = value
        self.effective_time = effective_time
        self.empty = False

    def use(self):
        if not self.empty:
            self.empty = True
            if self.effective_time > 0:
                return f"{self._ownership} used {self.name}, and {self.potion_type} increased by {self.value} for {self.effective_time}s"
            return f"{self.name} is consumed"
        return ""

    def __str__(self):
        return f"{self.name} (Potion: {self.potion_type}, Value: {self.value}, Rarity: {self.rarity})"

    @classmethod
    def from_ability(cls, name, owner, potion_type):
        return cls(name, potion_type, 50, 30, "common")
    

bonk = Weapon(name='Bonk', damage=5000, weapon_type='hammer', rarity='legendary')
print(bonk.pick_up('Pauly D'))   
print(bonk.equip())             
print(bonk.use())              

bing_shield = Shield(name='Bing', defense=50, broken=False, rarity='epic')
print(bing_shield.pick_up('Pauly D'))  
print(bing_shield.equip())            
print(bing_shield.use())            
print(bing_shield.throw_away())       
print(bing_shield.use())              

attack_potion = Potion.from_ability(name='atk potion temp', owner='Pauly D', potion_type='attack')
print(attack_potion.use())  
print(attack_potion.use())  





