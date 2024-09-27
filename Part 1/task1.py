# Task 1: Adding Even Numbers (10 points)
#  Objective: Write a Python program that calculates the sum of all even numbers between 1 and
# 100 (inclusive).  Instructions: Use a for loop and the range() function to iterate through the even numbers. 

even_numbers = 0

for i in range(2, 101, 2):
    even_numbers += 1

print(f"The sum of all even numbers between 1 and 100 is: {even_numbers}")