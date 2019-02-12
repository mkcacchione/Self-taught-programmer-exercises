#question 1 page 66
def f():
    x=5
    print (x**2)
f()

#question 2 page 66
def about_you():
    a= input ("what is your name:")
    b= input ("how old are you:")
    c= input ("where are you from:")

about_you()

#question 3 page 66
def f(x,y,z,l=5,m=2,n=3):
    return x+y+z+l+m+n
result = f(1,2,0)
print (result)
second = f(1,2,0,1,1,1)
print(second)

#question 4 page 66
def f(x):
    return x*2
result = f(4)
print (result)

def z(y):
    return y*4
second_result= z(result)
print(second_result)

#question 5 page 66
def f():
    try:
        f=input ("how old are you:")
        j=input ("what year are you in school:")
        f=float(f)
        j=float(j)
        return (f/j)
    except ValueError:
        print ("invalid answer")
result = f()
print(result)

#question 6 page 66
def f():
    """
    returns x squared
    :param x:int
    """
    x=5
    print (x**2)
f()

def about_you():
    """
    asks user to input information about themselves.
    No specific paramaters
    """
    a= input ("what is your name:")
    b= input ("how old are you:")
    c= input ("where are you from:")

about_you()

def f(x,y,z,l=5,m=2,n=3):
    """
    returns sum of variables
    :param x:int
    :param y:int
    :param z:int
    :param l:int
    :param m:int
    :param n:int
    """
    return x+y+z+l+m+n
result = f(1,2,0)
print (result)
second = f(1,2,0,1,1,1)
print(second)

def f(x):
    """
    returns x multiplied by 2
    :param x:int
    """
    return x*2
result = f(4)
print (result)

def z(y):
    """
    returns y multiplied by 4
    :param y:int
    """
    return y*4
second_result= z(result)
print(second_result)

def f():
    """
    returns age f divided by j
    :param f:int or float
    :param j:int or float
    """
    try:
        f=input ("how old are you:")
        j=input ("what year are you in school:")
        f=float(f)
        j=float(j)
        return (f/j)
    except ValueError:
        print ("invalid answer")
result = f()
print(result)
