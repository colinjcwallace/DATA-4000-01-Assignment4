def get_valid_number(prompt, is_float=False):
    while True:
        user_input = input(prompt).strip()
        try:
            if is_float:
                return float(user_input)
            else:
                return int(user_input)
        except ValueError:
            print(f"Invalid input: '{user_input}' is not a valid number. Please try again.")

def main():
    print("--- Retail Sales Data Entry ---")
    
    # Get validated units (int)
    units = get_valid_number("Enter number of units sold: ", is_float=False)
    
    # Get validated price (float)
    price = get_valid_number("Enter price per unit: ", is_float=True)
    
    # Calculate total
    total_revenue = units * price
    
    # Output results
    print("-" * 30)
    print(f"Units Sold: {units}")
    print(f"Price per Unit: ${price:,.2f}")
    print(f"Total Revenue: ${total_revenue:,.2f}")
    print("-" * 30)

main()