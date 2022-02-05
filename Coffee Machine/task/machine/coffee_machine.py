kinds = {'1': {'water': 250, 'milk': 0, 'beans': 16, 'cost': 4},
         '2': {'water': 350, 'milk': 75, 'beans': 20, 'cost': 7},
         '3': {'water': 200, 'milk': 100, 'beans': 12, 'cost': 6}}

class States:
    WAIT = 1
    BUY = 2
    FILL = 3
    WATER = 4
    MILK = 5
    BEAN = 6
    CUP = 7
    EXIT = 0

class CoffeeMachine:
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.cups = 9
        self.sum = 550
        self.currentState = States.WAIT

    def state(self):
        print("\nThe coffee machine has:")
        print(f"{self.water} of water")
        print(f"{self.milk} of milk")
        print(f"{self.beans} of coffee beans")
        print(f"{self.cups} of disposable cups")
        print(f"${self.sum} of money")


    def buy(self, msg):
        self.currentState = States.WAIT
        if msg == 'back':
            return
        coffee = kinds[msg]
        if coffee['water'] > self.water:
            print("Sorry, not enough water!")
        elif coffee['milk'] > self.milk:
            print("Sorry, not enough milk!")
        elif coffee['beans'] > self.beans:
            print("Sorry, not enough beans!")
        elif self.cups < 1:
            print("Sorry, not enough cups!")
        else:
            print("I have enough resources, making you a coffee!")
            self.water -= coffee['water']
            self.milk -= coffee['milk']
            self.beans -= coffee['beans']
            self.sum += coffee['cost']
            self.cups -= 1


    def fill(self, msg):
        if self.currentState == States.FILL:
            print("\nWrite how many ml of water do you want to add: ")
            self.currentState = States.WATER
        elif self.currentState == States.WATER:
            self.water += int(msg)
            print("Write how many ml of milk do you want to add: ")
            self.currentState = States.MILK
        elif self.currentState == States.MILK:
            self.milk += int(msg)
            print("Write how many grams of coffee beans do you want to add: ")
            self.currentState = States.BEAN
        elif self.currentState == States.BEAN:
            self.beans += int(msg)
            print("Write how many disposable cups of coffee do you want to add: ")
            self.currentState = States.CUP
        elif self.currentState == States.CUP:
            self.cups += int(msg)
            self.currentState = States.WAIT


    def take(self):
        print(f"I gave you ${self.sum}")
        self.sum = 0


    def read(self, msg):
        if self.currentState == States.WAIT:
            self.read_cmd(msg)
        elif self.currentState == States.BUY:
            self.buy(msg)
        else:
            self.fill(msg)

    def read_cmd(self, cmd):
        if cmd == 'buy':
            print("\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ")
            self.currentState = States.BUY
            return
        if cmd == 'fill':
            self.currentState = States.FILL
            self.fill(cmd)
        elif cmd == 'take':
            self.take()
        elif cmd == 'remaining':
            self.state()
        elif cmd == 'exit':
            self.currentState = States.EXIT
        else:
            return

cm = CoffeeMachine()
while cm.currentState != States.EXIT:
    if cm.currentState == States.WAIT:
        print("\nWrite action (buy, fill, take, remaining, exit): ")
    cm.read(input())
