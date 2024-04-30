import random
import string
class password_generate():
    def __init__(self):
        pass
    def generate_password(self,length, complexity):
        if complexity == 'simple':
            chars = string.ascii_letters + string.digits
        elif complexity == 'medium':
            chars = string.ascii_letters + string.digits + string.punctuation
        elif complexity == 'strong':
            chars = string.ascii_letters + string.digits + string.punctuation + string.ascii_uppercase + string.ascii_lowercase
        else:
            raise ValueError("Invalid complexity level. Choose from 'simple', 'medium', or 'strong'.")

        password = ''.join(random.choice(chars) for _ in range(length))
        return password

    def main(self):
        length = int(input("Enter the length of the password: "))
        complexity = input("Enter the complexity level (simple, medium, strong): ").lower()

        password = self.generate_password(length, complexity)
        print("Generated password:", password)


password = password_generate()
password.main()


