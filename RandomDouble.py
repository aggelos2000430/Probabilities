import random
import csv

value = input('How many random numbers do you need?\n')
value = int(value)
freq = {(0.01, 0.1): 0, (0.11, 0.2): 0, (0.21, 0.3): 0, (0.31, 0.4): 0, (0.41, 0.5): 0, (0.51, 0.6): 0, (0.61, 0.7): 0, (0.71, 0.8): 0, (0.81, 0.9): 0, (0.91, 1.0): 0}

for i in range(value):
    roll = random.uniform(0, 1)
    for range in freq.keys():
        if range[0] <= roll <= range[1]:
            freq[range] += 1
            break

with open('RandomDouble.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Range', 'Frequency'])
    for roll, count in freq.items():
        writer.writerow([roll, count])
