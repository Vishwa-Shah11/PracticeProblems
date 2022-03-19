#Type 1
#working
s = input()

given = 'abcdefghijklm'
convert = 'zyxwvutsrqpon'
l = []

for c in s:
    if (c in given):
        i = given.index(c)
        l.append(convert[i])
        #print(l)
    elif (c in convert):
        i = convert.index(c)
        l.append(given[i])
        #print(l)
v = ''
for i in l:
    v += i
print(v)







#Type 2
#working

s = input()
alpha = 'abcdefghijklmnopqrstuvwxyz'
encrypt = ''

for c in s:
    i = alpha.index(c)
    encrypt += alpha[-(i+1)]

print(encrypt)