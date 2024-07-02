# Python code to print every number less than 25
for i in range(25):
    print(i)
    if i % 7 == 0 and i != 0:  # Check if the number is divisible by 7
        print("This number is divisible by seven!")

# Extra Extra: Allowing user input for the maximum number
max_number = int(input("Enter the maximum number to count down from: "))
for i in range(max_number):
    print(i)
    if i % 7 == 0 and i != 0:  # Check if the number is divisible by 7
        print("This number is divisible by seven!")