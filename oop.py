class Account:
    __slots__ = ['name', 'balance']

    def __init__(self, name:str, balance:int | float):
        self.name = name
        print(f"Hi {name}")
        self.balance = balance
        print(f"${balance}")
    
    def deposit(self, extra):
        self.balance += extra
    
    def withdraw(self, need):
        while need > self.balance:
            print("higher than your balance")
            print(f"you only have {self.balance}")
            need = float(inputing("how much: ", "i"))
        self.balance -= need
    
    def __str__(self):
        return f"{self.name} \n ${self.balance}"

def is_int(x):
    try:
        float(x)
        return True
    except:
        return False


def is_char(x):
    return x.isalpha()


def inputing(m: str, c: str):
    match c:
        case "i":
            f = is_int
        case "c":
            f = is_char
        case _:
            return
    
    inp = input(m)
    print(inp)

    while not f(inp):
        inp = input(m)
        print(inp)
    
    return inp
    
print("Welcome to Luck Bank")

user = Account(inputing("name: ", "c"), float(inputing("balance: ", 'i')))

while True:
    inp = input("operation: ")
    match inp.lower():
        case "check" | "c" | "balance" | "check balance" | '1':
            print(user)
        case "d" | "deposit" | '2':
            user.deposit(float(inputing("how much: ", "i")))
            print(user)
        case "w" | "withdraw" | '3':
            user.withdraw(float(inputing("how much: ", "i")))
            print(user)
        case "e" | "exit" | '4':
            print(user)
            quit()
        case _:
            print("Error 404")
            print("Invalid operation")