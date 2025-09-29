"""
def media(num1, num2, num3, num4):
    
    numeros = [num1, num2, num3, num4]
    
    suma = num1+ num2 + num3 + num4
    promedio = suma/len(numeros)
    num_superior = []

    for num in numeros:
        if num>promedio:
            num_superior = num
    
    return "El promedio es " + str(promedio) + " y el mayor a la media es " + str(num_superior)

#print(media(5,4,9,6))

"""

def media():
    result  =""
    suma = 0

    cantidad = int(input("Cuantos introduciras: "))
    numeros = [0] * cantidad

    for i in range(cantidad):
        num = int(input("Introduzca número : "))
        numeros[i] = num
        suma +=num

    promedio = suma/len(numeros)

    for num in numeros:
        if num> promedio:
            result += str(num)+ " "
        else:
            result = "ninguno"

    return f"El promedio es {promedio} y los números mayores son {result}"

print(media())

