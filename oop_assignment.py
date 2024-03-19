#Initialise a Person object with the given name, age and gender
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print(f"Hello, my name is {self.name}. I am {self.age} years old and I am {self.gender}.")

#Update the person's age with the given new_age
    def update_age(self, new_age):
        self.age = new_age

        
#Update the person's name with the given new_name
    def update_name(self, new_name):
        self.name = new_name


person1 = Person("Martha", 40, "Female")
person1.introduce()

person1.update_age(42)
person1.update_name("Marsha")
person1.introduce()
