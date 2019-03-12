#UNIAO
def insere(A,a):
  valid=0
  for item in A:
    if(item == a):
        valid=1
        return A
  if(valid==0):
    A.insert(0,a)
    return A

def uniao(a,b):
  u = []
  for e in a:
    u=insere(u,e)
  for e in b:
    u=insere(u,e)
  return u
#FIM UNIÇAO


print('uniao',uniao([1,2,3,4],[4,6,7,1,9,0]))
print('interesecção',interseccao([]))
