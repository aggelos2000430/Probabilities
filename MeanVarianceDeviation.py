import random
import math
import matplotlib.pyplot as plt
import numpy as np

value = int(input("How many random numbers do you want to generate? "))

random_numbers = [random.randint(1, 100) for i in range(value)]

mean = sum(random_numbers) / value

variance = sum([((x - mean) ** 2) for x in random_numbers]) / value

std_dev = math.sqrt(variance)

# Create plot with mean as a line and standard deviation as shaded regions
x = np.arange(0, value, 1)
y = np.array(random_numbers)
plt.plot(x, y, 'o')
plt.axhline(y=mean, color='r', linestyle='-')
plt.fill_between(x, mean+std_dev, mean-std_dev, alpha=0.2)
plt.title("Random Numbers with Mean and Standard Deviation")
plt.xlabel("Index")
plt.ylabel("Value")
plt.show()

print("Random numbers: ", random_numbers)
print("Mean: ", mean)
print("Variance: ", variance)
print("Standard deviation: ", std_dev)

