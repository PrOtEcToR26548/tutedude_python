# Task 1: Check if a Number is Even or Odd

a = int(input('Enter the value: '))
if (a%2)==0:
    print('Input is Even number')
else:
    print('Input is Odd number')

# Task 2: Sum of Integers from 1 to 50 Using a Loop

num = 0
c=1
while c<=50:
    num=num+c
    c=c+1
print('Sum of sequence 1 to 50 is: ',num)