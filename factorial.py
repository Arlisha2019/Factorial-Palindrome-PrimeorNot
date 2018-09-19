user_number = int(input("Enter a number: "))
factorial = 1

def is_factorial(user_number, factorial):
    if(user_number == 0):
        print("The factorial for this number is 1!")
    elif(user_number > 1):
        for i in range(1,user_number + 1):
            factorial = factorial * i
        print("The factorial of {0}, is {1}!".format(user_number,factorial))
    else:
        print("Invaild Entry: Please enter a positive number!")

is_factorial(user_number, factorial)
