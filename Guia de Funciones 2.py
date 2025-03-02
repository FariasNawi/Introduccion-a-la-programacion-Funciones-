def calcular_potencia():
    
    base = int(input("Ingrese el numero base:"))
    
    exponente = int(input("Ingrese el exponente:"))
    
    resultado = base ** exponente
    
    return resultado

resultado = calcular_potencia

print(f"El resultado de la potencia es: {resultado}")