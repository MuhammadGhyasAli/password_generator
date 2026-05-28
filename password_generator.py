import random
import string

def generate_password(length, use_special=False):
    pool = string.ascii_letters + string.digits
    if use_special:
        pool += "!@#$%^&*"

    if length < 4:
        return None

    password = []
    password.append(random.choice(string.digits))
    if use_special:
        password.append(random.choice("!@#$%^&*"))
    remaining = length - len(password)
    password.extend(random.choice(pool) for _ in range(remaining))
    random.shuffle(password)
    return "".join(password)

print("===== PASSWORD GENERATOR =====")

while True:
    try:
        raw = input("Password length (or 0 to quit): ").strip()
        length = int(raw)
        if length == 0:
            print("Goodbye!")
            break
        if length < 4:
            print("Minimum length is 4 for security.")
            continue
        special = input("Include special characters? (y/n): ").strip().lower() == "y"
        password = generate_password(length, special)
        print(f"Generated password: {password}")
        print("-" * 40)
    except ValueError:
        print("Enter a valid number.")
