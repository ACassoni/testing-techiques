
def addthis(x,y):
    print(f"x is {x}, type of x is {type(x)}")
    print(f"x is {y}, type of x is {type(y)}")
    
    try:
        result = x + y

    except TypeError:
        print("The wrong type passed")
        result = int(x) + int(y)

    print(f"This is the result: {result}")
    return result

print(addthis("1", 2))