from decimal import Decimal, getcontext

# Using float (prone to errors)
result = 0.1 + 0.2
print("Using float:", result)  # Expected 0.3 but shows 0.30000000000000004

d1 = Decimal("0.1")
d2 = Decimal("0.2")
result_decimal = d1 + d2
print("Using decimal:", result_decimal)  # Outputs 0.3 precisely

# Set precision to 4 decimal places
getcontext().prec = 4


num1 = Decimal("1.12345")
num2 = Decimal("2.67890")

# Addition with precision
result = num1 + num2
print("With precision 4:", result)  # Outputs 3.802

# Rounding
rounded_result = result.quantize(Decimal("0.01"))  # Round to 2 decimal places
print("Rounded to 2 decimals:", rounded_result)  # Outputs 3.80


ans = 5.678 - 2.345
print("float ans:", ans)

a1 = Decimal("5.678")
a2 = Decimal("2.345")
answer = a1 - a2
print("Decimal answer:", answer)




# Set precision to ensure accurate calculations
getcontext().prec = 6

def calculate_total_cost(prices, quantities):
    """
    Calculate the total cost of items with precise decimal calculations.
    
    Args:
    prices (list): List of item prices
    quantities (list): List of corresponding item quantities
    
    Returns:
    Decimal: Total cost of all items
    """
    # Validate input
    if len(prices) != len(quantities):
        raise ValueError("Prices and quantities lists must be of equal length")
    
    # Calculate total cost
    total_cost = Decimal('0.00')
    for price, quantity in zip(prices, quantities):
        try:
            # Convert to Decimal to avoid floating-point imprecision
            price_decimal = Decimal(str(price))
            quantity_decimal = Decimal(str(quantity))
            
            # Calculate item total and add to overall total
            item_total = price_decimal * quantity_decimal
            total_cost += item_total
        except (TypeError, ValueError):
            print(f"Warning: Invalid input - Price: {price}, Quantity: {quantity}")
    
    return total_cost

# Example usage
def main():
    # Sample data
    prices = [10.50, 5.25, 7.75]
    quantities = [2, 3, 1]
    
    try:
        total = calculate_total_cost(prices, quantities)
        print(f"Total Cost: ${total:.2f}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()