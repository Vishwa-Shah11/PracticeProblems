def depth(exp):
    """
    Compute the maximum nesting depth
    
    Argument:
        exp: string
    Return:
        result: integer
    """
    max = 0
    cmax = 0
    n = len(exp)
    
    for i in range(n):
        if (exp[i] == '('):
            cmax += 1
            
            if cmax > max:
                max = cmax
                
        elif (exp[i] == ')'):
            if cmax > 0:
                cmax -=1
    return max

print(depth('(()(()))()'))s