# def sum_of_digits(x):
#     x = str(x)
#     total = 0
#     for i in x:
#         if i.isdigit():
#             i = int(i)
#             total += i      
#     return total  
# print(sum_of_digits("orwkogpot345"))

def sum_of_digit(x):
    total = 0
    for i in x:
        i = int(i)
        total += i
    print(total)

sum_of_digit("23456")

