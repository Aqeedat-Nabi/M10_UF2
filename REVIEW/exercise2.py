value = float(input("Enter a value in € : \n"))
print("The value is : " + str(value) + " €")
VAT = float(input("Enter the VAT to be applied (4%, 10% or 21%) : \n"))
print("The VAT requested is : " + str(VAT) + "%")
result = (VAT /100) * value
finalResult = value + result
print(f"The final result with VAT is :  {finalResult:.2f} €")