# def store_amount(type, amount):
#     result =""
#     if type ==("student") and amount >=100:
#         result = "15% discount"
        
#     elif type ==("student") and amount <100:
#         result = "10% discount"

#     elif type ==("regular") and amount >=200:
#         result = "12% discount"
    
#     else:
#         result = "5% discount"
    
#     return result

# print(store_amount("student", 1000))
# print(store_amount("student", 90))
# print(store_amount("regular", 210))
# print(store_amount("regular", 10))

def store_amount(type, amount):
    result  ="5%"
    if type == "student":
        if amount >=100:
            result  = "15%"
        else:
            result = "10%"
    elif type == "regular" and amount>=200:
        result = "12%"

    return result 

print(store_amount("student", 1000))
print(store_amount("student", 90))
print(store_amount("regular", 210))
print(store_amount("regular", 10))