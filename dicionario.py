#exercicio-funcao chave
def ProcuraChave(dicionario,valor):#quando a funcao usa algo que não ta dentro dela voce usa parametro de entrada (coisa dentro dos ())
    lista=[]
    for x,y in dicionario.items():#x assume valor da chave e y do valor
        if valor==y:
            lista.append(x)
    return lista


palavras={
    'alpha':1,
    'bravo':2,
    'charlie':1,
    'delta':3,
    'echo':1
}
#print(ProcuraChave(palavras,1))
#print(ProcuraChave(palavras,2))
#print(ProcuraChave(palavras,4))

for x in range(1,5):
    print(x,":")
    print(ProcuraChave(palavras,x))

#dicionario como parametro serve pra funcao ter acesso ao dicionario 
# 'palavras',que nao ta dentro da funcao, logo existe sem a funcao

#exercicio-numero aleatorio

numero={}
lista=[]
from random import randint
for x in range (100):
    num=randint(0,20)
    lista.append(num)
    if numero.get(num)==None:
        numero[num]=1
    else:
        numero[num]=numero[num]+1

for chave,valor in numero.items():
    print(chave,valor)
    print("%d : %d" %(chave,valor))
    print(lista)

#exercicio-lançamento de dado

from random import randint


def dados():
    dado1 = randint(1, 6)
    dado2 = randint(1, 6)
    return dado1 + dado2


num = 0
numero = {}
lista = []
for x in range(1000):
    num = dados()
    lista.append(num)
    if numero.get(num) == None:
        numero[num] = 1
    else:
        numero[num] = numero[num] + 1

for chave, valor in numero.items():
    conta = valor / 10
    print("%d : %.1f %%" % (chave, conta))

#exercicio-sting com carater único

def caracter(palavra):
    letras={}
    contador=0
    for x in palavra:
        if letras.get(x)== None:
            letras[x]=1
            contador=contador+1
    return contador     #quando chamarmos a funcao vai aparecer o contador

print(caracter("zzz"))
print(caracter("Hello, World!"))