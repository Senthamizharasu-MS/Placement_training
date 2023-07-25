def fun(n,fact):
    if(n<=a):
        fact=fact*n
        fun(n+1,fact)
    else:
        print(fact)

a=4
n=1
fact=1
fun(n,fact)