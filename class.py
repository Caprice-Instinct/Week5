# class girl:
#     skin_color = "black"
#     age = 21
#     height = 5.4
#     name = "Maddie"
    
#     def girlie(self):
#         print("She is just a girl!")
        
        
# first_girl = girl()
# print(first_girl.skin_color, first_girl.name)
# first_girl.girlie()

# Constructors
# class Car:
#     def __init__(self, color, model):
#         self.color = color
#         self.model = model

# my_car = Car("red", "BMW")
# print(my_car.color)

# your_car = Car("white", "Volvo")


# Inheritance
# class girl:
#     skin_color = "black"
#     age = 21
#     height = 5.4
#     name = "Maddie"
    
#     def girlie(self):
#         print("She is just a girl!")
        
# class sister(girl):
    
    
# Polymorphism
# class Animal:
#     def speak(self):
#         print("Animal sound")
    
# class Dog(Animal):
#     def speak(self):
#         print("Woof!")
        
# class Cat(Animal):
#     def speak(self):
#         print("Meow!")
        
        
# dog1 = Dog()
# dog1.speak()

# cat1 = Cat()
# cat1.speak()

# Encapsulation
class SecretStash:
    def __init__(self):
        self.__chocolates = 10  # Private attribute

    def take_chocolate(self):
        if self.__chocolates > 0:
            self.__chocolates -= 1
            print("One chocolate taken!")
        else:
            print("No chocolates left 😢")

stash = SecretStash()
stash.take_chocolate()