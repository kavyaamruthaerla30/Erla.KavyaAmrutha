#Case Study 42: Student Marks Matrix Analysis
def analyze_matrix(matrix):
    if not matrix or not matrix[0] or any(len(row) != len(matrix[0]) for row in matrix):
        raise ValueError("Marks must form a non-empty rectangular matrix.")
    row_totals = [sum(row) for row in matrix]
    column_totals = [sum(matrix[r][c] for r in range(len(matrix))) for c in range(len(matrix[0]))]
    return row_totals, column_totals

def main():
    students = int(input("Number of students: "))
    subjects = int(input("Number of subjects: "))
    if students <= 0 or subjects <= 0:
        raise ValueError("Counts must be positive.")
    matrix = []
    for i in range(students):
        row = [float(x) for x in input(f"Enter {subjects} marks for student {i+1}: ").split()]
        if len(row) != subjects or any(mark < 0 or mark > 100 for mark in row):
            raise ValueError(f"Enter exactly {subjects} marks, each from 0 to 100.")
        matrix.append(row)
    row_totals, column_totals = analyze_matrix(matrix)
    print("Total marks per student:", row_totals)
    print("Total marks per subject:", column_totals)
    print("Class average:", sum(row_totals) / (students * subjects))

if __name__ == "__main__":
    main()
