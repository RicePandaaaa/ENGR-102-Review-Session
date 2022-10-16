"""
Sheldon Cooper's (of Big Bang Theory) favorite number is 73. One of his reasons is that 73 is a prime number
and there are 21 prime numbers between 1 and 73. A prime number is a number greater than 1 that is not
divisible by another number (the only even number that is a prime number is 2; all other prime numbers are
odd). Write the Python code to calculate and print the prime numbers between 1 and 73 (but not including
73). Your program will also need to count the prime numbers to see if this is really the 21th prime number.
"""

# Store the primes
primes = ["2"]

# Loop and make the primes
for num in range(3, 73, 2):
    # Flag for prime
    is_prime = True
    # Check if it's prime by dividing num by every prime
    for prime in primes:
        # Is divisible by another priime
        if num % int(prime) == 0:
            is_prime = False

    # Add the number if it is prime
    if is_prime:
        primes.append(str(num))

# Output
print(", ".join(primes))
print(f"There are {len(primes)} prime numbers from 1 to 73 but not including 73. Therefore, 73 being the 21st prime is {len(primes) == 20}.")