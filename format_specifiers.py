#Jan 19, 2026
#Learning format specifiers in Python!

#Format specifiers: format a value based on what flags are inserted {value:flags}

#.(number)f = round to that many decimal places (fixed point)

price1 = 3.14159
price2 = -987.65
price3 = 12.3400

print(f"Price 1 is ${price1:.2f}") #2 decimal points as a floating point number
print(f"Price 2 is ${price2: 10}") #10 spaces before the output
print(f"Price 3 is ${price3: .3f}") #adds a trailing zero

print(f"Price 3 is ${price3:00010}")

#https://www.youtube.com/watch?v=FrvBwdAU2dQ
