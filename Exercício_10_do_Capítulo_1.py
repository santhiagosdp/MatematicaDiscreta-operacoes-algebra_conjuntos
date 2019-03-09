a = [1, 2, 3, 4, 11]
b = [2, 3, 4, 5, 10]
print('Conjunto A', a)
print('Conjunto B', b)
u = []

for e in a:
    valid=0
    for item in u:
        if(item == e):
            valid=1
            break
    if(valid==0):
        u.insert(0, e)
for e in b:
    valid=0
    for item in u:
        if(item == e):
            valid=1
            break
    if(valid== 0):
        u.insert(0,e)
print ('uniao', u )
