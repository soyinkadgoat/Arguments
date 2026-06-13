num = int(input("Enter your number: "))

def FindCube(number):
    return number * number * number

def Cube(number):
    if number % 3 == 0:
        print("The Cube of", str(num), "is", str(FindCube(number)))
    else:
        print(str(number), "is not divisible by 3")
    
Cube(num)