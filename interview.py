
""" returns square of a number x
    raises exception if x is not of type int or float """
def square(x):
    if type(x) != int and type(x) != float:
        raise Exception("Invalid input type: type must be int or float")
    print(f"the square is {x**2}")
    return x**2
