#Tuplas
pelicula_1 = ("El Padrino", 1972, 175, ["Drama", "Crimen"])
pelicula_2 = ("Forrest Gump", 1994, 142, ["Drama", "Comedia"])
pelicula_3 = ("Titanic", 1997, 194, ["Romance", "Drama"])

def mostrar_pelicula(pelicula):
    print("Título:", pelicula[0])
    print("Año de estreno:", pelicula[1])
    print("Duración:", pelicula[2], "minutos")
    print("Géneros:", ", ".join(pelicula[3]))

mostrar_pelicula(pelicula_1)
mostrar_pelicula(pelicula_2)
mostrar_pelicula(pelicula_3)

#tuplas anidadas

satellite1 = ('ISS', 'orbita baja', 200)
satellite2 = ('Directv', 'orbita geoestacionaria', 1000)
satellite3 = ('Hispasat', 'orbita polar', 500)

satellites = (satellite1, satellite2, satellite3)
def recorrerSatelites(satelites):
    for satellite in satellites:
        nombre, orbita, altitud = satellite
        print(f"{nombre} esta en una {orbita} a una altitud de {altitud} km.")

recorrerSatelites(satellites)