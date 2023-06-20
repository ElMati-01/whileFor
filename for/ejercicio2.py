numb1= int(input("Digite un numero: "))


if numb1 > 10:
    numbX = 1
    for i in range(1, 11):
        numbX*= i

else:
    numbX=0
    for i in range (1,numb1 + 1):
        numbX+= i

print(numbX)

