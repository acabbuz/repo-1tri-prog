def calcular_potencia(base,exponente):
    result = 1

    if exponente>=1:
        for i in range(exponente):
            result*=base
        
    elif exponente==0:
        result = 1
    
    else:
        for i in range(-exponente):
            result*=base
        result = 1/result

    return result

print(calcular_potencia(2,3))
print(calcular_potencia(2,5))
print(calcular_potencia(3,2))
print(calcular_potencia(3,4))
print(calcular_potencia(2,-3))


def calcular_potencia_simple(base,exponente):
    result = 0
    if exponente >0:
        result = base**exponente
    elif exponente ==0:
        result = 1
    else:
        result = 1/(base**(-exponente))

    return result

print(calcular_potencia_simple(2,3))
print(calcular_potencia_simple(2,5))
print(calcular_potencia_simple(3,2))
print(calcular_potencia_simple(3,4))
print(calcular_potencia_simple(2,-3))
print(calcular_potencia_simple(2,-10))
print(calcular_potencia_simple(2,-4))
print(calcular_potencia_simple(2,0))



