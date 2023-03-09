#EJEMPLO FOR

carros = ["mustang","camaro","porche"]

for i in carros:
    print(i)

#EJEMPLO WHILE

i = 0
while i < len(carros) and carros[i] != "camaro":
    print(carros[i])
    i += 1

print(" el Camaro esta estacionado en la puesto", i+1)

