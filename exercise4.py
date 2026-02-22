def calculate_profit_margin():
    print("--- Corporate Finance: Profit Margin Tool ---")
    
    while True:
        try:
            # 1. Prompt for financial data
            profit = float(input("Enter net profit: "))
            revenue = float(input("Enter total revenue: "))

            # 2. Calculate the ratio
            # This will trigger ZeroDivisionError if revenue is 0.0
            margin = (profit / revenue) * 100

        except ValueError:
            pass 
            
        except ZeroDivisionError:
            print("Finance Error: Revenue cannot be zero. Margin is undefined.")
            print("Please re-enter valid financial figures.\n")

        else:
            # This block only runs if NO exceptions were raised in the 'try' block
            print("-" * 30)
            print(f"Analysis Complete:")
            print(f"Net Profit:     ${profit:,.2f}")
            print(f"Total Revenue:  ${revenue:,.2f}")
            print(f"Profit Margin:  {margin:.2f}%")
            print("-" * 30)
            
            # Exit the loop once a successful calculation is made
            break

calculate_profit_margin()