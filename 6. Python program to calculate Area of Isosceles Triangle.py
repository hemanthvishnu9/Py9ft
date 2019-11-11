#Python progra to calculate area of Isosceles Triangle
#Assuming side a= side b (For an Isosceles triangle two sides are equal)
a=int(input("Enter length of side a:"))
b=int(input("Enter length of side b:"))
c=int(input("Enter length of side c:"))
p=a+b+c
a=(c/4)*(((4*a*a)-(c*c))**(1/2))
print("Perimeter of Isosceles Triangle:",p,"units")
print("Area of Isosceles Triangle:",a,"sq units")
