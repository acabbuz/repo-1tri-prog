def calcular_distancia(num1, num2):
    result = 0

    if num1>num2:
        mayor = num1
        menor = num2
    elif num1<num2:
        mayor = num2
        menor = num1
        
    for i in range(menor, mayor):
        result+=1

    return result

print(calcular_distancia(4, 5))
print(calcular_distancia(-2, 5))
print(calcular_distancia(0, 10))
print(calcular_distancia(5, 10))