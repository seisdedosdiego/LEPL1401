n=1
sum=0
while n<=10:
    sum=sum+(n*n)
    print(n,"\t", n*n,"\t", sum,"\t",n*(n+1)*(2*n+1)//6)
    n+=1

    