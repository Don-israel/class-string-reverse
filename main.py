class Reverse:
    def __init__(self, s=""):
        self.s = s

    def reverse_string(self):
        return self.s[::-1]

# Take input from the user
user_input = input("Enter a word: ")

# Create an instance of the Reverse class with the user input
reverse_instance = Reverse(user_input)

# Print the reversed string
print("Reversed string:", reverse_instance.reverse_string())
