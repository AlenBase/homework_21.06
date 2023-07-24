while True:
    try:
        number1=int(input('Write First Number:\n'))
        operator=input('Write Operator(+,-,/,*)\n')
        number2=int(input('Write Second Number:\n'))
        if operator == "+":
            result = number1 + number2
        if operator == "-":
            result = number1 - number2
        if operator == "*":
            result = number1 * number2
        if operator == "/":
            result = number1 / number2
        print(result)
        choise = input('You want to quit?(y/n)')
        if choise == 'y':
            break
    
    except ValueError:
        print('Write only int type numbers')
        choise = input('You want to quit?(y/n)')
        if choise == 'y':
            break
        
    except ZeroDivisionError:
        print("Can't divide by zero")
        choise = input('You want to quit?(y/n)')
        if choise == 'y':
            break