def calculate_income_tax(income):
    if income <= 10000:
        tax = 0
    elif income <= 20000:
        tax = (income - 10000) * 0.10
    else:
        tax = 10000 * 0.10 + (income - 20000) * 0.20
    
    return tax

# Test the function with different income values
income1 = 8000
income2 = 15000
income3 = 25000

tax1 = calculate_income_tax(income1)
tax2 = calculate_income_tax(income2)
tax3 = calculate_income_tax(income3)

print("Income:", income1, "Tax:", tax1)
print("Income:", income2, "Tax:", tax2)
print("Income:", income3, "Tax:", tax3)
