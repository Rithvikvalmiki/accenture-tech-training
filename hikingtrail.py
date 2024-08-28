hik = [1,2,3,4,3,2,1]
max = 0
for i in range(1,len(hik)):
    if hik[i]>hik[i+1]:
        max = hik[i]
        break
    
print(max)