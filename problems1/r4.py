#factorial
m =int(input("Enter the number :"))
fac = 1
if m < 0:
    print("factorial does not exist")
elif m == 1:
    print("Factorial is 1")
else:
    for i in range(1,m+1):
        fac=fac*i
print("factorial is : ",fac)
    