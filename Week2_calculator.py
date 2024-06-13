def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
def floor_div(a,b):
    return a//b
def expo(a,b):
    return a**b

print("---------------Welcome To Calculator---------------")
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

print("Please choose an option from below\n1. Add\n2.Subtract\n3. Multiply\n4. Divide\n5. Floor Divide\n6. Exponentiation")
c=int(input("Your option: "))

res = 0
x=""
if(c==1):
    x="+"
    res=add(a,b)
elif(c==2):
    x="-"
    res=subtract(a,b)
elif(c==3):
    x="*"
    res=multiply(a,b)
elif(c==4):
    x="/"
    res=divide(a,b)
elif(c==5):
    x="floor divided by"
    res=floor_div(a,b)
elif(c==6):
    x="raise to power"
    res=expo(a,b)
else:
    print("Error! Please choose a valid option.")

if(x!=""):
    print(a,x,b,"=",res)
