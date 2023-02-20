#冒泡排序
a = [12,45,7,453,64,213,56]
for i in range(len(a):
    for j in range(len(a)-1-i):
        if a[j] > a[j+1]:
            temp = a[j]
            a[j] = a[j+1]
            a[j+1] = temp
print(a)