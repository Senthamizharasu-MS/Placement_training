def checkNoUniqe(list):
    for i in range(len(list)):
        for j in range(i+1, len(list)):
            if list[i] == list[j]:
                return True
    return False


sequence = input("Enter the number of sequence seperated by space : ")

list = sequence.split()

if checkNoUniqe(list):
    print("The sequence has no unique elements")
else:
    print("The sequence has unique elements")
