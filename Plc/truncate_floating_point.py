def truncate(a):
    b=int(a-(a%1))
    return b

if __name__ == "__main__":
    a=float(input("Enter a number: "))
    print(truncate(a))