#Estructura selectiva simple

numero = int(input("Introduce un número: "))
def par_Impar(num):
    if num % 2 == 0:
        mensaje = print("El número es par.")
    else:
        mensaje = print("El número es impar.")
    return  mensaje

par_Impar(numero)

# Ejemplo de estructura selectiva doble en Python

edad = int(input("¿Cuál es tu edad? "))
def conducir(age):
    if edad >= 18:
        print("Puedes conducir.")
    else:
        print("No puedes conducir.")

    if edad < 18:
        print("Eres menor de edad.")

conducir(edad)

# Ejemplo de estructura selectiva múltiple en Python

calificacion =  float(input("¿que nota obtuvo  en la materia? "))
def calificaciones(nota):
    if calificacion >= 9:
        print("¡Felicidades! Tu calificación es sobresaliente.")
    elif calificacion >= 7:
        print("Tu calificación es buena, pero podrías mejorar.")
    elif calificacion >= 5:
        print("Tu calificación es suficiente, pero necesitas esforzarte más.")
    else:
        print("Lo siento, tu calificación es insuficiente. Debes estudiar más.")

calificaciones(calificacion)

#EJEMPLO SI ANIDADO
x = 30
y = 25
z = 13

def anidado(a,b,c):
    if x > y:
        print("x es mayor que y")
        if x > z:
            print("x también es mayor que z ")
        else:
            print("z es mayor que x")
    else:
        print("y es mayor que x")
anidado(x,y,z)