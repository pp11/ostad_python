#  Create a class named Car with the attributes brand, model, and year. 
# Include a constructor to initialize these values 
# and a method display_info() to print all the car details. 
# Then create an object of the Car class and display its details.

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Car details - Brand: {self.brand}, Model: {self.model}, Year: {self.year}")


car = Car("Nissan", "S109099", 2025)
car.display_info()