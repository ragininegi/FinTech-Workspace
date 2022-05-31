"""Split Second Homebuying."""

# @TODO: # Use the following variables for present value calculations.
home_price = 110000  # Investment cost
expected_sale_price = 120000  # Future Value of the home
hurdle_rate = 0.10  # 0.10 = 10% # Annual Discount Rate; minimum return expected
holding_months = 12  # Number of months until sold (until Future Value)

# @TODO: Using `expected_sale_price`, `hurdle_rate`, and `holding_months`,
# calculate the present value of the home. Save the result as a new
# variable named `present_value`.
# Use the **monthly** version of the present value formula. 
# YOUR CODE HERE!

present_value = expected_sale_price / (1+hurdle_rate/12) ** holding_months

print(f"Present Value is ${present_value: .2f}")

# @TODO: Put `present_value` into a conditional statement:
# If present value is greater than cost to buy (home_price), print a statement to buy the property:
# Otherwise, print a statement that you will pass on the opportunity:
# Bonus! The edge case: print that you expect to break even on this deal
# YOUR CODE HERE
if present_value > home_price:
    print("Good Buy")
elif present_value < home_price:
    print("Not worth buying! It is offered at a price that is more than what it is worth!")

elif present_value == home_price:
    print("Breakeven case")
