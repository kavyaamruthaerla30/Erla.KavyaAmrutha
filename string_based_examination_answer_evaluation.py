"""Case Study 31: String-Based Examination Answer Evaluation

Note: Demonstration evaluator using keyword matching, not an official grading system.
"""
import re

def evaluate_answer(answer, keywords, marks_per_keyword=1):
    normalized = set(re.findall(r"[a-zA-Z0-9]+", answer.lower()))
    matched = [word for word in keywords if word.lower() in normalized]
    score = len(matched) * marks_per_keyword
    return matched, score

def main():
    answer = input("Enter the student's answer: ")
    keywords = input("Enter expected keywords separated by commas: ").split(",")
    keywords = [word.strip() for word in keywords if word.strip()]
    marks = float(input("Marks per matched keyword: "))
    matched, score = evaluate_answer(answer, keywords, marks)
    print("Matched keywords:", matched if matched else "None")
    print(f"Estimated score: {score:.2f}")
    print("Review manually: keyword matching may miss correct explanations.")

if __name__ == "__main__":
    main()
