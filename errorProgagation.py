import math as m

def findError(type, x, dx, y, dy):
    match type:
        case "m":
            output = abs(x*y) * m.sqrt((dx/x)**2 + (dy/y)**2)
            o = ("mult", x*y)
        case "d":
            output = abs(x/y) * m.sqrt((dx/x)**2 + (dy/y)**2)
            o = ("div", x/y)
        case "a":
            output = m.sqrt(dx**2 + dy**2)
            o = ("add", x+y)
        case "s":
            output = m.sqrt(dx**2 + dy**2)
            o = ("sub", x-y)
        
    return o, output


def main():
    num = int(input("how many numbers are we dealing with: "))
    type = input("m for multiplication a for addition or d for division or s for subtraction: ")
    assert type in ("m", "a", "d", "s")
    x =  float(input("what is the first value: "))
    dx = float(input("what is the associated error: "))
    y =  float(input("what is the second value: "))
    dy = float(input("what is the second associated error: "))
    output = float
    o = tuple
    o, output = findError(type, x, dx, y, dy)

    print(f"the error propogation for {o} is {output}")

    # loop to get the values for repeated opperations
    for _ in range(num-2):
        y =  float(input("what is the third value: "))
        dy = float(input("what is the third associated error: "))
        o, output = findError(type, o[1], output, y, dy)

        
        print(f"the error propogation for {o[1]} is {output}")


main()