def concatenacion_operacion_simple(caracter,num1,num2):
    result = ""
    if caracter=="+" :
        result = str(num1+num2)
    elif caracter=="-" :
        result = str(num1-num2)
    elif caracter=="/" :
        result = str(num1/num2)
    elif caracter=="*" :
        result = str(num1*num2)
    else:
        result = str(num1) + caracter + str(num2)

    return result

print(concatenacion_operacion_simple("*", 2,2))
print(concatenacion_operacion_simple("w", 2,2))