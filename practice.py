#for values from 1 to n 
 i = 0
 n = int(input("Enter number of values: "))
 while (i < n):
     i = i + 1
     print ( i )
    
#for odd values 
i = 1
c = 0
n = int(input("enter number of odd values: "))
print ( i )
while (c < n):
    i = i + 2
    c = c + 1
    print ( i )

#for even values
i = 0
c = 0
n = int(input("enter number even values: "))
while (c < n):
    i = i + 2
    c = c + 1
    print ( i )
#printing square of a number
c = 0
n = int(input("enter number of squares: "))
while (c < n):
    i = c ** 2
    c = c + 1
    print ( i )


c = 1
n = int(input("enter number: "))
while (c < n):
    i = c * 10 - c ** 2
    c = c + 1
    print ( i )


#fibonacci series
c = 2
i = 1
p = 0
n = int(input("enter number: "))
print (p)
print (i)
while ( c < n): 
    b = i + p
    print (b)
    p = i
    i = b
    c = c + 1

#number divisible by 16    
print("enter -1 to stop")
n = float(input("Enter your number ="))
while n != -1:
    if n%16 == 0:
        print("number is divisible by 16")
    else :
        print("number is not divisible by 16")
    n = float(input("Enter your number ="))

#number divisible by another number
f = float(input("enter first number: "))
s = float(input("enter second number: "))
while f != -1:
    if f%s == 0:
        print ("its divisible")
    else:
        print ("its not divisible")
    f = float(input("enter first number: "))
    s = float(input("enter second number: "))
#checking divisiblity
n = float(input("Enter you number= "))
c = 1
x = 1
while c != n:
    if n%c == 0 :
        x = x + 1
    c = c + 1
print (x)


        










