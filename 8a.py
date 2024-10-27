a=int(input("Entre a=")) 
b=int(input("Entre b=")) 
try:
 c = ((a+b) / (a-b))
 if a==b:
     raise ZeroDivisionError #Handling of error
except ZeroDivisionError:
 print ("a/b result in 0") 
else:
 print (c)
