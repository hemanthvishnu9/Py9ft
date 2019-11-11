#Python program to check if number entered is PRIME or COMPOSITE
a=int(input("Enter a number:"))
for i in range(2,a):
    if (a%i)==0:
        print(a,"is a composite number")
        break
else:
    print(a,"is a prime number")
            
