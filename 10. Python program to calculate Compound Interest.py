#Python program to calculate Compound Interest
p=int(input("Enter principal amount: Rs"))
r=float(input("Enter rate%:"))
t=int(input("Enter time period(in years):"))
a=p*((1+r/100)**t)
c=a-p
print("Total Amount= Rs",a)
print("Compound Interest= Rs",c)
