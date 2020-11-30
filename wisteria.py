import matplotlib.pyplot as plt
import numpy as np

"""
==============
Wisteria
==============
Algorithm used:
        Take a number n (say 13)
        Find the product of non - zero digits in n (1*3 = 3)
        Subtract the obtained number from the starting number n (13 - 3 = 10)
        Repeat the steps for a large list of positive numbers
For example, for 25
        product_of_digits(25) = 2*5 = 10
        25 - 10 = 15 (final result for number 25)
For example, for 10125
        product_of_digits(10125) = 1*1*2*5 = 10 (only non zero numbers)
        10125 - 10 = 10110 (final result for number 10125)
Plot the numbers on the x axis and the corresponding resulting numbers on the y axis
"""

def wisteria(x):
        temp = x
        product_of_digits = 1
        while temp > 0:
                rem = temp % 10
                if rem == 0:
                        pass
                else:
                        product_of_digits *= rem
                temp //= 10
        output = x - product_of_digits
        return output

x = np.arange(0, 500, 1)
y = []
print('Please wait while we plot the graph...')
for i in x:
        y.append(wisteria(i))
print('Done')
plt.plot(x, y,'r+', linestyle = 'dotted', markeredgecolor = 'blue')
plt.title('Wisteria')
plt.show()

