# numb1= int(input("Ingrese un numero (0 para finalizar): "))
# add= []

# while numb1 !=0:
#     numbX= numb1
#     add.append(numbX)

# average= sum(add)

# print(sum)

################  corección ############

add = []
numb1 = int(input("Ingrese un número (0 para finalizar): "))

while numb1 != 0:
    add.append(numb1)
    numb1 = int(input("Ingrese un número (0 para finalizar): "))

average = sum(add)

print(f"El promedio es {average}")
