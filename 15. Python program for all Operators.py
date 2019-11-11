#Python program for all Operators
a=int(input("Enter number 1:"))
b=int(input("Enter number 2:"))

print("\nArithmetic Operators")
print(a,"+",b,"=",a+b) #Addition
print(a,"-",b,"=",a-b) #Subtraction
print(a,"*",b,"=",a*b) #Multiplication
print(a,"/",b,"=",a/b) #Division
print(a,"%",b,"=",a%b) #Modulus (Remainder)
print(a,"**",b,"=",a**b) #Exponentiation
print(a,"//",b,"=",a//b) #Floor division

print("\nAssignment Operators")
c=a+b   #Assign value
print(c)
c=c+a   
print(c)
c=c-a
print(c)
c=c*a
print(c)
c=c/a
print(c)
c=c%a
print(c)
c=c//a
print(c)
c=c**a
print(c)

print("\nRelational Operators")
print("a==b",a==b) #Equal to
print("a!=b",a!=b) #Not Equal to
print("a>b",a>b)   #Greater than
print("a<b",a<b)   #Less than
print("a>=b",a>=b) #Greater than or Equal to
print("a<=b",a<=b) #Less than or Equal to

print("\nLogical Operations")
print(a>5 and b<5)#AND Operator (Returns TRUE if both conditions are true)
print(a>5 or b<5) #OR Operator (Returns TRUE if one of the conditions are true)
print(not(a>5 and b<5)) #NOT Operator (Returns TRUE if condition is FALSE)

print("\nIdentity Operators")
print(a is b)   #Returns TRUE if both variables are the same object
print(a is not b)   #Returns true if both variables are not the same object

p='Welcome Back'
print("\nMembership Operators")
print('c' in p)
print('o' not in p)

print("\nBitwise Operators")
print(a & b)    #Bitwise AND
print(a | b)    #Bitwise OR
print( ~ b)    #Bitwise NOT
print(a ^ b)    #Bitwise XOR
print(a >> b)   #Bitwise right shift
print(a << b)   #Bitwise left shift




