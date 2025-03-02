def superficie_piso(largo, ancho):
    return largo * ancho

def superficie_paredes(largo, ancho, alto):
    return 2 * (largo + ancho) * alto

def perimetro(largo, ancho):
    return 2 * (largo + ancho)

def costo_alfombrado(superficie_piso):
    precio_por_metro = 104
    return superficie_piso * precio_por_metro

def costo_pintura(superficie_paredes):
    litros_necesarios = superficie_paredes/6
    precio_por_litro = 83
    return litros_necesarios * precio_por_litro

largo = int(input("Ingrese el largo del ambiente en metros:"))
ancho = int(input("Ingrese el ancho del ambiente en metros:"))
alto = int(input("Ingrese el alto del ambiente en metros:"))

superficie_del_piso = superficie_piso(largo, ancho)
superficie_de_las_paredes = superficie_paredes(largo, ancho, alto)
perimetro_del_ambiente = perimetro(largo, ancho)
costo_alfombrado_del_ambiente = costo_alfombrado(superficie_del_piso)
costo_pintura_del_ambiente = costo_pintura(superficie_de_las_paredes)

print(f"La superficie del piso es:{superficie_del_piso}m²")
print(f"La superficie de las paredes es:{superficie_de_las_paredes}m²")
print(f"El perímetro del ambiente es:{perimetro_del_ambiente} metros")
print(f"El costo de alfombrar el ambiente es:${costo_alfombrado_del_ambiente:.2f}")
print(f"El costo de pintar el ambiente es:${costo_pintura_del_ambiente:.2f}")