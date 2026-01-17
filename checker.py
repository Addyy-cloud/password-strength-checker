import re

def check_password(password):
    issues = []

    if len(password) < 8:
        issues.append("Password must be at least 8 characters long.")
    if not re.search(r"[A-Z]", password):
        issues.append("Add at least one uppercase letter.")
    if not re.search(r"[a-z]", password):
        issues.append("Add at least one lowercase letter.")
    if not re.search(r"[0-9]", password):
        issues.append("Add at least one number.")
    if not re.search(r"[!@#$%^&*()_+]", password):
        issues.append("Add at least one special character.")

    if not issues:
        return "Strong", []
    elif len(issues) <= 2:
        return "Medium", issues
    else:
        return "Weak", issues

if __name__ == "__main__":
    pwd = input("Enter password: ")
    strength, feedback = check_password(pwd)

    print(f"\nPassword Strength: {strength}")
    if feedback:
        print("Suggestions:")
        for item in feedback:
            print("-", item)
