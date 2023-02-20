class Dog:

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print ("Woof!")



    def Doggy(self, n):
            dogid = []
            for i in range(n):
                dogid.append(i)
            print(dogid)


dog = Dog("Buddy", "Labrador")
dog.bark()  # outputs "Woof!"
dog.Doggy(5)
