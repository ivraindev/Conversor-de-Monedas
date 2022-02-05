def conversor (tipo_pesos, valor_dolar):
    pesos  = input ("cuantos pesos " + tipo_pesos + " tienes?: ")
    pesos = float (pesos)
    dolares = pesos/valor_dolar
    dolares = round (dolares, 2)
    dolares = str (dolares)
    print("tienes $" + dolares + " dolares")

menu = """
Bienvenida al conversor de monedas ❤

1. Peso Mexicano
2. Peso colombiano
3. Peso Argentino

elige una opcion: """

opcion = int (input (menu))

if opcion == 1:
    conversor ("mexicanos", 20.68)
elif opcion ==2:
    conversor ("colombianos", 3875)
elif opcion == 3:
    conversor ("argentinos", 65)
else:
    print ("Solo hay 3 opciones, escoge una de esas")
