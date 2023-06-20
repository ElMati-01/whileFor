numb1= int(input("Ingrese el numero de temperaturas que quiere medir: "))

temp1=[]

for i in range(0, numb1):
    tempX= int(input("Ingrese la temperatura: "))
    temp1.append(tempX)

tempMax= max(temp1)
tempMin= min(temp1)
tempAver= sum(temp1) / numb1

print(f"La temperatura maxima es: {tempMax}°, la minima es: {tempMin}° y wl promedio es: {tempAver}")
