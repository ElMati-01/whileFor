numb1= int(input("Ingrese el numero de temperaturas que quiere medir: "))

temp1=[]
counter= 0

while numb1 > counter:
    tempX= int(input("Ingrese la temperatura: "))
    temp1.append(tempX)
    counter+=1

tempMax= max(temp1)
tempMin= min(temp1)
tempAver= sum(temp1) / numb1

print(f"La temperatura maxima es: {tempMax}°, la minima es: {tempMin}° y wl promedio es: {tempAver}")