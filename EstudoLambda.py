# Autor: Rafael Lua - rafaellua13
 
# Um breve resumo das anotações realizadas no estudo de Lambda, em Python:
 
 
# Lambda
# (lambda x: ação)(variável x passando por parâmetro, 0 caso só precise executar)
 
print("------------- Igualdade")
################## igualdade
 
# var = 1
# print(var+1)
 
(lambda var: var+1)(1) # Lambda var terá mais um somado, porém, é necessário passar o lambda como parâmetro para utilizar novamente esse var
 
(lambda showVar: print(showVar))((lambda var: var+1)(1))
 
 
print("------------- Print")
##################  print
# print("Hey")
(lambda a: print("Hey"))(0)
 
 
 
print("------------- Mais comandos ao mesmo tempo")
##################  Mais comandos ao mesmo tempo
# var = 1
# print(var)
# print(var+1)
(lambda var: [print(var),print(var+1)])(1)
 
print("------------- Mais parâmetros ao mesmo tempo")
##################  Mais comandos ao mesmo tempo
# var = 1
# print(var)
# print(var+1)
(lambda var,test: [print(var,test)])(1,2)
 
 
print("------------- If e Else")
################## if e else
# b = 0
# if b == 0:
#   print("yo")
(lambda b: print("Yo?") if b == 0 else None)(0)
 
# b = 1
# if b == 0:
#   print("yo?")
# else:
#   print("Ya!")
(lambda b: print("Yo?") if b == 0 else print("Ya!"))(1)
 
 
print("------------- Vetor")
##################  vetor
 
# vetor = [1,2,3]
# print(vetor[0])
 
(lambda vetor: print(vetor[0]))([1,2,3])
 
print("------------- Listas")
##################  listas
 
# vetor = [1,2,3]
# vetor.append(4)
# print(vetor)
(lambda vetor: [vetor.append(4),print(vetor)])([1,2,3])
 
 
 
print("------------- For")
##################  for
 
#for c in range(0,10):
#    print(c, end = " ")
(lambda c: [print(c, end = " ") for c in range(0,10) ])(0)
 
print("\n")
## for + if
 
#for d in range(0,10):
#   if d%2==0: #(Se é par)
#    print(d, end = " ")
(lambda d: [print(d, end = " ") if d%2==0 else None for d in range(0,10) ])(0)
 
 
print("\n-------------While")
##################  while
 # while escrito normalmente
# cont = 0
# while cont != 10:
#   print(cont)
#   cont+=1
 
 
 # while escrito na forma apropriada para o lambda
 
# vetor = [[0],0]
# for x in vetor[0]:
#   print(vetor)
#   if vetor[1] == 10:
#     vetor[0].clear()
#   else:
#     print(vetor[1])
#     vetor.append(vetor[1]+1)
#     vetor.remove(vetor[1])
#     vetor[0].append(0)
(lambda vetor: [[vetor[0].clear() if vetor[1] == 10 else [print(vetor[1]),vetor.append(vetor[1]+1),vetor.remove(vetor[1]),vetor[0].append(0)]] for x in vetor[0]])([[0],0])
 
 
 
print("\n-Extras (Funções e outras utilizações com Lambda):\n")
################### extras
print("https://www.w3schools.com/python/python_lambda.asp")
print("\n")
 
 
 
 
