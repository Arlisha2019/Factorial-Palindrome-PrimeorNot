user_number = int(input("Enter a number to determine if it's prime or not: "))

def is_prime(user_number):
    for i in range(2, user_number +1):
        for j in range(2, i):
            if(i % j == 0):
                print(True)
                break
    else:
        print(False)

is_prime(user_number)
