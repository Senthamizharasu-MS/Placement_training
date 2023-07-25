def multiply(x,y):
    c=0
    for i in range(y):
        c+=x
    return c

if __name__ == "__main__":
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))
    c=multiply(a,b)
    print("Product of two numbers is: ",c)