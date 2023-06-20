numb1= int(input("Ingrese cantidad de notas: "))
notes= []

for i in range(numb1):
    noteX= float(input("Ingrese sus notas aquí: "))
    notes.append(noteX)

average= sum(notes) / numb1

print(f"Su promedio de notas es: {average}")