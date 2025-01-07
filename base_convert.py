#!/usr/bin/env python3
import sys

BASE_CHARS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz+/"

def direct_base_conversion(value, base_from, base_to):
    """Directly convert a number from base_from to base_to."""
    if base_from < 2 or base_from > 64 or base_to < 2 or base_to > 64:
        raise ValueError("BaseFrom and BaseTo must be between 2 and 64.")

    # Convert from base_from to decimal-like representation (integer array)
    digits = [BASE_CHARS.index(d) for d in value]

    # Perform the conversion directly to base_to
    result = []
    while digits:
        remainder = 0
        new_digits = []
        for d in digits:
            combined = remainder * base_from + d
            new_digits.append(combined // base_to)
            remainder = combined % base_to
        result.append(remainder)
        digits = [d for d in new_digits if d != 0]  # Remove leading zeros

    # Convert result digits to characters
    return ''.join(BASE_CHARS[d] for d in reversed(result))

def print_help():
    """Prints the help message."""
    help_message = """
BaseConvert - A Python script to convert numbers between bases 2 and 64.

Usage:
    base_convert [BaseFrom] [BaseTo] [value]
    
    - BaseFrom: The base of the input value (integer between 2 and 64).
    - BaseTo: The base to convert the input value to (integer between 2 and 64), or 'all' to display all bases.
    - value: The value to convert (must be valid in the BaseFrom system).
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

        if base_to.lower() == "all":
            print(f"Value {value} in base {base_from} converted to all bases:")
            for b in range(2, 65):
                converted_value = direct_base_conversion(value, base_from, b)
                print(f"Base {b:2}: {converted_value}")
        else:
            base_to = int(base_to)
            if not (2 <= base_to <= 64):
                raise ValueError("BaseTo must be between 2 and 64.")
            converted_value = direct_base_conversion(value, base_from, base_to)
            print(converted_value)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
