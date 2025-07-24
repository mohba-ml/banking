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


def withdraw(b):
    while True:
        amount = float(inputing("how much: ", "i"))

        if amount > b:
            print("higher than your balance")
            print(f"you only have {b}")
            continue

        return amount


def printer(name, balance):
    print(name)
    print(balance)


print("Welcome to Luck Bank")

name = inputing("name: ", "c")
print(f"Hi {name}")

balance = float(inputing("balance: ", 'i'))
print(f"${balance}")

while True:
    inp = input("operation: ")
    match inp.lower():
        case "check" | "c" | "balance" | "check balance" | '1':
            printer(name, balance)
        case "d" | "deposit" | '2':
            balance += float(inputing("how much: ", "i"))
            printer(name, balance)
        case "w" | "withdraw" | '3':
            balance -= withdraw(balance)
            printer(name, balance)
        case "e" | "exit" | '4':
            printer(name, balance)
            quit()
        case _:
            print("Error 404")
            print("Invalid operation")
