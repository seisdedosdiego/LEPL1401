m=1
while m<=n:
    diviseurs = 0
    for i in range(1, m):
        x = (m//i)
        if (x*i==m):
            diviseurs +=1
    print(m, ":", diviseurs)
    m +=1