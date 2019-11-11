#Python program to print PRIME numbers between an interval
a=int(input("Enter starting value:"))
b=int(input("Enter ending value:"))
for i in range(a,b+1):
    if i>1:
        for x in range(2,i):
            if (i%x)==0:
                break
        else:
            print(i)
