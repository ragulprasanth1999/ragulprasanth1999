#The user given set of 2 choice
#asked to select 1 ....1 - to find radius of circle 2 - area of reactangle
ch = int(input("Enter CH value"))
a=[3,2]
def areaSwitchCase(ch,*a):
    if ch==1:
        return (3.14*(a**2))
    elif ch==2:
        var = 1
        for i in a:
            var *= i
        return float(var)
l= areaSwitchCase(ch,*a)
print(l)