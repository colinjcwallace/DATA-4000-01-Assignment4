## Exercise 1: Handling Invalid Sales Data Input
- Created a function get_valid_number that abstracts input validation for reusability across different numeric types.
- Implemented try-except blocks to catch ValueError when a user enters non-numeric data for units or price.
- Utilized a while True loop to ensure the program reprompts the user until valid business data is provided.
- Developed a main function to calculate total revenue and output the results using professional financial f-string formatting.
------------------------------------------------------------------------------------------------------------------------------------

## Exercise 2: Inventory Quantity Checker
- Developed a script to monitor supply chain stock levels against a minimum reorder threshold.
- Implemented specific error handling for ZeroDivisionError to prevent crashes when calculating "Stock Health" percentage if the threshold is set to zero.
- Used an infinite loop to keep the management interface active until valid integers are provided for inventory levels.
- Added logic to print automatic reorder alerts when inventory falls below the required threshold.
-------------------------------------------------------------------------------------------------------------------------------------

## Exercise 3: Customer Age Verification
- Built a marketing compliance tool to verify if customers are eligible for age-restricted promotions (18+).
- Simulated a NameError to practice debugging variable scope and definition within a corporate script.
- Combined try-except with logical if-else checks to ensure age inputs are not only numeric but also positive integers.
- Created a modular structure where get_customer_age handles the data cleaning and the main block handles the eligibility logic.
------------------------------------------------------------------------------------------------------------------------------------

## Exercise 4: Financial Ratio Calculator
- Created a Corporate Finance tool to calculate the Profit Margin Ratio based on user-provided profit and revenue.
- Implemented a try-except-else structure to separate error handling from the "happy path" calculation logic.
- Utilized the pass keyword within the exception block to provide a silent, clean reprompt for ValueError.
- Used the else block to ensure the final financial report only prints if the mathematical operations in the try block are successful.
-------------------------------------------------------------------------------------------------------------------------------------

## Exercise 5: Employee Salary Adjustment Simulator
- Developed an HR tool to simulate annual salary increases while protecting against "fat-finger" data entry errors.
- Created a robust helper function get_validated_input that enforces positive float values for both currency and percentages.

Added business-rule warnings for adjustments exceeding 100% to flag significant promotional changes.

Implemented advanced f-string alignment (^40) to create a centered, professional summary report for the adjustment results.
