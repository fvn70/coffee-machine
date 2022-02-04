cm = {'water': 400, 'milk': 540, 'beans': 120, 'cups': 9, 'sum': 550}
kinds = {1: {'water': 250, 'milk': 0, 'beans': 16, 'cost': 4},
         2: {'water': 350, 'milk': 75, 'beans': 20, 'cost': 7},
         3: {'water': 200, 'milk': 100, 'beans': 12, 'cost': 6}}


def state():
    print("\nThe coffee machine has:")
    print(f"{cm['water']} of water")
    print(f"{cm['milk']} of milk")
    print(f"{cm['beans']} of coffee beans")
    print(f"{cm['cups']} of disposable cups")
    print(f"{cm['sum']} of money")


def buy():
    print("\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
    kind = int(input())
    cm['water'] -= kinds[kind]['water']
    cm['milk'] -= kinds[kind]['milk']
    cm['beans'] -= kinds[kind]['beans']
    cm['sum'] += kinds[kind]['cost']
    cm['cups'] -= 1


def fill():
    cm['water'] += int(input("Write how many ml of water you want to add:\n"))
    cm['milk'] += int(input("Write how many ml of milk you want to add:\n"))
    cm['beans'] += int(input("Write how many grams of coffee beans you want to add:\n"))
    cm['cups'] += int(input("Write how many disposable coffee cups you want to add:\n"))


def take():
    print(f"I gave you ${cm['sum']}")
    cm['sum'] = 0


state()
cmd = input("\nWrite action (buy, fill, take):\n")
if cmd == 'buy':
    buy()
elif cmd == 'fill':
    fill()
elif cmd == 'take':
    take()
state()
