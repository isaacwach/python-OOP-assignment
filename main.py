class Person:
    def __init__(self, name, age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print(f"Meet {self.name} who is a {self.gender} and is {self.age} years old")

person1 = Person("Zacs", 34, "Male")
person1.introduce()