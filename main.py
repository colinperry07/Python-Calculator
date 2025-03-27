import time
add = lambda x,y: x+y
subtract = lambda x,y: x-y
multiply = lambda x,y: x*y
divide = lambda x,y: x/y

while True:
    global first
    try:
        first = float(input("Enter first number: "))
        break
    except:
        print("Invalid response...")
    time.sleep(.5)

while True:
    global second
    try:
        second = float(input("Enter second number: "))
        break
    except:
        print("Invalid response...")
    time.sleep(.5)


while True:
    global answer
    sign = input("Would you like to add, subtract, multiply, or divide: ")
    
    if sign.lower() == "add":
        answer = add(first, second)
        break
    elif sign.lower() == "subtract":
        answer  = subtract(first, second)
        break
    elif sign.lower() == "multiply":
        answer = multiply(first, second)
        break
    elif sign.lower() == "divide":
        answer = divide(first, second)
        break
    else:
        print("Invalid response...")
    time.sleep(.5)
        
print(answer)
