print("Tarea 2\n")

numeros=[4,7,12,15,18,21,24,30,33,40]
for i in numeros:
    print(i)

suma=0
pares=0
impares=0
lista_pares=[]
lista_impares=[]
mayores_20=[]

for i in numeros:
    suma+=i
    if i%2==0:
        pares+=1
        #Agrego de forma extra la lista
        lista_pares+=[i]
    else:
        impares+=1
        #Agrego de forma extra la lista
        lista_impares+=[i]
    if i>20:
        mayores_20+= [i]
        
print("La suma de todos los elementos es: ", suma, "\n")
print("El número de pares es: ",pares, "y los elementos son: ",lista_pares,"\n")
print("El número de impares es: ",impares, "y los elementos son: ",lista_impares,"\n")
print("Lista de numeros mayores a 20: ",mayores_20)
