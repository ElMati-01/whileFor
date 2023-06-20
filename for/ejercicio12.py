numb1 = int(input("Ingrese cantidad de estudiantes: "))
notes = []


for e in range(numb1):
    students = []
    
for i in range(4):
    noteX = float(input("Ingrese sus notas aquí: "))
    notes.append(noteX)

noteHigh = max(notes)  
noteLow = min(notes)  
average = sum(notes) / 4

print(f"La nota más alta es: {noteHigh}, la más baja es: {noteLow} y el promedio es: {average}.")



