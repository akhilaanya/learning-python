# Jan 19: Learning functions (for my 302 homework...)

#function = block of reusable code
    # place () after the function name to invoke it
#Write code once and reuse it whenever necessary

def happy_birthday():
    print("Happy birthday to the happy_birthday function!")
    print("You are old!")
    print("Happy birthday to the happy_birthday function!")
    print()

happy_birthday()

#to execute it another two times
happy_birthday()
happy_birthday()

#Arguments: send data (values or variables) directly to a function
def birthday(name, age):
    print(f"Happy birthday to {name}!")
    #(f" "): f-string to directly embed variables inside strings
    print(f"You are {age} years old!")
    print("Happy birthday to you!")
    print()

#Parameter: temporary variable within a function

birthday("Bro", 20)
birthday("Steve", 20)
birthday("Joe", 20)
#don't write 'name = "Bro"' b/c ur calling the fn w/ the 2 parameters (name, age)
#Order of parameters matters!

def display_invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"Your bill of ${amount: .2f} is due: {due_date}")
        #amount: .2f is a format specifier: define presentation of a value
        #refer to format_specifiers.py for more info
    
display_invoice("Akhila", 10.35, "01/01/2027")

#Return: statement used to end a fn and send a result back to the caller

def add(x, y):
    z = x + y
    return z

def sub(x,y):
    z = x - y
    return z

def multiply(x,y):
    z = x * y 
    return z
#You can't do 'z = xy' to multiply

def divide(x,y):
    z = x / y
    return z

print(add(1,2))
print(sub(1,2))
print(multiply(1,2))
print(divide(1,2))

#you get 'None' if you don't specify what to return

def create_name(first, last):
    first = first.capitalize()
    #.capitalize() is a method; see methods.py for more info
    last = last.capitalize()
    return first + " " + last

full_name = create_name("akhila", "anya")


print(full_name)
