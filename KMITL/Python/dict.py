def count_operands_in_expr(x):
    if type(x[0]) == tuple and type(x[2]) == tuple:
        return count_operands_in_expr(x[0]) + count_operands_in_expr(x[2])
    elif type(x[0]) == tuple and type(x[2]) == int:
        return count_operands_in_expr(x[0]) + 1
    else:
        return 2
    
print(count_operands_in_expr ( (3, '**', 4) ))