def with_vat(ftotal, vat = 21):
    ftotal = float(ftotal) * (1 + vat / 100)   
    return ftotal 

ftotal = input('Enter the price of the entire cart: ')
result = with_vat(ftotal)
print(result)
