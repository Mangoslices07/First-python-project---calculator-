# helpers.py

import re

def parse_math_expression(user_input):

    # Regular expression to find basic math problems
    match = re.search(r'(\d+)\s*([+\-*/])\s*(\d+)', user_input)
    if match:
        num1, operator, num2 = match.groups()
        return int(num1), operator, int(num2)
    return None

def solve_math_problem(num1, operator, num2):
   
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        # Handle division by zero
        return "Oops! Division by zero isn't allowed." if num2 == 0 else num1 / num2
    return "I couldn't solve that. Can you try again?"