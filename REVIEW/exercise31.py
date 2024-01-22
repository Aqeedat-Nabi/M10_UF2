def calc_VAT(amount , VAT = None):
    
    print(f"Amount without VAT: {amount} €")
    
    vat_perc = [4 , 10 , 21]
    
    if VAT not in vat_perc:
        VAT = 21
    
    result = (amount * VAT) / 100
    print(f"The VAT requested is :  {result} €")
    
    finalResult = amount + result
    print(f"The final amount with VAT is :  {finalResult} €")
