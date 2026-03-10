#!/usr/bin/env python3
"""
Simple terminal calculator with an interactive REPL.
"""


def calculate(left_text, operator, right_text):
    """Parse operands and perform the requested operation."""
    try:
        left = float(left_text)
        right = float(right_text)
    except ValueError:
        return "Invalid number. Use format: <num> <op> <num>"

    if operator == "+":
        return left + right
    if operator == "-":
        return left - right
    if operator == "*":
        return left * right
    if operator == "/":
        if right == 0:
            return "Cannot divide by zero."
        return left / right
    return "Invalid operator. Use one of: + - * /"


def format_result(result):
    """Avoid trailing .0 for whole-number float results."""
    if isinstance(result, float) and result.is_integer():
        return str(int(result))
    return str(result)


def main():
    """Run the calculator REPL."""
    print("Enter expressions like: 2 + 2")
    print("Type 'exit' or 'quit' to leave.")

    while True:
        try:
            raw = input("> ").strip()
        except EOFError:
            print()
            break

        if not raw:
            continue

        if raw.lower() in {"exit", "quit"}:
            break

        parts = raw.split()
        if len(parts) != 3:
            print("Invalid format. Use: <num> <op> <num>")
            continue

        result = calculate(parts[0], parts[1], parts[2])
        print(format_result(result))


if __name__ == "__main__":
    main()
