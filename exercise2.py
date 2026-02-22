def check_inventory():
    print("--- Supply Chain Inventory Management ---")
    
    while True:
        try:
            # 1. Prompt for inputs
            inventory = int(input("Enter current inventory level: "))
            threshold = int(input("Enter minimum reorder threshold: "))

            # 2. Handle Reorder Logic
            if inventory < threshold:
                print("\n ALERT: Inventory is BELOW threshold. Place a reorder immediately!")
            else:
                print("\n Status: Inventory levels are sufficient.")

            # 3. Calculate Stock Health (Percentage of Threshold)
            # This triggers ZeroDivisionError if threshold is 0
            health_percentage = (inventory / threshold) * 100
            print(f"Stock Health: {health_percentage:.1f}% of minimum requirement.")
            
            # If we reach here, inputs were valid; break the loop
            break

        except ValueError:
            print(" Input Error: Please enter whole numbers (integers) only.\n")
            
        except ZeroDivisionError:
            print(" Math Error: Reorder threshold cannot be zero. Please re-enter data.\n")


check_inventory()

# Could deal with negative numbers