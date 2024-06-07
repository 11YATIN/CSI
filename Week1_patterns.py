def lower_triang(n):
    for i in range(1,n+1):
        for j in range(i):
            print("*",end="") 
        print()     

def upper_triang(n):
    for i in range(n,-1,-1):
        for j in range(i):
            print("*",end="") 
        print()     

def pyramid(n):
    for i in range(1,n+1):
        for j in range(n-i):
            print(end=" ")
        for j in range(i):
            print("*",end=" ") 
        print()     
print("-----------Welcome To Patterns By Yatin Sansanwal-----------")
print()
n = int(input("Enter the value of n: "))
print()
print("-----------Lower Triangualar Pattern-----------")
lower_triang(n)
print()
print("-----------Upper Triangualar Pattern-----------")
upper_triang(n)
print()
print("-----------Pyramid Pattern-----------")
pyramid(n)
