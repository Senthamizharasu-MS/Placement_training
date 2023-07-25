def fun(n,sum):
    if(n<=a):
        sum=sum+n
        fun(n+1,sum)
    else:
        print(sum)

a=int(input("Enter a number: "))
sum=0
n=1
fun(n,sum)