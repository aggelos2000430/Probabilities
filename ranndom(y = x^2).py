import random
import math
import csv
import matplotlib.pyplot as plt

freq = {(0.01, 0.10): 0, (0.11, 0.20): 0, (0.21, 0.30): 0, (0.31, 0.40): 0, (0.41, 0.50): 0, (0.51, 0.60): 0, (0.61, 0.70): 0, (0.71, 0.80): 0, (0.81, 0.90): 0, (0.91, 1.0): 0}

for i in range(10000):
    y = math.pow(random.uniform(0, 1), 2)
    for range in freq.keys():
        if range[0] <= y <= range[1]:
            freq[range] += 1

with open('Random(y = x^2).csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Range', 'Frequency'])
        for roll, count in freq.items():
            writer.writerow([roll, count])

freq = {}
with open('Random(y = x^2).csv', newline='') as file:
    reader = csv.reader(file)
    next(reader)  # Skip header row
    for row in reader:
        freq[row[0]] = int(row[1])

x = [float(range_str[1:-1].split(',')[0]) for range_str in freq.keys()]
y = list(freq.values())

plt.plot(x, y)
plt.xlabel('Range')
plt.ylabel('Frequency')
plt.title('Random(y = x^2)')
plt.show()