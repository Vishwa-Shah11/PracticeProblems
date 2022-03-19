a = int(input())
b = int(input())

#def pattern(a,b):
for i in range(a):
    if (i == 0 or i == a-1):
        print(b*'o')
    else:
        print(f"o{' '*(b-2)}o")