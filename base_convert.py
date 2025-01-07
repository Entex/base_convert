#!/usr/bin/env python3
import sys

# Define the character set for bases up to 64
BASE_CHARS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz+/"

def base_to_decimal(value, base_from):
    """Converts a number from a given base to decimal."""
    decimal_value = 0
    for digit in value:
        decimal_value = decimal_value * base_from + BASE_CHARS.index(digit)
    return decimal_value

def decimal_to_base(value, base_to):
    """Converts a decimal number to a given base."""
    if value == 0:
        return BASE_CHARS[0]
    result = ""
    while value > 0:
        result = BASE_CHARS[value % base_to] + result
        value //= base_to
    return result

def base_convert(base_from, base_to, value):
    """Converts a value from one base to another."""
    # Convert to decimal first
    decimal_value = base_to_decimal(value, base_from)
    # Convert decimal to target base
    return decimal_to_base(decimal_value, base_to)

def print_help():
    """Prints the help message."""
    help_message = """
Base Convert - A Python script to convert numbers between bases 2 - 64.

Usage:
    base_convert [BaseFrom] [BaseTo] [value]
    
    - BaseFrom: The base of the input value (integer between 2 and 64).
    - BaseTo: The base to convert the input value to (integer between 2 and 64), or 'all' to display all bases.
    - value: The value to convert (must be valid in the BaseFrom system).

Examples:
    Convert a decimal number to binary:
        python base_convert.py 10 2 1234
        Output: 10011010010

    Convert a base-16 number to base-64:
        python base_convert.py 16 64 1A3F
        Output: 1e/

    Display the value in all bases from 2 to 64:
        python base_convert.py 10 all 1234

Notes:
    - Bases must be between 2 and 64 (inclusive).
    - Input value must only use valid characters for the specified base.

    """
    print(help_message)

def main():
    if len(sys.argv) == 2 and sys.argv[1] in {"--help", "-h"}:
        print_help()
        return

    if len(sys.argv) != 4:
        print("Invalid arguments. Use --help or -h for usage information.")
        return

    try:
        base_from = int(sys.argv[1])
        base_to = sys.argv[2]  # Could be an integer or "all"
        value = sys.argv[3]

        if not (2 <= base_from <= 64):
            raise ValueError("BaseFrom must be between 2 and 64.")

        # Validate the input value
        for char in value:
            if char not in BASE_CHARS[:base_from]:
                raise ValueError(f"Invalid character '{char}' for base {base_from}.")

        # Convert to decimal
        decimal_value = base_to_decimal(value, base_from)

        if base_to.lower() == "all":
            # Print the converted value in all bases from 2 to 64
            print(f"Value {value} in base {base_from} converted to all bases:")
            for b in range(2, 65):
                converted_value = decimal_to_base(decimal_value, b)
                print(f"Base {b:2}: {converted_value}")
        else:
            # Convert to the specified base
            base_to = int(base_to)
            if not (2 <= base_to <= 64):
                raise ValueError("BaseTo must be between 2 and 64.")
            converted_value = decimal_to_base(decimal_value, base_to)
            print(converted_value)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
