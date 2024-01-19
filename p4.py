#logic with fibonoci series
i = int(input("Enter the number"))
lis = [0,1]
a,b=0,1
for j in range(i):
    su = a + b
    lis.append(su)
    a = b
    b = su
print(lis[i])
