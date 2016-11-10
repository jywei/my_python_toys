def compound_interest():
    principal = int(input("Please input your initial deposit: $"))
    rate = float(input("Give us your interest rate: "))
    rate = rate / 100
    time = int(input("Enter the number of year it will be saved: "))
    time += 1
    compund = int(input("How many times is the interest compund yearly? "))

    print("Year %21s" % "Amount on deposit")

    for time in range(1, time):
        formula = principal * (1.0 + rate) ** time
        print("%4d%21.2f" % (time, formula))

def start():
    print("Let's start the bitch!")
    compound_interest()

start()
