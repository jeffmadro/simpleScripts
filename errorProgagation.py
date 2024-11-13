import math as m

def findError(type, x, dx, y, dy):
    match type:
        case "m":
            output = m.abs(x*y) * m.sqrt((dx/x)**2 + (dy/y)**2)
            o = ("mult", x*y)
        case "d":
            output = m.abs(x*y) * m.sqrt((dx/x)**2 + (dy/y)**2)
            o = ("div", x/y)
        case "a":
            output = m.sqrt(dx**2 + dy**2)
            o = ("add", x+y)
        
    return o, output


def main():

    type = input("m for multiplication a for addition or d for division: ")
    x =  float(input("what is the first value: "))
    dx = float(input("what is the associated error: "))
    y =  float(input("what is the second value: "))
    dy = float(input("what is the second associated error: "))
    output = float
    o = tuple
    o, output = findError(type, x, dx, y, dy)

    print(f"the error propogation for {o} is {output}")

    # loop to get the values for repeated opperations
    y =  float(input("what is the second value: "))
    dy = float(input("what is the second associated error: "))
    o, output = findError(type, x, dx, y, dy)

    
    print(f"the error propogation for {o} is {output}")


main()