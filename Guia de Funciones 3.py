def calcular_triple(numero):
    return numero * 3
    
def calcular_siguiente(numero):
    return numero + 1
    
numero = int(input("Ingrese un numero:"))

consecutivo_del_triple = calcular_siguiente(calcular_triple(numero))

triple_del_consecutivo = calcular_triple(calcular_siguiente(numero))

print(f"El consecutivo del triple del numero es: {consecutivo_del_triple}")

print(f"El triple del consecutivo del numero es: {triple_del_consecutivo}")