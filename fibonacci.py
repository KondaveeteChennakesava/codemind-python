def fibo(n):
   if n <= 1:
       return n
   else:
       return(fibo(n-1) + fibo(n-2))
a=int(input())
for i in range(a):
    print(fibo(i),end=' ')