#UNIAO
def insere(A,a):
  valid=0
  for item in A:
    if(item == a):
        valid=1
        return A
  if(valid==0):
    A.append(a)
    return A

def uniao(A,B):
  u = []
  for e in A:
    u=insere(u,e)
  for e in B:
    u=insere(u,e)
  return u
#FIM UNIÇAO
print('uniao',uniao([1,2,3,4],[4,6,7,1,9,0]))

#Intersecção
def interseccao(A,B):
  I = []
  U = []
  U =uniao(A,B)

  for elemDa_U in U:
    for elemDe_A in A:
      if(elemDe_A == elemDa_U):
        for elemDe_B in B:
          if(elemDe_B == elemDa_U):
            I.append(elemDa_U)
  return I
#Fim-Intersecção
print('Intersecção',interseccao([1,2,3,4],[4,6,7,1,9,0]))
