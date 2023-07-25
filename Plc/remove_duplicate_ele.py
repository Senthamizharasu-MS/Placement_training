def remove_duplicates(arr):
    return list(set(arr))

if __name__ == '__main__':
    a=input("Enter elements in space seperated: ")
    arr=list(a.split())
    print(remove_duplicates(arr))