from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    def stop(self):
        pass

    def fuel_type(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car Started")

    def stop(self):
        print("Car Stopped")

    def fuel_type(self):
        print("Petrol") 

class Bike(Vehicle):
    def start(self):
        print("bike Started")

    def stop(self):
        print("Bike Stopped")

    def fuel_type(self):
        print("Petrol") 

class Tesla(Vehicle):
    def start(self):
        print("Tesla Started")

    def stop(self):
        print("Tesla Stopped")

    def fuel_type(self):
        print("Electric")

print("=>Car Details")
my_car = Car()
my_car.start()
my_car.stop()
my_car.fuel_type()

print("\n=>Bike Details")
my_bike = Bike()
my_bike.start()
my_bike.stop()
my_bike.fuel_type()

print("\n=>Tesla Details")
my_tesla = Tesla()
my_tesla.start()
my_tesla.stop()
my_tesla.fuel_type()