max = 0
max_name = None
for i in l:
    count = 0
    for k in l:
        if i==k:
            count += 1
    if count > max:
        max = count
        max_name = i
return max_name 

# ZONE TEST #
print(plus_frequent([1,2,3,1,2,2]))
print(plus_frequent([1,1,3,1,2,2]))
print(plus_frequent(["a","b", "b", "b"]))
