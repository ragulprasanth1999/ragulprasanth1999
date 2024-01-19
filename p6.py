"""Write a program to input an integer 'n' and print the sum of all its even digits and the sum of all its odd digits separately.



Digits mean numbers, not places! That is, if the given integer is "132456", even digits are 2, 4, and 6, and odd digits are 1, 3, and 5.

Constraints
0<= 'n' <=10000"""
n = int(input())
lis =[]
for i in range(n+1):
    lis.append(i)
lis.remove(0)
print(lis)
odd = [i for i in lis if i%2!=0 ]
even =[i for i in lis if i%2==0]
print(sum(odd))
print(sum(even))
