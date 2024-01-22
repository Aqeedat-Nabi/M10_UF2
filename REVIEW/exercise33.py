def calc_shopping(shopping_list, vat):
    amount = 0
    discount_applied = 0

    print("The Shopping List : ")
    for i, (price, discount) in enumerate(shopping_list.items(), start=1):
        discounted_price = price - (price * discount / 100)
        amount += price
        discount_applied += discounted_price

        print(f"Product {i}:")
        print(f"  Price before discount: {price} €")
        print(f"  Discount applied: {discount_applied}%")
        print(f"  Price after discount: {discounted_price} €")
        print("---")

    total_with_vat = discount_applied * (1 + vat / 100)

    print(f"Total before discount: {amount} €")
    print(f"Total after discount: {discount_applied} €")
    print(f"Total with VAT ({vat}%): {total_with_vat} €")
