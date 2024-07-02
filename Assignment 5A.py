# Program to calculate the total price for movie tickets

# Define the ticket price
ticket_price = 11

# Ask the user for the number of tickets
num_tickets = int(input("Enter the number of movie tickets you would like to buy: "))

# Check if the order qualifies for a bulk discount
if num_tickets > 20:
    ticket_price = 7  # Discounted price

# Calculate the total price
total_price = num_tickets * ticket_price

# Print out the total price
print(f"The total price for {num_tickets} movie tickets is ${total_price}.")