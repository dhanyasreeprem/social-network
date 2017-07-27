class Vehicle:
    def __init__(self,name):
        self.name = name
        self.wheels = 0
        self.ignition = False
        self.passengers = []
    def num_wheels(self, wheels):
        self.wheels = wheels
    def ignition(self, key):
        self.ignition = key
    def add_passengers(self, passenger):
        self.passengers.append(passenger)

def main():
    #put all the stuff I want to do wiht the different vehicles in here
    SuperCar = Vehicle("Tesla")
    SuperCar.num_wheels(5)
    SuperCar.add_passengers("Lilly Singh")

    SpaceCraft = Vehicle("NASA")
    SpaceCraft.add_passengers("Tom Hanks")

    print ("Passengers in SuperCar = " + str(SuperCar.passengers[0]))
    print("Passengers in SpaceCraft = " + str(SpaceCraft.passengers[0]))
