sum1 = 0
count = 0
num = input("Enter your number: ")
while (num != "done"):
    if num.isnumeric():
        num1 = int(num)
        sum1 = sum1 + num1
        count = count + 1
        num = input("Enter your number: ")
    else:
        print("invalid input")
        num = input("Enter your number: ")
avg = sum1 / count
print(sum1,count,avg)
