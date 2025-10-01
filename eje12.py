def concatenacion_operacion_simple(caracter,num1,num2):
    result = ""
    if caracter=="+" :
        result = str(num1+num2)
    elif caracter=="-" :
        result = str(num1-num2)
    elif caracter=="/" :
        if num2 ==0:
            result = "No se puede dividir por 0"
        else:
            result = str(num1/num2)
    elif caracter=="*" :
        result = str(num1*num2)
    else:
        result = str(num1) + caracter + str(num2)

    return result

print(concatenacion_operacion_simple("*", 2,2))
print(concatenacion_operacion_simple("w", 2,2))
print(concatenacion_operacion_simple("/", 0,15))
print(concatenacion_operacion_simple("/", 15,0))