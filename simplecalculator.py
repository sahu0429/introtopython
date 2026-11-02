a = float(input("First number: ")) 
op = input("Operator (+ - * /): ")  
b = float(input("Second number: ")) 
if op == "+":
    result = a + b  
elif op == "-":
    result = a - b      
elif op == "*":
    result = a * b      
elif op == "/":
    if b == 0:
        print("Error: division by zero")
    else:
        print(a / b)    
else:
    print("Unknown operator:", op)