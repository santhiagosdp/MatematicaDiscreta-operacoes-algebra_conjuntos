#a = [1, 2, 3, 4, [1,2]]
a=['a','b','c','d']
b = [1,2,3,4,5,6,7,8,9]
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

print("COMPLEMENTO A em relação a B ")
c=[]
ehsubconjunto=0;

for elem_b in b:
    for elem_a in a:
        if(elem_a==elem_b):
            ehsubconjunto=ehsubconjunto+1
            
#print('qtsitenA=',subconjunto)
if(len(a)==ehsubconjunto): #se A for subconjunto de B
    for e in u: #percorrer U
        for item_b in b: #percorrer B
            verif=0
            if(e==item_b):
                for item_i in i: #percorrer I (intersecçao)
                    if(e==item_i):
                        verif=1
                        break
                if(verif==0):
                    c.insert(0,e)
    print (c)
else:
    print('Não se aplica, pois A não é SubConjunto de B')    
print("")

print("CONJUNTO DAS PARTES DE A ") #∅
p=['∅', a]
cont=0

for elem_a in a:
    pos=1+cont
    c = [elem_a]
    p.insert(0,c)
    while (pos < len(a)):
        c=[elem_a, a[pos]]
        p.insert(0,c)
        pos=pos+1
    cont=cont+1
print(p)
print(len(p))
print("")


#Produto cartesiano
#União disjunta