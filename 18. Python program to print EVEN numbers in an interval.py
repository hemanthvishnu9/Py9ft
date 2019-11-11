#Python program to print EVEN numbers in an interval
a=int(input("Enter starting value:"))
b=int(input("Enter ending value:"))
for i in range(a,b):
    if(i%2==0):
        print(i)
