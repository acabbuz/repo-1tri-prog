def calcular_forma_triangulo(lado1, lado2, lado3):
    result = ""

    if lado1>=1 and lado2>=1 and lado3>=1:
        
        if lado1 == lado2 ==lado3:
            result = "Triángulo Equilatero"
        elif lado1 == lado2 or lado1 ==lado3 or lado2 ==lado3:
            result = "Triángulo Isosceles"
        elif lado1!=lado2 !=lado3:
            result = "Triangulo Escaleno"
        
    else:
        result = "Algún lado invalido"
    
    return result


print(calcular_forma_triangulo(2,2,4))
print(calcular_forma_triangulo(1,2,4))
print(calcular_forma_triangulo(2,2,2))