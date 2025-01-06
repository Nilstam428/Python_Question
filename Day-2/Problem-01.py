# Q create a function to add two numbers and store result in 'result' variable.
# create a another function which double value of 'result'
# Local variable and globle variable
def add(a,b):
    global result
    result=a+b
    return result

def double(value):
    return value*2

num=int(input("Enter First value:-"))
num1=int(input("Enter second value:-"))
print("Addition :-",add(num,num1))
print("Double value:-",double(result))

