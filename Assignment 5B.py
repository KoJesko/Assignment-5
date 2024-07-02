# Ask the user to enter an even number
number = int(input("Please enter an even number: "))

# Use a while loop to check if the number is even
while number % 2 != 0:
    # If it is not even, ask the user to enter an even number again
    number = int(input("That's not an even number. Please enter an even number: "))

# When the user enters an even number, print a thank you message
print("Thank you for the even number.")