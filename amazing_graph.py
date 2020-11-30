import matplotlib.pyplot as plt
import numpy as np

"""
==============
Amazing graph
==============
Algorithm used:
        Take the smallest prime number (2)
        Convert it into binary (2 in binary is 10)
        Reverse the obtained binary number (reverse of 10 is 01 or 1)
        Convert the reversed binary number back to decimal number (1 in decimal is 1)
        Subtract the final number obtained from the starting prime number (2 - 1 = 1)
        Repeat the steps for a large list of primes
For example, prime number = 3
        binary(3) = 11
        reverse(11) = 11
        decimal(11) = 3
        3 - 3 = 0 (final result for the prime 3)
Next prime number is 5
        binary(5) = 101
        reverse(101) = 101
        decimal(101) = 5
        5 - 5 = 0 (final result for prime 5)
Repeat the steps for a large amount of primes (say for first 3245 primes
or prime numbers till the prime number 29989)
Plot the primes on the x axis and the corresponding resulting numbers on the y axis
"""

def decimal_to_binary(x):
        binary = ''
        while x > 0:
                rem = x % 2
                binary += str(rem)
                x //= 2

        output = int(binary[::-1])
        return output

def binary_to_decimal(x):
        decimal = 0
        count = 0
        while x > 0:
                rem = x % 10
                n = rem * (2 ** count)
                decimal += n
                x //= 10
                count += 1
                
        return decimal


def get_primes(x):
        list_of_primes = list(range(2, x))
        for i in list_of_primes:
                for j in list_of_primes:
                        if i != j and j % i == 0:
                                list_of_primes.remove(j)


        else:
                return list_of_primes

print('Please wait for 5 seconds...')
print('Collecting data to be plotted...')

n = 30000 # Do not set this number greater than 30000 as program will take more time to execute
primes = get_primes(n)

print('creating x axis...')
print('x values ready')
print('creating y axis')
print('y values ready')
print('Plotting the graph...')

y = []
for i in primes:
        binary = decimal_to_binary(i)
        reverse = str(binary)[::-1]
        decimal = binary_to_decimal(int(reverse))
        y.append(i - decimal)

plt.plot(primes, y, 'black')
plt.show()
        
                                
