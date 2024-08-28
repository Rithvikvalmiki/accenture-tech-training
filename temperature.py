t = [73,74,75,71,69,72,76,73]
o=[0 for x in range(len(t))]

for i in range(len(t)):
    for j in range(i+1,len(t)):
        if t[j] > t[i]:
          o[i]=j-i
          break
print(o)