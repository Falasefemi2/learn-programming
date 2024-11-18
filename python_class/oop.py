# Object-Oriented Programming (OOP)
# Object-Oriented Programming is a programming paradigm that revolves around the concept of objects, which can represent real-world entities with attributes (data) and behaviors (methods).

# Lesson 1: Classes and Objects
# Class:

# A blueprint for creating objects.
# Defined using the class keyword.

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

# Object:

# An instance of a class.
my_dog = Dog("Buddy", "Golden Retriever")
print(my_dog.name)
print(my_dog.breed)

# Lesson 2: Methods
# Instance Methods:

# Functions inside a class that operate on instances.
# Always include self as the first parameter.

class Cat:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        
    def meow(self):
        return f"{self.name} says Meow!"
    
    def colors(self):
        return f"{self.name} color is {self.color}"
    
my_cat = Cat("Big catt", "Yellow")
print(my_cat.meow())
print(my_cat.colors())

# Special Methods (Dunder Methods):

# Methods with double underscores, e.g., __init__ for initialization.

# Example:

# __str__: Defines how an object is represented as a string.
class Dogs:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def __str__(self):
        return f"{self.name} is a {self.breed}"

my_dog = Dogs("Buddy", "Golden Retriever")
print(my_dog)  # Output: Buddy is a Golden Retriever

# Lesson 3: Inheritance
# Inheritance allows a class to derive properties and methods from another class.

class Animal:
    def __init__(self, name):
        self.name = name
        
    def eat(self):
        return f"{self.name} is eating"
    
class Doged(Animal):
    def bark(self):
        return f"{self.name} says woof"
    
my_dogs = Doged("Buddy")
print(my_dogs.eat())
print(my_dogs.bark())

# Lesson 4: Encapsulation
# Encapsulation restricts access to certain data or methods.

# Example:

# Use underscores (_) for protected attributes and double underscores (__) for private ones.
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance # Private attribute
        
    def deposit(self, amount):
        self.__balance += amount
        
    def withdraw(self, amount):
        self.__balance -= amount
    
    def get_balance(self):
        return self.__balance
    
account = BankAccount(2000)
account.deposit(50)
account.withdraw(150)
print(account.get_balance())


# Your Exercise
# Part 1: Classes and Methods
# Create a class called Car with:

# Attributes: make, model, and year.
# A method display_info() that prints the car's details.
# Create an object of the Car class and call display_info().

# Part 2: Inheritance
# Create a base class Person with:

# Attributes: name and age.
# A method introduce() that prints: "Hi, I'm <name> and I'm <age> years old."
# Create a derived class Student that:

# Inherits from Person.
# Adds an attribute school.
# Overrides the introduce() method to also print the school name.
# Create a Student object and call its introduce() method.

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        
    def display_info(self):
        return f"the product is {self.make} and its {self.model} and created in {self.year}"
    
bugatti = Car("Toyota", "Black", "2024")
print(bugatti.display_info())


class Person1:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def introduce(self):
        return f"Hi, I'm {self.name} and I'm {self.age} years"
    
class Student(Person1):
    def __init__(self, name, age, school):
        super().__init__(name, age) # Inherit attributes from Person
        self.school = school
    # Override the introduce method
    def introduce(self):
        return f"Hi, I'm {self.name}, I'm {self.age} years old, and I study at {self.school}"

answer = Person1("Femi", 24)
print(answer.introduce())

student = Student("Femi", 24, "Lagos State University")
print(student.introduce())