class Animal:
    def __init__(self,name):
        self.name = name 
        
    def speak(self):
        return 'I am an animal'
    
class Dog(Animal):
    
    def speak(self):
        return 'Woof woof!'
    
dog = Dog('tuppy')
print(dog.name)
print(dog.speak())