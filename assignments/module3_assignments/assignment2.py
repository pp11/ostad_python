# Create three classes Animal, Mammal, and Dog where Animal has a method eat(), 
# Mammal inherits from Animal and has a method walk(), 
# and Dog inherits from Mammal and has a method bark(). 
# Create an object of Dog and demonstrate all three methods. 
# Also, create a class Calculator with an add() method that can take either two or three parameters, 
# and then create a subclass AdvancedCalculator that overrides the add() method 
# to add any number of parameters using variable-length arguments. 
# Demonstrate both functionalities.


class Animal:
    def eat(self):
        print("Animal class")

class Mammal(Animal):
    def walk(self):
        print("this is Mammal class")

class Dog(Mammal):
    def bark(self):
        print("this is Dog class")


dog1=Dog()

dog1.eat()
dog1.walk()
dog1.bark()


#part 2 

class Calculator:

    def __init__(self, num1, num2, num3=None):
        self.num1=num1
        self.num2=num2
        self.num3=num3

    def add(self):
        if self.num3!=None:
            sum=self.num1+self.num2+self.num3
        else:
            sum=self.num1+self.num2
        print("the result of the sum is :" , sum)
        

class AdvancedCalculator(Calculator):

    def __init__(self, *nums):
        self.nums=nums

    def add(self):
        result=sum(self.nums)
        print("the sum  of all numbers is ", result)


calc= Calculator(11,2,25)
calc.add()

calc2=Calculator(20,58)
calc2.add()

advCalc=AdvancedCalculator(2,3,6,5,50)
advCalc.add()
