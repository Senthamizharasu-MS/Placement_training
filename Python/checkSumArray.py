
arr = []
a=int(input("Enter the number : "))
n=input("Enter the number of sequence seperated by space : ")
arr = n.split()

def checkSuminArray(arr,a):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if int(arr[i]) + int(arr[j]) == a:
                print("(" + arr[i] + "," + arr[j] + ")")

print(checkSuminArray(arr,a))