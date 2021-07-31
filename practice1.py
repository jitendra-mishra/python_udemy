def aByb(a, b):
    try:
        if a == b:
            raise NameError("Hi There")
        c = (a+b)/(a-b)
    except(ZeroDivisionError):
        print("DivideByZero error: Value of a and b are equal")
    else:
        print(c)
    finally:
        print("I am finally")

a = 10.0
b = 10.0
aByb(a, b)