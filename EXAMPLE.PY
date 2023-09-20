"""
FECHA:20-09-2023
AUTOR:cristian Jimenez 
OBJETIVO:versionar código Python en Gitgub
"""
result = 0
option1 = int(input("Cuando aprendes algo nuevo, ¿prefieres que te presenten teorías o conceptos antes que ejemplos prácticos?"))
while option1 != 1 and option1 != 2:
    print("respuesta incorrecta")
    option1 = int(input("Digite 1.SI O 2.NO \n"))
if option1 == 1:
    result += 1
option2 = int(input("¿Te sientes más cómodo aprendiendo a través de la lectura de libros o materiales escritos?"))
while option2 != 1 and option2 != 2:
    print("respuesta incorrecta")
    option2 = int(input("Digite 1.SI O 2.NO \n"))
if option2 == 1:
    result+=1
option3= int(input("¿Encuentras útil hacer esquemas, resúmenes o diagramas para organizar la información que estás aprendiendo?"))
while option3 != 1 and option3 !=2:
    print("respuesta incorrecta")
    option3 = int(input("Digite 1.SI O 2.NO \n"))
if option3 == 1:
    result += 1 
option4 = int(input("o	¿Te gusta analizar y reflexionar sobre las ideas y conceptos antes de ponerlos en práctica?"))
while option4 != 1 and option4 !=2:
    print("respuesta incorrecta ")
    option4 = int(input("Digite 1.SI O 2.NO \n"))
if option4 == 1:
    result +=1 
option5 = int(input("o	¿Tienes tendencia a destacar en asignaturas que requieren comprensión de teorías y conceptos, como las matemáticas o la física?"))
while option5 != 1 and option5 != 2:
    print("respuesta incorrecta")
    option5 = int(input("Digite 1.SI O 2.NO \n"))
if option5 == 1 :
    result += 1
option6 = int(input("¿Te sientes más cómodo en entornos de aprendizaje estructurados, como conferencias o clases magistrales?"))
while option6 != 1 and option6 != 2: 
    print("respuesta incorrecta")
    option6 int(input("Digite 1.SI O 2.NO \n"))
if option6 == 1 :
    result += 1
option7 = int(input("¿Prefieres aprender de manera independiente en lugar de trabajar en grupos o equipos?"))
while option7 != 1 and option7 != 2:
    print("respuesta incorrecta")
    option7 int(input("Digite 1.SI O 2.NO \n"))
if option7 == 1 :
    result += 1

if result >= 4:
    print("su estilo de aprendisaje es asilimilador: ")
else:
    print("Su estilo de aprendisaje es otro")



             
