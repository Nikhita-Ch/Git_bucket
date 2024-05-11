def calculator( a, b, c):
    if c=='+' :
        return a+b
    elif c=='-' :
        return a-b
    elif c== '*':
        return a*b
    elif c=='/':
        return a/b
    else:
        print("Invalid operation")

a= int(input("enter operand 1: "))
b= int(input("enter operand 2: "))
c= input("enter operator: ")
print("result of op: ", +calculator(a, b, c))
