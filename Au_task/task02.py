#Problem1: Write a program that will give you in hand monthly salary after deduction on CTC - HRA(10%), DA(5%), PF(3%) 
#and taxes deduction as below:
#Salary(Lakhs) : Tax(%)
#Below 5 : 0%
#5-10 : 10%
#10-20 : 20%
#aboove 20 : 30%**bold text**
def final_Salary(Salary):
  HRA = 0.10*Salary
  DA = 0.05*Salary
  PF = 0.03*Salary
  if Salary<=5000:
    print("Tax deduction 0%")
  elif Salary<=10000:
    print("Tax deduction 10%")
  elif Salary<=20000:
    print("Tax deduction 20%")
  else:
    print("Salary is not correct")
  final = Salary - (HRA+DA+PF)
  return final
print(final_Salary(15000) )

#Problem2: Write a program that take a user input of three angles and will find out whether it can form a triangle or not.
a = int(input("Enter a angle"))
b = int(input("Enter a angle"))
c = int(input("Enter a angle"))
if a+b+c == 180:
  print("It is a triangle")
else:
  print("It is not a triangle")


#Problem 3: Write a program that will take user input of cost price and selling price 
#and determines whether its a loss or a profit.
cost_price = float(input("Enter a cost price"))
selling_price = float(input("Enter a selling price"))
if cost_price>selling_price:
  print("It is a loss of",cost_price-selling_price)
elif cost_price<selling_price:
  print("It is a profit of",selling_price-cost_price)
else:
  print("It is a loss")


#Problem 4: Write a menu-driven program -
#1. cm to ft
#2. km to miles
#3. USD to INR
#4. exit
def convert(n):
  ft=n/30.48
  miles=n/1.609
  INR=n/84.40
  return ft,miles,INR
n=int(input("Enter a number:"))
ft, miles, INR = convert(n)
print("value of {n}cm to {ft}ft:",ft)
print("value of {n}km to {miles}miles:",miles)
print("value of {n}usd to {INR}INR:",INR)
print("Exit")


#Problem 5: Display Fibonacci series up to 10 terms.
#Note: The Fibonacci Sequence is a series of numbers. 
#The next number is found by adding up the two numbers before it. 
#The first two numbers are 0 and 1. For example, 0, 1, 1, 2, 3, 5, 8, 13, 21. 
#The next number in this series above is 13+21 = 34
def fibonacci(n):
    a = 0
    b = 1
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return 0
    elif n == 1:
        return b
    else:
        for i in range(1, n+1):
            c = a + b
            a = b
            b = c
        return b
print(fibonacci(5))


#Problem 6: Find the factorial of a given number.
#Write a program to use the loop to find the factorial of a given number.
#The factorial (symbol: `!`) means to multiply all whole numbers from the chosen number down to 1.
#For example: calculate the factorial of 5
#5! = 5 × 4 × 3 × 2 × 1 = 120
Output:120
n = int(input("Enter a number"))
fact = 1
for i in range(1, n + 1):
    fact = fact*i
print(fact)


#Problem 7:Reverse a given integer number.
#Example:
#Input:76542
#Output:24567
N = int(input("Enter a number"))
while N > 0:
    last_digit = N % 10
    print(last_digit, end="")
    N = N // 10

#Problem 8: Take a user input as integer N. Find out the sum from 1 to N.
# If any number if divisible by 5, then skip that number. And if the sum is greater than 300, 
#don't need to calculate the sum further more. Print the final result. And don't use for loop to solve this problem.
#Example1:
#Input:30
#Output:276
N = int(input("Enter a number: "))
i = 1
sum = 0
while i <= N and sum <= 300:
    if i % 5 != 0:
        sum = sum + i
    i = i+1
print("Final sum:", sum)

#Problem 9: Write a program that keeps on accepting a number from the user until the user enters Zero.
#Display the sum and average of all the numbers.
a = int(input("Enter a number"))
sum=0
temp = a
for a in range(a,0,-1):
  sum =sum+a
  Average=sum/temp
  print(a)
print(sum)
print(Average)

#Problem 10: Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
#between 2000 and 3200 (both included). The numbers obtained should be printed in a comma-separated sequence on a single line.
for i in range(2000,3201):
  if(i%7==0 and i%5!=0):
    print(i,end=",")

#Problem 11: Write a program, which will find all such numbers between 1000 and 3000 (both included) 
# such that each digit of the number is an even number. 
# The numbers obtained should be printed in a space-separated sequence on a single line.
for i in range(1000,3000):
  N=i
  flag=True
  while N>0:
    last_digit=N%10
    if last_digit%2 != 0:
      flag=False
      break
    N=N//10
    if flag:5
    print(i,end=" ")


#Problem 12: A robot moves in a plane starting from the original point (0,0). 
#The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps.
#The trace of robot movement is shown as the following:
#UP 5
#DOWN 3
#LEFT 3
#RIGHT 2
#The numbers after the direction are steps.
#means robot stop there.
#Please write a program to compute the distance from current position after a sequence of movement and original point.**
#If the distance is a float, then just print the nearest integer.*
#Example:
#Input:
#UP 5
#DOWN 3
#LEFT 3
#RIGHT 2
#Output:2
x=0
y=0
print("up",1)
print("down",2)
print("left",3)
print("right",4)
a1 = int(input("Enter a number:"))
a2 = int(input("Enter a number:"))
if (a1== 1):
    a2=y+a2
    print("for move up:",a2)
elif (a1 == 2):
    a2=y-a2
    print("for move down:",a2)
elif (a1 == 3):
    a2=y+a2
    print("for move left",a2)
elif (a1 == 4):
    a2=y-a2
    print("for move right",a2)
else:
    print(exit)
    
#Problem 13:Write a program to print whether a given number is a prime number or not
n = int(input("Enter a number"))
if n==1 or n==0:
  print("not a prime number")
if n>1:
  for i in range(2,n):
    if(n%i)==0:
      print("not a prime number")
      break
  else:
    print("a prime number")


#Problem 14:Print all the Armstrong numbers in a given range.
#Range will be provided by the user
#Armstrong number is a number that is equal to the sum of cubes of its digits. 
#For example 0, 1, 153, 370, 371 and 407 are the Armstrong numbers.
number=int(input("Enter a number"))
def armstrong(number):
  digits=str(number)
  power=len(digits)
  total=sum(int(digit)**power for digit in digits)
  return total
if number==armstrong(number):
  print("Armstrong number")
else:
  print("Not armstrong number")

#Problem 15:Calculate the angle between the hour hand and minute hand.
#Note: There can be two angles between hands; we need to print a minimum of two. 
#Also, we need to print the floor of the final result angle. For example, if the final angle is 10.61, we need to print 10.
#Input:H = 9 , M = 0
#Output:90
#Explanation:The minimum angle between hour and minute hand when the time is 9 is 90 degress.
def clock_angle(H,M):
  clock_angle= abs((11/2)*M-30*H)
  return clock_angle
H = int(input("Enter value of hour"))
M = int(input("Enter value of minute"))
angle=360-clock_angle(H,M)
print(angle)


#Problem 16:Given two rectangles,
#find if the given two rectangles overlap or not.
#A rectangle is denoted by providing the x and y coordinates of two points: 
#the left top corner and the right bottom corner of the rectangle. 
#Two rectangles sharing a side are considered overlapping. 
#(L1 and R1 are the extreme points of the first rectangle and L2 and R2 are the extreme points of the second rectangle).
x1=int(input(" "))
y1=int(input(" "))
x2=int(input(" "))
y2=int(input(" "))
x3=int(input(" "))
y3=int(input(" "))
x4=int(input(" "))
y4=int(input(" "))
def do_overlap(x1,y1,x2,y2,x3,y3,x4,y4):
  if x2<=x3 or x4<=x1:
    return False
  if y2>=y3 or y4>=y1:
    return False
  return True
if do_overlap(x1, y1, x2, y2, x3, y3, x4, y4):
  print("do overlap")
else:
  print("do not overlap")

