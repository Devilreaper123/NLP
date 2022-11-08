class Human:
    def __init__(self, n, o):
        self.name = n
        self.occupation = o

    def do_work(self):
        if self.occupation == "Tenis Player":
            print(f"{self.name} is a {self.occupation}")
        elif self.occupation == 'Software Engineer':
            print(f"{self.name} is a {self.occupation}")

    def speak(self):
        print(f"{self.name} says how are you?")


Ronit = Human('Ronit', "Software Engineer")
Maria = Human('Maria Sharpova', "Tenis Player")
Ronit.do_work()
Ronit.speak()
Maria.do_work()
Maria.speak()
