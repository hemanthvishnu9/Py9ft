#Python program to calculate profit percentage from the sales of goods
b=float(input("Enter buying price:"))
s=float(input("Enter selling price:"))
if(s>b):
    p=s-b
    pp=(p/b)*100
    print("Profit:",p,"Rs","\n","Profit%:",pp,"%")
else:
    l=b-s
    lp=(l/b)*100
    print("Loss:",l,"Rs","\n","Loss%:",lp,"%")
