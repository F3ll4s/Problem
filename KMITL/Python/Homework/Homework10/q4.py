def print_table(x):
    for i in x:
        for j in range(len(i)):
            print(i[j],end="\t")
        print("")
print_table([["X","Y"],[0,0],[10,10],[200,200]])
print("")
print_table([
    ["ID","Name","Surname"],
    ["001","Guido","van Rossum"],
    ["002","Donald","Knuth"],
    ["003","Gordon","Moore"],
    ])