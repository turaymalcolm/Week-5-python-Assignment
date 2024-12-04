# Base Class
class Superhero:
    def __init__(self, name, power, weakness):
        self.name = name
        self.power = power
        self.weakness = weakness

    def display_info(self):
        return f"Superhero Name: {self.name}, Power: {self.power}, Weakness: {self.weakness}"

    def fight_crime(self):
        return f"{self.name} is using their {self.power} to fight crime!"

# Derived Class
class TechHero(Superhero):
    def __init__(self, name, power, weakness, gadgets):
        super().__init__(name, power, weakness)
        self.gadgets = gadgets

    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, Gadgets: {', '.join(self.gadgets)}"

    def fight_crime(self):
        return f"{self.name} is using their gadgets ({', '.join(self.gadgets)}) to fight crime!"

# Create instances
hero1 = Superhero("InvisiMan", "Invisibility", "Sound")
hero2 = TechHero("GadgetGirl", "Engineering", "EMP Attacks", ["Utility Belt", "Grappling Hook"])

# Display information
print(hero1.display_info())
print(hero1.fight_crime())
print(hero2.display_info())
print(hero2.fight_crime())
