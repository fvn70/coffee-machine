from math import floor

cup = {'water': 200, 'milk': 50, 'beans': 15}
water = int(input("Write how many ml of water the coffee machine has:\n"))
milk = int(input("Write how many ml of milk the coffee machine has:\n"))
beans = int(input("Write how many grams of coffee beans the coffee machine has:\n"))
num = int(input("Write how many cups of coffee you will need:\n"))

cups = floor(min(water / cup['water'], milk / cup['milk'], beans / cup['beans']))

if cups < num:
    print(f"No, I can make only {cups} cups of coffee")
elif cups > num:
    print(f"Yes, I can make that amount of coffee (and even {cups - num} more than that)")
else:
    print("Yes, I can make that amount of coffee")
