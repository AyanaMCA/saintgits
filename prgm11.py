tax_rate=0.20
standard_deduction=10000.0
dependent_deduction=3000.0
gross_income=float(input("Enter gross income:"))
num_dependent=int(input("Enter number of dependent:"))
taxable_income=(gross_income-standard_deduction)-(dependent_deduction*num_dependent)
income_tax=taxable_income*tax_rate
print("Income Tax is:",income_tax)
