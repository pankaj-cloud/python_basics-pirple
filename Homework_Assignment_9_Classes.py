"""
Details:
Create a class called "Vehicle" and methods that allow you to set the "Make", "Model", "Year,", and "Weight".
The class should also contain a "NeedsMaintenance" boolean that defaults to False, and and "TripsSinceMaintenance"
Integer that defaults to 0. Next an inheritance classes from Vehicle called "Cars". T
he Cars class should contain a method called "Drive" that sets the state of a boolean isDriving to True.
It should have another method called "Stop" that sets the value of isDriving to false.Switching isDriving from true to
false should increment the "TripsSinceMaintenance" counter. And when TripsSinceMaintenance exceeds 100,
then the NeedsMaintenance boolean should be set to true. Add a "Repair" method to either class that resets
the TripsSinceMaintenance to zero, and NeedsMaintenance to false. Create 3 different cars,
using your Cars class, and drive them all a different number of times.
Then print out their values for Make, Model, Year, Weight, NeedsMaintenance, and TripsSinceMaintenance
"""

class Vehicle:
    def __init__(self, make, model, year, weight, needsMaintenance = False, tripsSinceMaintenance = 0):
        self.make = make
        self.model = model
        self.year = year
        self.weight = weight
        self.needsMaintenance = needsMaintenance
        self.tripsSinceMaintenance = tripsSinceMaintenance

    #setters
    def setMake(self, make):
        self.make = make

    def setModel(self, mode):
        self.mode = mode

    def setYear(self, year):
        self.year = year

    def setWeight(self, weight):
        self.weight = weight

    #getters
    def getMake(self):
        return self.make

    def getModel(self):
        return self.model

    def getYear(self):
        return self.year

    def getWeight(self):
        return self.weight

    def repair(self):
        self.tripsSinceMaintenance = 0
        self.needsMaintenance = False

# define cars class - inherited from vehicle class
class Cars(Vehicle):
    def __init__(self, make, model, year, weight, isDriving = False):
        Vehicle.__init__(self, make, model, year, weight)
        self.isDriving = isDriving

    def drive(self):
        self.isDriving = True

    def stop(self):
        if self.isDriving:
            self.tripsSinceMaintenance += 1
            if self.tripsSinceMaintenance > 100:
                self.needsMaintenance = True
        self.isDriving = False

# define plane class - inherited from vehicle class
class Plane(Vehicle):
    def __init__(self, make, model, year, weight, isFlying = False):
        Vehicle.__init__(self, make, model, year, weight)
        self.isFlying = isFlying

    def flying(self):
        if self.needsMaintenance == True:
            return False
        self.isFlying = True
        return True

    def landing(self):
        if self.isFlying:
            self.tripsSinceMaintenance += 1
            if self.tripsSinceMaintenance > 100:
                self.needsMaintenance = True
        self.isFlying = False

# print car attributes
def print_car_specs(car):
    print("========================")
    print('Make ',car.make)
    print('Model ',car.model)
    print('Year ',car.year)
    print('Weight ',car.weight)
    print('Needs Maintenance ',car.needsMaintenance)
    print('Trips Since Maintenance ',car.tripsSinceMaintenance)
    print('Weight ',car.weight)
    print("========================\n")

# print plane attributes
def print_plane_specs(plane):
    print("========================")
    print('Make ',plane.make)
    print('Model ',plane.model)
    print('Year ',plane.year)
    print('Weight ',plane.weight)
    print('Needs Maintenance ',plane.needsMaintenance)
    print('Trips Since Maintenance ',plane.tripsSinceMaintenance)
    print('Weight ',plane.weight)
    print("========================\n")

# creating three instances from Cars class
carOne = Cars("Honda", "Civic", 2006, 1033 )
carTwo = Cars("volkswagen group", "City", 2002, 1038 )
carThree = Cars("volkswagen group", "Jazz", 2012, 1023 )

# creating two objects from Plane class
planeOne = Plane("Boeing", "A Class", 1992, 1050)
planeTwo = Plane("Boeing", "B Class", 1982, 2004)

# printing cars and plane attributes
print_car_specs(carOne)
print_car_specs(carTwo)
print_car_specs(carThree)
print_plane_specs(planeOne)
print_plane_specs(planeTwo)