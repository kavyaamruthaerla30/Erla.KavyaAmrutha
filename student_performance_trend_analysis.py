#Case Study 17: Student Performance Trend Analysis
def analyze_trend(marks):
    if not marks or any(mark < 0 or mark > 100 for mark in marks):
        raise ValueError("Enter one or more marks between 0 and 100.")
    average = sum(marks) / len(marks)
    changes = [marks[i] - marks[i-1] for i in range(1, len(marks))]
    if not changes:
        trend = "Insufficient data to identify a trend"
    elif all(change > 0 for change in changes):
        trend = "Consistently improving"
    elif all(change < 0 for change in changes):
        trend = "Consistently declining"
    elif all(change == 0 for change in changes):
        trend = "Stable"
    else:
        trend = "Fluctuating"
    return average, trend, changes

def main():
    marks = [float(x) for x in input("Enter marks in chronological order, separated by spaces: ").split()]
    average, trend, changes = analyze_trend(marks)
    print(f"Average mark: {average:.2f}")
    print("Trend:", trend)
    print("Change between tests:", changes)

if __name__ == "__main__":
    main()
