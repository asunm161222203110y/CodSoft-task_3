import random
import string

def generate_password(length, complexity):
    if complexity == "low":
        characters = string.ascii_letters
    elif complexity == "medium":
        characters = string.ascii_letters + string.digits
    elif complexity == "high":
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        return "Invalid complexity level"

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    length = int(input("Enter the desired length of the password: "))
    complexity = input("Enter the complexity level (low/medium/high): ").lower()

    password = generate_password(length, complexity)

    print("Generated Password:", password)

if __name__ == "__main__":
    main()
