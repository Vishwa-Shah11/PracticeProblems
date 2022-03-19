def std_dev(X):
    """
    Compute the standard deviation
    
    Argument:
        X: list of integers
    Return:
        sigma: float
    """
    mean = sum(X)/len(X)
    a = 0
    for i in X:
        a += ((i-mean)**2)/(len(X)-1)
    s = a**0.5
    return s
    
X = [float(x) for x in input().split(',')]
sigma = std_dev(X)
print(f'{sigma:.2f}')