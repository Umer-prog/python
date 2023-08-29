#number input
num = int(input("enter a number "))
#this is a flag either true or false
f = 0
#initial divider
i = 2
#biggest number multiplied can be half of the given number
#like if u want 50 biggest number u will multiply with any number is its half 25
#less then 1/2 will give you number in decimal
while i <= num / 2:
#if number divided by i gives 0 remainder then flag true or 1
    if num % i == 0:
        f = 1
#to break out of the loop
        break
    i = i + 1

if f == 0:
    print("prime")
else:
    print("non prime")
    
