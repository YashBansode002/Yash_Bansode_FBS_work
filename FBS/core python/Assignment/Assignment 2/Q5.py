costprice=int(input('cost price'))
discount=int(input('discount'))

discount_amount=(costprice*discount)/100
selling_price =costprice-discount_amount

print(f'the discount amount :{discount_amount},the selling price :{selling_price}')