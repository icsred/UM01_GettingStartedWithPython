nombre= str (input ("Por favor, ingresá tu nombre:"))
edad= int (input ("Ahora ingresá tu edad:"))
meses= edad*12
print (nombre, ", tu edad en meses serían aproximadamente:", meses)
if edad % 2 == 0:
    print ("Tu edad en años, es un número par")
    if edad % 10 == 2:
        print ("Hoy es un buen día para tomarse un gin tonic")
    else:
        print ("Escuchate el tema Lucky Man de The Verve, te va a gustar.")
else: 
    print ("Tu edad en años es un número impar")
    if edad % 10 == 5:
        print ("Mirate la peli ¨la mujer en la ventana¨")
    else:
        print ("Mirate la serie El inocente, está muy buena.")    





