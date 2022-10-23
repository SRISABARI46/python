print(" $$$    welcome to calculator    $$$")
print()

def calculate():
    num1 = input("ENTER THE FIRST NUMBER:")
    num2 = input("ENTER THE SECOND NUMBER:")
    print("SELECT OPERATION")
    print("ADDITION- 1")
    print("SUBTRACTION- 2")
    print("MULTIPLICATION- 3")
    print("DIVISION- 4")

    operation = input("CHOICE ")

    if operation == '1':
        print("THE SUM IS %.1f " % (float(num1) + float(num2)))

    elif operation == '2':
        print("THE SUBTRACT IS %.1f " % (float(num1) - float(num2)))

    elif operation == '3':
        print("THE PRODUCT IS %.1f " % (float(num1) * float(num2)))

    elif operation == '4':
        print("THE QUOTIENT IS %.1f " % (float(num1) / float(num2)))
    else:
        print(" ERROR")

    again()


def again():
    next_calculation = input("WANT TO CONTINUE ? (YES OR NO)")
    if  (next_calculation == "yes") or (next_calculation == "YES") or (next_calculation == "Yes"):
        calculate()

    elif (next_calculation == "no") or (next_calculation == "NO") or (next_calculation == "No"):
        print("Thank you....")
    else:
        again()


calculate()










