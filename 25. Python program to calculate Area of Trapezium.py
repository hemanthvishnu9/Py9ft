#Python program to calculate Area of Trapezium 
a=int(input("Enter length of side a:"))
b=int(input("Enter length of side b:"))
c=int(input("Enter length of side c:"))
d=int(input("Enter length of side d:"))
h=int(input("Enter height of trapezium:"))
a=((a+b)*h)/2
p=a+b+c+d
print("Perimeter of Trapezium=",p,"units")
print("Area of Trapezium=",a,"sq units")
