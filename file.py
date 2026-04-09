# Program to calculate the average of numbers entered by the user

# Ask the user how many numbers they want to input
n = int(input("How many numbers do you want to enter? "))

# Initialize a list to store numbers
numbers = []

# Loop to get all numbers from the user
for i in range(n):
    num = float(input(f"Enter number {i+1}: "))
    numbers.append(num)

# Calculate the sum and average
total = sum(numbers)
average = total / n

# Display the results
print(f"The sum of the numbers is: {total}")
print(f"The average of the numbers is: {average}")
