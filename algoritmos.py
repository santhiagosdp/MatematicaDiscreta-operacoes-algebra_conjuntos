#METODOS PARA SEREM USADOS NO MENU

#INSERIR NO VETOR SE NÃO EXISTIR
def insere(A,a):
  for item in A:
    if(item == a):
        return A #Se exisitir, retorna A sem add
  A.append(a) #se n entrar no If, add a e retorna A
  return A 
#FIM-INSERE

#UNIÃO
def uniao(A,B):
  u = []
  for item in A:
    u=insere(u,item) #chama metodo insere
  for item in B:
    u=insere(u,item)
  return u
#FIM-UNIÃO

#INTERSECÇÃO
def interseccao(A,B):
  I = []
  U =uniao(A,B)
  for elemDa_U in U:
    for elemDe_A in A:
      if(elemDe_A == elemDa_U):
        for elemDe_B in B:
          if(elemDe_B == elemDa_U):
            I.append(elemDa_U)
  return I
#FIM-INTERSECÇÃO

#DIFERENÇA A-B
def diferenca(A,B):
  Dif = []
  U = uniao(A,B)
  for item in U:
    for a in A:
      verifica=0
      if (a == item):
        for b in B:
          if (item == b):
            verifica=1
            break
        if(verifica==0):
          Dif.append(item)
  return Dif
#FIM-DIFERENÇA

#COMPLEMENTO
def ehsbuconj(A,B):
  cont=0
  for elem_b in B:
    for elem_a in A:
        if(elem_a==elem_b):
            cont=cont+1
  if(len(A)==cont): #se A for subconjunto de B faça
    return True
  else:
    return False

def complemento(A,B):
#todos de B que não está em A se A for subconj de B
  c=[]
  u = uniao(A,B) 

  if(ehsbuconj(A,B)):
    for item_u in u: #percorrer U
      for item_b in B: #percorrer B
        verif=0
        if(item_u == item_b):
          for item_a in A: #percorrer I (intersecçao)
            if(item_u == item_a):
              verif=1
              break
          if(verif==0):
            c.insert(0,item_u)
    return c
  else:
    #c= "{}{}{}{}".format("Não se aplica, pois: ",A," não é SubConjunto de: ",B)
    c= f'{"Não se aplica, pois:"}{A}{" não é SubConjunto de: "}{B}' 
    return c
#FIM-COMPLEMENTO

#CONJUNTO DAS PARTES - usar recursividade.
def conjunto_partes(A):
  p=['∅', A] 
  cont=0

  for elem_a in A:
    pos=1+cont
    c = [elem_a]
    p.append(c)
    while (pos < len(A)):
      c=[elem_a, A[pos]]
      p.append(c)
      pos=pos+1
    cont=cont+1
  return p

#FIM-CONJUNTO DAS PARTES

#PRODUTO CARTESIANO

print("PRODUTO CARTESIANO")
x = ['a','b','c','d']
z = ['a','b']
pc = []

for i in x:
  for j in z:
    elem=[i,j]
    pc.insert(0,elem)
print ("produto cartesiano de ",x," e ",z)
print (pc)

#FIM-PRODUTO CARTESIANO


print('uniao:',uniao([1,5,8,4,2,3],[5,4,5,3,2,1,5]))

print('Intersecção:',interseccao([1,2,3,4],[4,6,7,1,9,0]))

print('Diferença:',diferenca([1,2,3,4,6],[1,4,6,7,9,0]))

print('Complemento:',complemento([1,2,3,9],[1,2,3,4,5]))

print('Conjunto das partes: ', conjunto_partes([1,2,3]))

