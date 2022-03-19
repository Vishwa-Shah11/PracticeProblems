def is_prime(n):
    flag = True
    if n <= 1:
        flag = False
    for i in range(2,n):
        if (n % i == 0):
            flag = False
    return flag

def primes_galore(L):
    """
    Compute number of primes located at prime indices

	Argument:
    	L: list of integers
    Return:
    	result: integer
    """
    L1 = []
    for i in range(len(L)):
        if (is_prime(i)):
            L1.append(L[i])

    count = 0 

    for i in L1:
        if (is_prime(i)):
            count += 1

    return count

l = [1, 3, 11, 18, 17, 5, 6, 8, 10]
k = [1, 2, 3, 4, 5, 6, 7, 8, 9]
s = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]

print(primes_galore(l))
print(primes_galore(k))
print(primes_galore(s))