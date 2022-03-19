L = input().split(',')
L = [int(i) for i in L]
k = int(input())
p = k%len(L)
l = []
#l = L[-p:] + L[:-p]

for i in range(p):
    l.append(L[-(p-i)])
for i in range(len(L)-p):
    l.append(L[i])
for i in range(len(l)):
    if (i != (len(l)-1)):
        #print(i)
        print(int(l[i]), end = ',')
    else:
        print(int(l[i]), end = '')
    #l1.append(int(i))