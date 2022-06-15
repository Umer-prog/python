# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


#def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    #print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
    #print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/d


def adder(x,y):
    '''
    print("your first number is: ",x)
    print("your second number is: ",y)
    print("On addition")
    '''
    z = x + y
    print("your answer is: ",z)
def multiplyer(x,y):
    z = x * y
    print("multiplied values are: ", z)
print("for addition press 1 for multiplication press 2")
choice = float(input("enter your choice:"))

a = 5
b = 2
c = 3
d = 50
e = 60
f = 96
g = 100
if choice == 1:
    adder(a,b)
elif choice == 2:
    multiplyer(c,d)
else:
    print("wrong input choice")

