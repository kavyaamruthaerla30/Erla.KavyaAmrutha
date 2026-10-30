#Case Study 29: Password Policy Validation Engine
import string

def validate_password(password):
    checks = {
        "At least 8 characters": len(password) >= 8,
        "Contains an uppercase letter": any(c.isupper() for c in password),
        "Contains a lowercase letter": any(c.islower() for c in password),
        "Contains a digit": any(c.isdigit() for c in password),
        "Contains a special character": any(c in string.punctuation for c in password),
        "Contains no whitespace": not any(c.isspace() for c in password),
    }
    return checks, all(checks.values())

def main():
    password = input("Enter a password to validate: ")
    checks, valid = validate_password(password)
    for rule, passed in checks.items():
        print(f"{'PASS' if passed else 'FAIL'} - {rule}")
    print("Password meets policy." if valid else "Password does not meet policy.")

if __name__ == "__main__":
    main()
