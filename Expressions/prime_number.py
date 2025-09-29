
number = int(input("enter the number to check :"))

def primeNumber():
    if number == 1 or number == 0:
        print("Non prime")

    for i in range(2, number):
        if number%i == 0: