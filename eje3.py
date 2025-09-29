def multiplos(num):
    result = ""
    
    if num%5==0:
        result += " El numero " + str(num) + " es múltiplo de 5"
    if num%7==0:
        result += " El numero " + str(num) + " es múltiplo de 7"
    return result


print(multiplos(5))
print(multiplos(7))
print(multiplos(35))
print(multiplos(1))