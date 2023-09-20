import csv
import random

file_path = 'particpants_responses.csv'

participant_names = []

with open(file_path, 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        participant_names.append(row['Full Name'])
        
random.shuffle(participant_names)

pairs = []

for i in range(0, len(participant_names), 2):
    if i + 1 < len(participant_names):
        pairs.append((participant_names[i], participant_names[i + 1]))
    else:
        pairs.append((participant_names[i], "No partner available"))
        
for pair in pairs:
    print(f"Pair: {pair[0]} and {pair[1]}")