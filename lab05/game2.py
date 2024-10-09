class Item:
    def __init__(self, name, legendary=False, damage=0, item_type=''):
        self.name = name
        self.legendary = legendary
        self.damage = damage
        self.type = item_type
        self.owner = None

    def __str__(self):
        # Utilized chatgpt to write the part where these symbols appeared
        presentation = (
            f"✨ Legendary Item: {self.name} ✨\n"
            f"Damage: {self.damage}\n"
            f"Type: {self.type}"
        ) if self.legendary else (
            f"Item: {self.name}\n"
            f"Damage: {self.damage}\n"
            f"Type: {self.type}"
        )
        return presentation



class Weapon(Item):
    def attack_move(self):
        raise NotImplementedError("Subclasses should implement this method")



class SingleHandedWeapon(Weapon):
    def _slash(self):
        return "You perform a quick slash!"

    def attack_move(self):
        return f"{self._slash()} You deal {self.damage} damage."



class DoubleHandedWeapon(Weapon):
    def _spin(self):
        return "You spin the weapon with great force!"

    def attack_move(self):
        return f"{self._spin()} You deal {self.damage} damage."



class Pike(Weapon):
    def _thrust(self):
        return "You thrust the pike forward!"

    def attack_move(self):
        return f"{self._thrust()} You deal {self.damage} damage."



class RangedWeapon(Weapon):
    def _shoot(self):
        return "You take aim and shoot an arrow!"

    def attack_move(self):
        return f"{self._shoot()} You deal {self.damage} damage."



class Inventory:
    def __init__(self, owner=None):
        self.owner = owner
        self.items = []

    def add_item(self, item):
        item.owner = self.owner
        self.items.append(item)

    def drop_item(self, item):
        if item in self.items:
            item.owner = None
            self.items.remove(item)

    def view(self, item_type=None):
        if item_type:
            return [str(item) for item in self.items if isinstance(item, item_type)]
        return [str(item) for item in self.items]

    def __iter__(self):
        return iter(self.items)

    def __contains__(self, item):
        return item in self.items



if __name__ == "__main__":
  
    master_sword = SingleHandedWeapon(name="Master Sword", legendary=True, damage=300, item_type='sword')
    muramasa = DoubleHandedWeapon(name="Muramasa", legendary=True, damage=580, item_type='katana')
    gungnir = Pike(name="Gungnir", legendary=True, damage=290, item_type='spear')
    belthronding = RangedWeapon(name="Belthronding", legendary=True, damage=500, item_type='bow')


    beleg_backpack = Inventory(owner='Beleg')


    beleg_backpack.add_item(belthronding)
    beleg_backpack.add_item(master_sword)
    beleg_backpack.add_item(muramasa)
    beleg_backpack.add_item(gungnir)

    print("Viewing all items in the inventory:")
    for item in beleg_backpack.view():
        print(item)


    if master_sword in beleg_backpack:
        print(f"\nUsing {master_sword.name}:")
        print(master_sword.attack_move())


    beleg_backpack.drop_item(master_sword)
    print("\nAfter dropping the Master Sword:")
    for item in beleg_backpack.view():
        print(item)


    print("\nUnique attack movements for remaining weapons:")
    for item in beleg_backpack:
        if isinstance(item, Weapon):
            print(f"{item.name}: {item.attack_move()}")
