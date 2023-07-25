def swap(a,b):

    return b,a

if __name__ == "__main__":
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))
    print("Before swapping: ",a,b)
    a,b=swap(a,b)
    print("After swapping: ",a,b)