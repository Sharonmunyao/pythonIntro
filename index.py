a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
oper = input("Enter your operation (+,-,*,/):")

if oper == "+" :
    result = a + b
    print (result)
elif oper == "-" :
    result = a - b
    print (result)
elif oper == "*" :
    result = a * b
    print (result)
elif oper == "/" :
    if b != 0:
        result = a / b
        print (result)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation. Please choose one of the following: +, -, *, /")