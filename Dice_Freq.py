import random
import sys
import csv

print("τυχαίες ρίψεις ζαριού")

# Ένα λεξικό για το αρχείο
freq = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
for i in range(1000):
	roll = (random.randint(1, 6))
	freq[roll] += 1
with open('dice_freq.csv', 'w', newline='') as file:
	# Δημιουργία CSV αρχείου για έξοδο
	writer = csv.writer(file)
	# Εκτύπωση των αποτελεσμάτων στο CSV αρχείο
	writer.writerow(['Roll Value', 'Frequency'])
	for roll, count in freq.items():
		writer.writerow([roll, count])