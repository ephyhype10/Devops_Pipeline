
import ast

user_input = input("Enter a value: ")

result = ast.literal_eval(user_input)

print("Result:", result)
