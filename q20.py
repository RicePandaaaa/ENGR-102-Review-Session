"""
Sheldon Cooper's (of Big Bang Theory) favorite number is 73. One of his reasons is that 73 is a prime number
and there are 21 prime numbers between 1 and 73. A prime number is a number greater than 1 that is not
divisible by another number (the only even number that is a prime number is 2; all other prime numbers are
odd). Write the Python code to calculate and print the prime numbers between 1 and 73 (but not including
73). Your program will also need to count the prime numbers to see if this is really the 21th prime number.
"""

# Store the primes
primes = ["2"]

# First loop goes from 3 (inclusive) to 73 (exclusive)
for num in range(3, 73, 2):
    # Flag for prime
    is_prime = True
    # Go through the primes
    for prime in primes:
        # Check for divisibility
        if num % int(prime) == 0:
            is_prime = False

    # Add the number to primes if it is prime
    if is_prime:
        primes.append(str(num))

# Output
print(", ".join(primes))
print(f"There are currently {len(primes)} prime numbers from 1 to 72, therefore, 73 being the 21st prime is {len(primes) == 20}.")

"""
example = ['a', 'b', 'c']

" | ".join(example) -> "a | b | c"
"""