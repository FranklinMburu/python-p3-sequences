#!/usr/bin/env python3

def print_fibonacci(length):
    """
    Generates a Fibonacci sequence up to the given length and prints it.

    Parameters:
    length (int): The number of Fibonacci numbers to generate.
    """
    # Base case: if length is 0 or negative, print an empty list
    if length <= 0:
        print([])
        return
    
    # Base case: if length is 1, print only the first Fibonacci number
    elif length == 1:
        print([0])
        return
    
    # Base case: if length is 2, print the first two Fibonacci numbers
    elif length == 2:
        print([0, 1])
        return
    
    # Initialize the Fibonacci sequence with the first two numbers
    fibonacci_sequence = [0, 1]
    
    # Generate Fibonacci numbers from the 3rd up to the nth
    for i in range(2, length):
        next_fib = fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2]
        fibonacci_sequence.append(next_fib)
    
    # Print the Fibonacci sequence
    print(fibonacci_sequence)
