#Creating a calculator with Python for my 302 homework (learning how to do it)

def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

print("Please select operation -/n"
      "1. Add \n"
      "2. Subtract \n"
      "3. Multiply \n"
      "4. Divide \n"

sel = int(input("Select operation (1-4): "))

n1 = int(input("Please enter the first number: "))

n2 = int(input("Please enter your second number: "))

if sel == 1:
      print(n1, "+", n2, "=", add(n1,n2))
elif sel == 2:
    print(n1, "-", n2, "=", sub(n1,n2))
elif sel == 3:
    print(n1, "*", n2, "=", mul(n1,n2))
elif sel == 4:
    print(n1, "/", n2, "=", div(n1,n2))
else:
    print("Invalid input")
