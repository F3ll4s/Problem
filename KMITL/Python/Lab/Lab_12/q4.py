def is_subset(sup,sub):
    new = []
    for i in sub:
        if i not in sup:
            new.append(i)
        else:
            pass
    if len(new) >= 1:
        print("False")
    else:
        print("True")
        
sup = set([1,2,3,4])
sub = set([1,2,4])

sub2 = set([1,2,5])
is_subset(sup,sub2)