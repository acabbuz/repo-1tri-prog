def calcular_costos(num_alum):
    result = 0

    if num_alum>=100:
        result = num_alum*65
    elif 50<=num_alum<=99:
        result= num_alum*70
    elif 30<=num_alum<=49:
        result= num_alum*95
    elif num_alum<30:
        result = 2500

    return f"El precio del autobus será de {result} para los {num_alum} alumnos"

print(calcular_costos(100))
print(calcular_costos(101))
print(calcular_costos(55))
print(calcular_costos(99))
print(calcular_costos(46))
print(calcular_costos(2))