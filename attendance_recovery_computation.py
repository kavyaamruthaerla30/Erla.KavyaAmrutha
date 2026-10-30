#Case Study 12: Attendance Recovery Computation
def calculate_recovery(total_classes, attended_classes, target_percent):
    if total_classes <= 0 or attended_classes < 0 or attended_classes > total_classes:
        raise ValueError("Enter valid class counts.")
    if not 0 < target_percent <= 100:
        raise ValueError("Target percentage must be between 0 and 100.")
    current = attended_classes / total_classes * 100
    if current >= target_percent:
        return current, 0
    # Solve (attended + x) / (total + x) >= target / 100
    needed = (target_percent * total_classes - 100 * attended_classes) / (100 - target_percent)
    return current, max(0, int(needed) if needed.is_integer() else int(needed) + 1)

def main():
    total = int(input("Total classes conducted: "))
    attended = int(input("Classes attended: "))
    target = float(input("Required attendance percentage: "))
    current, recovery = calculate_recovery(total, attended, target)
    print(f"Current attendance: {current:.2f}%")
    if recovery == 0:
        print("You have already reached the required attendance.")
    else:
        print(f"Attend the next {recovery} consecutive classes to reach {target:.2f}%.")

if __name__ == "__main__":
    main()
