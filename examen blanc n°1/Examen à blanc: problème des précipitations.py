total = 0
total_n = 0
for i in l:
    if 0<i<9999:
        total += i
        total_n += 1
    if 0>i:
        total_n += 1
    if i==9999:
        if total_n == 0:
            return "pas de moyenne"
        else:
            moy = total/total_n
            return moy

# ZONE TEST #
print(rainfall([100,50,50,250,200,9999])) 
print(rainfall([9999,50,50,250,200,100])) 
print(rainfall([-999,-99,-99,9999,200,100])) 
print(rainfall([1,2,3,4,5,-1,9999])) 