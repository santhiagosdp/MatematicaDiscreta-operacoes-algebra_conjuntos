a = [1, 2, 3, 4, 8 , 11]
b = [2, 3, 4, 5, 10]
print('Conjunto A', a)
print('Conjunto B', b)
print("")

print("UNIÃO (A ∪ B) ou (B ∪ A)")
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
print (u)
print("")

print("INTERSECÇÃO (A ∩ B)")
i=[]
for e in u: #percorrer U
    for item_a in a: #percorrer A 
        if(e==item_a):
            for item_b in b: #percorrer B   
                if(e==item_b):
                    i.insert(0, e)
print (i)
print("")

print("DIFERENÇA ENTRE A e B (A-B)")
d=[]
for e in u: #percorrer U
    for item_a in a: #percorrer A 
        verif=0
        if(e==item_a):
            for item_b in b: #percorrer B   
                if(e==item_b):
                    verif=1
                    break
            if(verif==0):
                d.insert(0,e)
print (d)
print("")

print("DIFERENÇA ENTRE B e A (B-A)")
d=[]
for e in u: #percorrer U
    for item_b in b: #percorrer B 
        verif=0
        if(e==item_b):
            for item_a in a: #percorrer A   
                if(e==item_a):
                    verif=1
                    break
            if(verif==0):
                d.insert(0,e)
print (d)
print("")
