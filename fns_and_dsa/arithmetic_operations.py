def perform_operation (num1, num2, operation):
    if operation == "add":
        result = num1 + num2
    elif operation == "subtract":
        result = num1 - num2
    elif operation == "multiply":
        result = num1 * num2
    elif operation == "divide":
        if num2 == 0:
            result = "you can not divide a number by 0. try again"
        else:
            result = num1 / num2
    else:
        print("wrong input please try again")
    return result



test = perform_operation(5,0,'divide')
print (test)