import json

# Item and Weapon Classes
class Item:
    def __init__(self, name, legendary=False, damage=0, item_type=''):
        self.name = name
        self.legendary = legendary
        self.damage = damage
        self.type = item_type
        self.owner = None

    def to_json(self):
        """Converts the item to a JSON encodable object (dictionary)."""
        return {
            'name': self.name,
            'legendary': self.legendary,
            'damage': self.damage,
            'type': self.type
        }

    @classmethod
    def from_json(cls, json_str):
        """
        Creates an item instance from a JSON string.
        :param json_str: JSON string representing an item
        :return: Item instance
        """
        data = json.loads(json_str)
        return cls(name=data['name'], legendary=data['legendary'],
                   damage=data['damage'], item_type=data['type'])

    def __str__(self):
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


# Inventory Class
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

    def to_json(self):
        """Converts the inventory and its items to a JSON encodable object."""
        return {
            'owner': self.owner,
            'items': [item.to_json() for item in self.items] 
        }

    @classmethod
    def from_json(cls, json_str):
        """
        Creates an inventory instance from a JSON string.
        :param json_str: JSON string representing an inventory
        :return: Inventory instance
        """
        data = json.loads(json_str)
        inventory = cls(owner=data['owner'])
        for item_data in data['items']:
            item_type = item_data['type']
            if item_type == 'sword':
                inventory.add_item(SingleHandedWeapon.from_json(json.dumps(item_data)))
            elif item_type == 'katana':
                inventory.add_item(DoubleHandedWeapon.from_json(json.dumps(item_data)))
            elif item_type == 'spear':
                inventory.add_item(Pike.from_json(json.dumps(item_data)))
            elif item_type == 'bow':
                inventory.add_item(RangedWeapon.from_json(json.dumps(item_data)))
        return inventory

    def view(self, item_type=None):
        if item_type:
            return [str(item) for item in self.items if isinstance(item, item_type)]
        return [str(item) for item in self.items]


# Example Usage
if __name__ == "__main__":
    # Create weapon instances
    master_sword = SingleHandedWeapon(name="Master Sword", legendary=True, damage=300, item_type='sword')
    muramasa = DoubleHandedWeapon(name="Muramasa", legendary=True, damage=580, item_type='katana')
    gungnir = Pike(name="Gungnir", legendary=True, damage=290, item_type='spear')
    belthronding = RangedWeapon(name="Belthronding", legendary=True, damage=500, item_type='bow')

    # Create inventory and add items
    beleg_backpack = Inventory(owner='Beleg')
    beleg_backpack.add_item(belthronding)
    beleg_backpack.add_item(master_sword)
    beleg_backpack.add_item(muramasa)
    beleg_backpack.add_item(gungnir)

    # Serialize to JSON
    inventory_json = beleg_backpack.to_json()
    json_str = json.dumps(inventory_json, indent=4)
    print("Serialized Inventory:\n", json_str)

    # Deserialize from JSON
    new_inventory = Inventory.from_json(json_str)
    print("\nDeserialized Inventory (view):")
    for item in new_inventory.view():
        print(item)

    # Save to file
    with open('lab06/inventory.json', 'w') as f:
        json.dump(beleg_backpack, f, default=lambda obj: obj.to_json(), indent=4)

