#Control Structures

#Imports (for math)
import math

#If statements

#basic int
num = 2

#Checking if its positive
if num >= 0:
    print("This num is even!")

#For loops
#Method to find if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n% i == 0:
            return False
    return True

#Array to store the nums
primes = []

#Checks all numbers 2,40 if there prime
for i in range(2, 40):
    #If the length is less then or equal to 9 (finds 10 nums)
    if len(primes) <= 9:
        if is_prime(i):
            primes.append(i)
    else:
        break
#Displays all the prime numbers
print(primes)

#While loop to sum nums

#starting num, will 
starting_num = 1

str_start = str(starting_num)

#Ending Num
end_num = 100

#var to store summation
total = 0

while starting_num <= end_num:
    total += starting_num
    starting_num += 1
print("The sum of numbers from " + str_start + " to " + str(end_num) + " is " + str(total))