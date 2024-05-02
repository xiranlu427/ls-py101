def tip_calculator():
    amount = float(input("What is the bill? "))
    tip_rate = float(input("What is the tip percentage? "))
    tip = amount * tip_rate / 100
    total = amount + tip
    print(f"The tip is ${tip:.2f}\n"
          f"The total is ${total:.2f}")

tip_calculator()
