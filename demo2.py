#选择法排序
a = [12,454,67,3]
for i in range(len(a)-1):
    for j in range(len(a)-1-i):
        if a[i] > a[j+1+i]:
            temp = a[i]
            a[i] = a[j+1+i]
            a[j+1+i] = temp
print(a]