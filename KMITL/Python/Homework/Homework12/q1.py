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