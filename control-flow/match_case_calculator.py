num1 = int(input ("Enter the first number: "))
num2 = int(input ("Enter the second number: "))
operation = input ("Choose the operation (+, -, *, /): ")

match operation:
    case "+":
        print(num1 + num2)
    case "-":
        print(num1 - num2)
    case "*":
        print(num1 * num2)
    case "/":
        if num2 == 0:
            print ("Cannot divide by zero.")
        else:
            print(num1 / num2)
        