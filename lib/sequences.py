#!/usr/bin/env python3

def print_fibonacci(length):
    # Initialize the first two numbers in the Fibonacci sequence
    fib_sequence = [0, 1]

    # Check if the length is less than or equal to 0
    if length <= 0:
        print("Length should be greater than 0")
        return

    # If length is 1, print the first number in the sequence
    if length == 1:
        print(fib_sequence[0])
        return

    # Generate the Fibonacci sequence up to the given length
    for i in range(2, length):
        next_number = fib_sequence[i - 1] + fib_sequence[i - 2]
        fib_sequence.append(next_number)

    # Print the generated Fibonacci sequence
    print("Fibonacci sequence up to length", length, "is:")
    print(fib_sequence)

# Example usage:
length_to_generate = 10
print_fibonacci(length_to_generate)