"""Import the Account class from the Account.py file."""
# ADD YOUR CODE HERE
from Accounts import Account
# Define a function for the Savings Account
def create_savings_account(balance, interest_rate, months):
   
    # Create an instance of the `Account` class and pass in the balance and interest parameters.
    #  Hint: You need to add the interest as a value, i.e, 0.
    # ADD YOUR CODE HERE
    savings_account = Account(balance, interest_rate)

    # Calculate interest earned
     # ADD YOUR CODE HERE
    total_interest_earned = 0
    for month in range(months):
         monthly_interest = savings_account.balance * (savings_account.interest / 100 / 12)
         total_interest_earned += monthly_interest
    # Update the savings account balance by adding the interest earned
    # ADD YOUR CODE HERE
    updated_balance = savings_account.balance + total_interest_earned
    savings_account.set_balance(updated_balance)

    # Pass the updated_balance to the set balance method using the instance of the SavingsAccount class.
    # ADD YOUR CODE HERE
    savings_account.set_interest(total_interest_earned)
    # Pass the interest_earned to the set interest method using the instance of the SavingsAccount class.
    # ADD YOUR CODE HERE

    # Return the updated balance and interest earned.
    return updated_balance, total_interest_earned
