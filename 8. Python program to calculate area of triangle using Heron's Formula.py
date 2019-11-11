#Python program to calculate area of triangle using Heron's Formula
a=int(input("Enter length of side a:"))
b=int(input("Enter length of side b:"))
c=int(input("Enter length of side c:"))
p=a+b+c #Perimeter of triangle
s=p/2   #Semi-perimeter of triangle
a=(s*(s-a)*(s-b)*(s-c))**(1/2) #Heron's Formula
print("Perimeter of Triangle:",p,"units")
print("Area of Triangle:",a,"sq units")
