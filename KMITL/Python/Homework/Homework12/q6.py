class StationaryGood:
    def get_cost(self):
        raise NotImplementedError("Subclasses should implement this method")

class Magazine(StationaryGood):
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def get_cost(self):
        return self.price

class Book(StationaryGood):
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def get_cost(self):
        return self.price * 0.9 

class Ribbon(StationaryGood):
    def __init__(self, length):
        self.length = length
    
    def get_cost(self):
        return self.length * 5  

def getTotalCost(basket):
    total = 0
    for item in basket:
        total += item.get_cost()
    return total


basket = [
    Magazine("Computer World", 70),  
    Magazine("Computer World", 70),
    Magazine("Computer World", 70),
    Book("Windows 7 for Beginners", 200),  
    Book("Windows 7 for Beginners", 200),
    Ribbon(10)  
]

print("Total cost:", getTotalCost(basket))
