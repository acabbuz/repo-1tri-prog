def num_multiplos_entre_si(num1, num2):
    result = ""
    if num1%num2==0:
        result = "El número " + str(num2) + " es multiplo de " + str(num1)
        
    elif num2%num1==0:
        result = "El número " + str(num1) + " es multiplo de " + str(num2)
    else:
        result = "No son multiplos"
        
    return result

print(num_multiplos_entre_si(36,9))
print(num_multiplos_entre_si(15,24))
print(num_multiplos_entre_si(9,36))