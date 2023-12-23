"""Import the Account class from the Account.py file."""
# ADD YOUR CODE HERE

def create_cd_account(balance, interest_rate, months):
    """Creates a CD account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial CD account balance.
        interest_rate (float): The APR interest rate for the CD account.
        months (int): The length of months for the CD.

    Returns:
        float: The updated CD account balance after adding the interest earned.
        And returns the interest earned.
    """
    # Create an instance of the `Account` class and pass in the balance and interest parameters.
    #  Hint: You need to add the interest as a value, i.e, 0.
    # ADD YOUR CODE HERE
    cd_account = Account(balance, interest_rate)

    # Calculate interest earned
    # ADD YOUR CODE HERE
    total_interest_earned = 0
    for month in range(months):
        monthly_interest = cd_account.balance * (cd_account.interest_rate / 100 / 12)
        total_interest_earned += monthly_interest
    

    # Update the CD account balance by adding the interest earned
    # ADD YOUR CODE HERE
    cd_account.balance += total_interest_earned
    # Pass the updated_balance to the set balance method using the instance of the CDAccount class.
    # ADD YOUR CODE HERE
    cd_account.set_balance(cd_account.balance)
    # Pass the interest_earned to the set interest method using the instance of the CDAccount class.
    # ADD YOUR CODE HERE
    cd_account.set_interest(total_interest_earned)
    # Return the updated balance and interest earned.
    return cd_account.balance, total_interest_earned  # ADD YOUR CODE HERE
