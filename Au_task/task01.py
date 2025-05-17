#Q1:- Write a program that will convert celsius value to fahrenheit.
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = celsius_to_fahrenheit(celsius)
print(f"{celsius}°C is equal to {fahrenheit}°F")


#Q2:- Take 2 numbers as input from the user.Write a program to swap the numbers without using any special python syntax.
def swap_numbers(a, b):
    temp = a
    a = b
    b = temp
    return a, b
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num1, num2 = swap_numbers(num1, num2)
print(f"After swapping: First number = {num1}, Second number = {num2}")


#Q3:- Write a program to find the euclidean distance between two coordinates.Take both the coordinates from the user as input.
import math
def calculate_distance(x1, y1, x2, y2):
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance
print("Enter the coordinates of the first point (x1, y1):")
x1 = float(input("x1: "))
y1 = float(input("y1: "))
print("Enter the coordinates of the second point (x2, y2):")
x2 = float(input("x2: "))
y2 = float(input("y2: "))
distance = calculate_distance(x1, y1, x2, y2)
print(f"The Euclidean distance between the points is: {distance:.2f}")


#Q4:- Write a program to find the simple interest when the value of principle,rate of interest and time period is provided by the user.
def calculate_simple_interest(principal, rate, time):
    return (principal * rate * time) / 100
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest (per annum): "))
time = float(input("Enter the time period (in years): "))
simple_interest = calculate_simple_interest(principal, rate, time)




"""Q5:- Write a program that will tell the number of dogs and chicken are there when the user will provide the value of total heads and legs.
For example:
Input:
heads -> 4
legs -> 12
<br>
Output:
dogs -> 2
chicken -> 2"""
def solve_animals(total_heads, total_legs):
    chickens = (4 * total_heads - total_legs) // 2
    dogs = total_heads - chickens
    if chickens < 0 or dogs < 0 or (2 * chickens + 4 * dogs != total_legs):
        return None  
    else:
        return chickens, dogs
heads = int(input("Enter the total number of heads: "))
legs = int(input("Enter the total number of legs: "))
result = solve_animals(heads, legs)
if result:
    chickens, dogs = result
    print(f"Number of chickens: {chickens}")
    print(f"Number of dogs: {dogs}")
else:
    print("No valid solution exists with the given heads and legs.")


#Q6:- Write a program to find the sum of squares of first n natural numbers where n will be provided by the user.
def calculate_sum_of_squares(n):
    sum_of_squares = 0
    for i in range(1, n + 1):
        sum_of_squares += i ** 2
    return sum_of_squares
n = int(input("Enter the value of n: "))
print("The sum of squares of first", n, "natural numbers is:", calculate_sum_of_squares(n))


#Q7:- Given the first 2 terms of an Arithmetic Series.Find the Nth term of the series. Assume all inputs are provided by the user.
def find_nth_term(a1, a2, n):
    d = a2 - a1  
    return a1 + (n - 1) * d
def main():
    # Get input from the user
    a1 = float(input("Enter the first term (a1): "))
    a2 = float(input("Enter the second term (a2): "))
    n = int(input("Enter the term number (n): ")) 
    an = find_nth_term(a1, a2, n)
    print(f"The {n}th term of the arithmetic series is: {an}")
main()


#Q8:- Given 2 fractions, find the sum of those 2 fractions.Take the numerator and denominator values of the fractions from the user.
def sum_of_fractions(a,b,c,d):
  sum_of_fractions = (a*b)+(c*d)/(b*d)
  return sum_of_fractions
a=int(input("Enter the numerator of the first fraction: "))
b=int(input("Enter the denominator of the second fraction: "))
c=int(input("Enter the numerator of the third fraction: "))
d=int(input("Enter the denominator of the forth fraction: "))
sum = sum_of_fractions(a,b,c,d)
print("The sum of the fractions is:",sum)


""" Q9:- Given the height, width and breadth of a milk tank, you have to find out how many glasses of milk can be obtained? Assume all the inputs are provided by the user.
Input:<br>
Dimensions of the milk tank<br>
H = 20cm, L = 20cm, B = 20cm
<br><br>
Dimensions of the glass<br>
h = 3cm, r = 1cm"""
def calculate_glasses_of_milk():
    height = float(input("Enter the height of the milk tank "))
    width = float(input("Enter the width of the milk tank"))
    breadth = float(input("Enter the breadth of the milk tank"))
    glass_capacity = float(input("Enter the capacity of one glass"))
    tank_volume = height * width * breadth
    num_glasses = tank_volume // glass_capacity
    print(f"Number of glasses of milk that can be obtained: {int(num_glasses)}")
calculate_glasses_of_milk() 