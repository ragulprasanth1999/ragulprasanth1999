#fibanoci series
m = int(input("Enter the number : "))
a = 0
b = 1
print(a)
print(b)
for i in range(2,m):
    add = a + b
    print(add)
    a=b
    b=add