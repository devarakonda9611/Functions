# def <function_name>(args):
    # operation 
# print(<function_name>(args))


# def add(x,y):
    # return x + y 
# print(add(10,20))

# Types of functions:
# .....................
# Required or positional arguments
# default arguments
# keyword arguments
# variable length arguments
# keyword variable length arguments

# Required or positional arguments :
# ................................


# def add(x,y):
     # return x + y
     
# print(add(10,20))
# print(add(30,20))
# print(add(50,20))

# default : 
# ............

# def ravee(x,y,z=50):
    # return x + y + z
# print(ravee(50,70))

#keyword:
# ................
# def ravee(x,y,z):
    # return x + y + z
# print(ravee(z=33,y=66,x=50))

# Variable length : 
# .................
# def ravee(*args):
    # return args
# print(ravee(1,2,3,4,5,6))

# keyword Variable length(**kwargs) : 

def ravee(**kwargs):
    return kwargs
print(ravee(name = "santosh",age = 28))
