def mitad_de_pares(lista):
    for numero in lista:
        if numero % 2 == 0:
            print(f"La mitad de {numero} es: {numero/2}")

n = int(input("Cuantos numeros va a ingresar¿?"))

numeros = []

for i in range(n):
    numero = int(input(f"Ingresa el numero {i+1}:"))
    numeros.append(numero)

mitad_de_pares(numeros)