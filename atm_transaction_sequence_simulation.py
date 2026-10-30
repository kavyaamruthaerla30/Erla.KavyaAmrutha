#Case Study 13: ATM Transaction Sequence Simulation
def run_atm(balance, transactions, pin, entered_pin):
    if entered_pin != pin:
        return balance, ["Access denied: incorrect PIN."]
    log = ["ATM session started."]
    for kind, amount in transactions:
        if amount <= 0:
            log.append("Rejected: amount must be positive.")
        elif kind == "deposit":
            balance += amount
            log.append(f"Deposit successful: Rs. {amount:.2f}")
        elif kind == "withdraw":
            if amount > balance:
                log.append(f"Declined: insufficient balance for Rs. {amount:.2f}")
            else:
                balance -= amount
                log.append(f"Withdrawal successful: Rs. {amount:.2f}")
        else:
            log.append(f"Rejected: unknown transaction '{kind}'.")
    log.append(f"Available balance: Rs. {balance:.2f}")
    return balance, log

def main():
    balance = float(input("Opening balance: Rs. "))
    pin = input("Set demo PIN: ")
    entered = input("Enter PIN: ")
    transactions = []
    while True:
        choice = input("Transaction (deposit/withdraw/done): ").strip().lower()
        if choice == "done":
            break
        amount = float(input("Amount: Rs. "))
        transactions.append((choice, amount))
    balance, messages = run_atm(balance, transactions, pin, entered)
    print("\n".join(messages))

if __name__ == "__main__":
    main()
