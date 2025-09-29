def comparar_numeros(num1, num2):
    result = ""
    if num1 == num2:
        result = "Iguales"
    elif num1<num2:
        result = str(num2) + " más grande que " + str(num1)
    else:
        result = str(num1) + " más grande que " + str(num2)
    return result

print(comparar_numeros(2,2))
print(comparar_numeros(1,2))
print(comparar_numeros(3,2))