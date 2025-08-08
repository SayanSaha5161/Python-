#Write a Python program that:
#1.Takes an integer input from the user.
#2.Checks whether the number is even or odd using an if-else statement.
#3.Displays the result accordingly.
'''
number = int(input("Enter an integer: "))

if number % 2 == 0:
    print(number, "is even.")
else:
    print(number, "is odd.")
    print('Thank You')
'''
#Write a Python program that:
#1. Uses a for loop to iterate over numbers from 1 to 50.
#2. Calculates the sum of all integers in this range.
#3. Displays the final sum.

total_sum = 0
for number in range(1, 51):
    total_sum += number
    print("The sum of numbers from 1 to 50 is:", total_sum)
