# Entradas
base = float(input("Ingrese Base:"))
altura = float(input("Ingrese Altura:"))


# Proceso
def calcularAreaTriangulo(b, al):
    area = (b * al) / 2
    return area


# salida
resultado = calcularAreaTriangulo(base, altura)

print("El Area del Triangulo es:", resultado)

#funcion con argumentos por defecto
def mostrarPais(pais= "Colombia"):
    print( "yo soy de :"+pais)

mostrarPais("Suiza")
mostrarPais("Ecuador")
mostrarPais()
mostrarPais("Brazil")