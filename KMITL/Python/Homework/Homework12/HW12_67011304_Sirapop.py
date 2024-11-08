# Question 1
abbreviation_dict = {
    "be": "b",
    "because": "cuz",
    "see": "c",
    "the": "da",
    "okay": "ok",
    "are": "r",
    "you": "u",
    "without": "w/o",
    "why": "y",
    "see you": "cu",
    "ate": "8",
    "great": "gr8",
    "mate": "m8",
    "wait": "w8",
    "later": "l8r",
    "tomorrow": "2mro",
    "for": "4",
    "before": "b4",
    "once": "1ce",
    "and": "&",
    "your": "ur",
    "you're": "ur",
    "as far as I know": "afaik",
    "as soon as possible": "ASAP",
    "at the moment": "atm",
    "be right back": "brb",
    "by the way": "btw",
    "for your information": "FYI",
    "in my humble opinion": "imho",
    "in my opinion": "imo",
    "laughing out loud": "lol",
    "oh my god": "omg",
    "rolling on the floor laughing": "rofl",
    "talk to you later": "ttyl"
}

def textese(x):
    if x in abbreviation_dict:
        return abbreviation_dict[x]
def untextese(x):
    for keys, values in abbreviation_dict.items():
        if values == x:
            return keys
        
print(textese("see"))
print(untextese("cuz"))
# Question 2
def composite(dict1, dict2):
    result = {}
    for k, v in dict1.items():
        if v in dict2:
            result[k] = dict2[v]
    return result


dict1 = {'a': 'p', 'b': 'r', 'c': 'q', 'd': 'p', 'e': 's'}
dict2 = {'p': '1', 'q': '2', 'r': '3', 's': '9'}
print(composite(dict1, dict2))
# Question 3
def product(*sets):
    if len(sets) == 1:
        return {(x,) for x in sets[0]}
    
    result = set()
    rest_product = product(*sets[1:])
    
    for x in sets[0]:
        for rest in rest_product:
            result.add((x,) + rest)
    
    return result

s1 = {1, 2, 3}
s2 = {'p', 'q'}
s3 = {'a', 'b', 'c'}
# Question 6
print(product(s1, s2))
print(product(s1, s2, s3))
print(product(s1))

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

