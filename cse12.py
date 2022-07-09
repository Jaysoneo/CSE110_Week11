#prices=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=

price_childs_meal=float(input("what is the price of a child's meal?: $"))
number_childs_meal=int(input("How many children are?: "))

price_adults_meal=float(input("What is the price of an adult's meal?: $"))
number_adults_meal=int(input("How many adults are?: "))

price_drink=float(input("what is the price of a drink?: $"))
number_drinks=int(input("how many drinks are?: "))

q=input('do you want salads? (yes/no): ')
price_salad=0
number_salad=0
if q=="yes":
    price_salad=float(input('what is the price of a salad?: $'))
    number_salad=int(input('how many salads you will buy?: '))

#other=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=

tip=float(input('what is the tip percentage?: '))/100
tax=float(input("What is the tax rate?: "))/100

#calculations=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o

subtotal=price_childs_meal*number_childs_meal + price_adults_meal*number_adults_meal + price_drink*number_drinks + price_salad*number_salad 
sales_tax=subtotal*tax
tip_amount=subtotal*tip
total=tax*subtotal+subtotal+tip_amount

#output=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o

print(f"""--------------------------------------------
Subtotal:      ${round(subtotal,2)}
Sales tax:     ${round(sales_tax,2)}
Tip amount:    ${round(tip_amount,2)}
Total:         ${round(total,2)}
--------------------------------------------""")

#payment=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o

Payment_Amount=float(input("what is the payment amount?: $"))
Change=Payment_Amount-total
while Change < 0:
    print("""
            ERROR

the payment amount is insufficient
""")
    Payment_Amount=float(input("what is the payment amount?: $"))
    Change=Payment_Amount-total
print(f"Change: ${round(Change,2)}")