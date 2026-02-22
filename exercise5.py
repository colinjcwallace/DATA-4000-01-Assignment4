def get_validated_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Error: Value cannot be negative. Please try again.")
                continue
            return value
        except ValueError:
            print("Error: Invalid input. Please enter a numeric value (e.g., 50000.50).")

def main():
    print("--- HR Portal: Salary Adjustment Simulator ---")

    # 1. Get validated inputs using our helper function
    current_salary = get_validated_input("Enter current annual salary: $")
    adjustment_percent = get_validated_input("Enter adjustment percentage (e.g., 5 for 5%): ")

    # 2. Logic Check: Ensure percentage isn't over 100 (optional business rule)
    if adjustment_percent > 100:
        print("Warning: Adjustment is over 100%. Processing as a significant promotion.")

    # 3. Perform Calculations
    # Formula: New Salary = Current + (Current * (Percent / 100))
    increase_amount = current_salary * (adjustment_percent / 100)
    new_salary = current_salary + increase_amount

    # 4. Professional Output Formatting
    print("\n" + "="*40)
    print(f"{'SALARY ADJUSTMENT SUMMARY':^40}")
    print("="*40)
    print(f"Current Salary:     ${current_salary:,.2f}")
    print(f"Adjustment:         {adjustment_percent:.2f}%")
    print(f"Increase Amount:    ${increase_amount:,.2f}")
    print("-" * 40)
    print(f"New Total Salary:   ${new_salary:,.2f}")
    print("="*40)

main()