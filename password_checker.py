"""Password Strength Checker
A simple console app that scores a password and suggests improvements.
"""

COMMON = ["password", "123456", "qwerty", "abc123", "letmein", "admin"]


def check_password(pw):
    """Return (score out of 5, list of tips)."""
    score = 0
    tips = []

    if len(pw) >= 8:
        score += 1
    else:
        tips.append("Use at least 8 characters.")

    if len(pw) >= 12:
        score += 1
    else:
        tips.append("12 or more characters is even better.")

    if any(c.islower() for c in pw) and any(c.isupper() for c in pw):
        score += 1
    else:
        tips.append("Mix uppercase and lowercase letters.")

    if any(c.isdigit() for c in pw):
        score += 1
    else:
        tips.append("Add at least one number.")

    if any(not c.isalnum() for c in pw):
        score += 1
    else:
        tips.append("Add a symbol such as ! @ # $.")

    # A common word caps the score no matter how long the password is
    if any(word in pw.lower() for word in COMMON):
        score = min(score, 1)
        tips.append("Avoid common words and patterns.")

    return score, tips


def rating(score):
    if score <= 2:
        return "Weak"
    if score <= 4:
        return "Okay"
    return "Strong"


def main():
    print("=== Password Strength Checker ===")
    print("Type 'q' to quit.\n")

    while True:
        pw = input("Enter a password: ")

        if pw.lower() == "q":
            print("Goodbye!")
            break
        if pw == "":
            print("Please type something first.\n")
            continue

        score, tips = check_password(pw)
        print(f"\nScore: {score}/5 - {rating(score)}")
        for tip in tips:
            print(f"  - {tip}")
        print()


if __name__ == "__main__":
    main()
