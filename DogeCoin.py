User
import math

def calculate_individual_selling_price(cost, markup_percent, fee1_percent, fee2_percent):
    # Apply markup to the cost for a single item.
    marked_up_cost = cost * (1 + markup_percent / 100)

    # Calculate fees for a single item.
    fee1 = marked_up_cost * (fee1_percent / 100)
    fee2 = marked_up_cost * (fee2_percent / 100)

    # Calculate total fees for a single item.
    total_fees = fee1 + fee2

    # Calculate selling price for a single item.
    selling_price = marked_up_cost + total_fees

    # Round up to the nearest one-hundred-thousandth.
    selling_price = math.ceil(selling_price * 1e5) / 1e5

    return selling_price

# Input values
cost = float(input("Enter the cost per Doge Coin: "))
markup_percent = float(input("Enter the markup percentage you'd like to sell for: "))

# Define implicit fees as percentages.
fee1_percent = 0.1301
fee2_percent = 0.096

# Assume quantity is always one.
qty = 1

# Calculate and display the selling price for a single item.
result = calculate_individual_selling_price(cost, markup_percent, fee1_percent, fee2_percent)
print(f"The minimum selling price for 1 coin should be: {result} to render a profit")