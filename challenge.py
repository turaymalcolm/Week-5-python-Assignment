# Base Class
class Vehicle:
    def move(self):
        raise NotImplementedError("This method should be overridden by subclasses")

# Derived Classes
class Car(Vehicle):
    def move(self):
        return "Driving 🚗"

class Plane(Vehicle):
    def move(self):
        return "Flying ✈️"

class Boat(Vehicle):
    def move(self):
        return "Sailing 🚤"

# Testing Polymorphism
vehicles = [Car(), Plane(), Boat()]
for vehicle in vehicles:
    print(vehicle.move())
