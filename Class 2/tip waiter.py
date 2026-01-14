bill_amt = int(input("How much was your bill?\n"))
def total_calc(bill_amt, tip_per):
    total = bill_amt * (1 + 0.01 * tip_per)
    total = round(total, 2)
    print(f"Please pay ${total}")
    return total
print(f"Your tip amount is ${total_calc(bill_amt, 20)- bill_amt}")