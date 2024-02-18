def dodavannya(a, b):
    return a + b

def vidnimannya(a, b):
    return a - b

def mnozhennya(a, b):
    return a * b

def dilyennya(a, b):
    if b == 0:
        return "Error! Cant dilutu na 0!"
    else:
        return a / b

def stepin(a, b):
    return a ** b

print("Chose your operation: 1.+,  2.-,  3./,  4.*,  5.**")

ch = input("Enter number:")

num1 = float(input("\nFirst num: "))
num2 = float(input("Second num: "))

match ch:
    case '1':
        Result = dodavannya(num1, num2)
    case '2':
        Result = vidnimannya(num1, num2)
    case '3':
        Result = mnozhennya(num1, num2)
    case '4':
        Result = dilyennya(num1, num2)
    case '5':
        Result = stepin(num1, num2)
    case _:
        "Wrong Choice!"

print("\nResult:", Result)
