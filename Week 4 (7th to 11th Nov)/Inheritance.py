class Vehicle:
    def general_usage(self):
        print("The general usage of vehicle class is for Transportation")


class Car(Vehicle):
    def __init__(self):
        print("I am a Car")
        self.wheels = 4
        self.has_roof = True

    def specific_usage(self):
        self.general_usage()
        print("Specific use : Commute to work, vacation with family")


class MotorCycle(Vehicle):
    def __init__(self):
        print("I am a MotorCycle")
        self.wheels = 2
        self.has_roof = False

    def specific_usage(self):
        self.general_usage()
        print("Specific use : Road trip, racing")


c = Car()
c.general_usage()
c.specific_usage()
m = MotorCycle()
m.specific_usage()
m.general_usage()
print(isinstance(c,MotorCycle))
print(issubclass(Car,Vehicle))
