#Python program to get selling price and GST rate and print invoice along with both CGST and SGST values
sp=float(input("Enter selling price:"))
gst=float(input("Enter GST rate%:"))
tax=(gst/100)*sp
print("-------------Invoice-------------")
print("Item Name-------------Price")
print("Product X-------------",sp,"Rs")
print("GST%------------------",gst,"%")
print("Total GST tax---------",tax,"Rs")
print("CGST%-----------------",gst/2,"%")
print("CGST Tax--------------",tax/2,"Rs")
print("SGST%-----------------",gst/2,"%")
print("SGST Tax--------------",tax/2,"Rs")
print("Total Amount----------",sp+tax,"Rs")

