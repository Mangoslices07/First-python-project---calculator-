# chatbot.py

from helpers import parse_math_expression, solve_math_problem


def baymax_greeting():
    """Greets the user."""
    return ("Hello! I’m Baymax, your calculator, How can I help you today?")


def baymax_response(user_input):
    """Generates a response based on user input."""

    parsed_expression = parse_math_expression(user_input)

    if parsed_expression:
        num1, operator, num2 = parsed_expression
        result = solve_math_problem(num1, operator, num2)
        return f"The result is: {result}"

    # Catch-all response for non-math related input
    return "I'm here to help with anything! Just ask me something."


def chat():
    """Main chat loop to interact with Baymax."""
    print(baymax_greeting())

    while True:
        user_input = input("> ")

        if user_input.lower() in ['bye', 'exit', 'quit','finish session','close']:
            print("Goodbye! Stay safe and healthy.")
            break

        response = baymax_response(user_input)
        print(response)


if __name__ == "__main__":
    chat()