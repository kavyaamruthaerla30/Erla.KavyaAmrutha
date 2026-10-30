#Case Study 28: Repeated Transaction Detection
from collections import Counter

def find_repeated_transactions(transaction_ids):
    counts = Counter(transaction_ids)
    return {transaction_id: count for transaction_id, count in counts.items() if count > 1}

def main():
    ids = input("Enter transaction IDs separated by spaces: ").split()
    repeated = find_repeated_transactions(ids)
    if repeated:
        print("Repeated transaction IDs:")
        for transaction_id, count in repeated.items():
            print(f"{transaction_id}: appears {count} times")
    else:
        print("No repeated transactions detected.")

if __name__ == "__main__":
    main()
