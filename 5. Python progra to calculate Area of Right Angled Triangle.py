#Python progra to calculate area of Right Angled Triangle
b=int(input("Enter base of the right angled triangle:"))
p=int(input("Enter perpendicular height of the right angled triangle:"))
h=(b**2+p**2)**(1/2) 
x=b+p+h
a=(1/2)*b*p
print("Perimeter of Right Angled Triangle:",x,"units")
print("Area of Right Angled Triangle:",a,"sq units")
