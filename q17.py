# Write a program that calculates the discount on a product based on the following conditions:
# 1. If price > $100, 20% discount
# 2. If price is between $50 and $100, 10% discount
# 3. If price is < $50, 5% discound
# 4. If price is exactly $0, print "Invalid Price"
# The program should take the price as input and print the final price after the discount

print()
while True:
    try:
        price = int(input("What is the price?\n> $"))
        # 4. If price is exactly $0, print "Invalid Price"
        if price == 0:
            print("\nInvalid price.")
        elif price < 0:
            print("\nInvalid input.")
        else: 
            break
    except ValueError:
        print("\nInvalid input.")

if price > 100:
    discount = 0.2
elif price >= 50 and price <= 100:
    discount = 0.1
# 3. If price is < $50, 5% discound
else:
    discount = 0.05

print(f"\n\
    Original Price: ${price}\n\
    Discounted Price: ${price * (1-discount)}\n\
    ")