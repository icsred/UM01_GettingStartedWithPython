"""Ejercicio 1
Crear un programa que le pregunte al usuario su nombre y su edad en años.
El programa debe mostrarle al usuario el nombre e indicarle cuántos meses tiene.
Extras:
1. El programa debe indicarle al usuario si su edad es un número par o impar
2. Si su edad en años es par, sugiérele una canción
3. Si su edad en años es impar, sugiérele una serie
4. Pero si su edad termina en 5, sugiérele una película
5. Pero si su edad termina en 2, sugiérele un coctél
"""

def Nombre():
    print ("Cual es tu nombre?")
    "nombre = fer"
    while True:
        try:
            nombre = str(input("Por favor ingrese su primer nombre: "))
            if nombre.isdigit():
                raise TypeError
            elif (len(nombre) < 2):
                raise EOFError
            break
        except TypeError:
            print("Solo letras :)")
            continue
        except EOFError:
            print("Ingresa algo :/....")
            continue
    return (nombre)

def Edad():
    print ("Cual es tu edad?")
    "edad = 39"
    while True:
        try:
            edad = int(input("Por favor ingresa un numero: "))
            break
        except ValueError:
            print("Oops!  Eso no es numero :/...  Intenta de nuevo...")
            continue
    return (edad)


if __name__ == '__main__':
    nombre = Nombre()
    edad = Edad()

    print("Tu nombre es {} y tu edad es de {} meses\n" .format(nombre, edad*12))

    if edad%2 == 0:
        print ("Sabias que tu edad es Par!\n")
        print ("Escuchaste alguna vez la canción Outlaws & Outsiders? Deberias...\n")
    else:
        print ("Sabias que tu edad es Impar!\n")
        print ("Mira la serie Merli es buenisima!\n")


    if edad%5 == 0:
        print ("Asi que tenes {}. Te viste la ultima peli de Marvel?\n".format(edad))
    elif edad%2 == 0:
        print ("Asi que tenes {}. Queres tomar un coctel?\n".format(edad))
