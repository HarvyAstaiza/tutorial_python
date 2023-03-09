#Ejemplo Diccionarios
# Diccionario de aeronaves
aeronaves = {
    "Boeing 747": {
        "capacidad": 660,
        "alcance": 14250,
        "velocidad": 988
    },
    "Airbus A380": {
        "capacidad": 853,
        "alcance": 15200,
        "velocidad": 903
    },
    "Cessna 172": {
        "capacidad": 4,
        "alcance": 837,
        "velocidad": 126
    }
}



# Ejemplo Obtener la capacidad del Boeing 747
capacidad_boeing_747 = aeronaves["Boeing 747"]["capacidad"]
print(capacidad_boeing_747) # Output: 660



# Agregar información sobre un avión nuevo
aeronaves["Bombardier Global 7500"] = {
    "capacidad": 19,
    "alcance": 16100,
    "velocidad": 980
}

# Imprimir la capacidad de todas las aeronaves
for nombre, datos in aeronaves.items():
    print(f"La capacidad del {nombre} es de {datos['capacidad']} pasajeros.")



# Eliminar información sobre el Cessna 172
nombre = input("nombre de aeronave a eliminar:")
def eliminarAeronave(nombre):

   del aeronaves[nombre]
   print("Aeronave Eliminada")

eliminarAeronave(nombre)



# Imprimir la capacidad de todas las aeronaves
for nombre, datos in aeronaves.items():
    print(f"La capacidad del {nombre} es de {datos['capacidad']} pasajeros.")