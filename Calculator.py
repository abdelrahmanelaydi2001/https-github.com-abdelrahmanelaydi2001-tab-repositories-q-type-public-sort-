def calculator():
    while True:
        op=input("Operator (+,-,*,/) or 'q' to quit: ")
        if op=="q":
            print("Goodbye")
            break
        if op not in ("+","-","*","/"):
            print("Invalid operator")
            continue
        try:
            a=float(input("Enter first number: "))
            b=float(input("Enter second number: "))
        except ValueError:
            print("Please enter valid numbers")
            continue
        if op=="+":
            print("result =",a+b)
        elif op=="-":
            print("result =",a-b)
        elif op=="*":
            print("result =",a*b)
        elif op=="/":
            if b==0:
                print("Error: cannot divide by zero.")
            else:
                print("result =",a/b)
calculator()