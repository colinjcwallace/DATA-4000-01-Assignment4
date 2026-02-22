def get_customer_age():

    while True:
        try:
            # Simulated NameError: Referencing a variable that isn't defined yet
            # (Unless you uncomment the line above)
            print(f"--- {company_name} Verification ---")
            
            age_input = input("Please enter the customer's age: ").strip()
            age = int(age_input)

            if age < 0:
                print("Age cannot be negative. Please try again.")
                continue
            
            return age

        except ValueError:
            print(f"Error: '{age_input}' is not a valid number. Please enter an integer.")
        
        except NameError:
            print("Developer Error: 'company_name' is referenced but not defined!")
            # Temporary fix so the code can proceed for the student's demo:
            company_name = "Thorin and Company (Fixed)"

def main():
    # Call the function and get a valid age
    customer_age = get_customer_age()
    
    # Eligibility Logic (Legal Requirement: 18+)
    if customer_age >= 18:
        print("Status: ELIGIBLE for age-restricted marketing campaigns.")
    else:
        print("Status: INELIGIBLE. Customer is under 18.")

main()