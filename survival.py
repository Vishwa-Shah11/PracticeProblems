def survival(T):
    """
    Determine if the organism will survive or not
    
    Argument:
        T: integer
    Return:
        result: bool
    """
    for i in range(6):
        x = i
        for j in range(6):
            y = j
            f = 30 + x**2 + y**2 - 3*x - 4*y
            if (f <= T):
                return True
                break
            
    return False

print(survival(30))
print(survival(10))