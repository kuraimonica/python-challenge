# Import the os module
import os
# Import Module for reading CSV Files
import csv

# Path to collect data from the Resource folder
election_data_csv = os.path.join('Resources', 'election_data.csv')

# Open and read the election_data.csv file
with open(election_data_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    # Skip the header
    header = next(csv_reader)
    
    # Variables
    votes = list(csv_reader)
    total_votes = len(votes)

# Create an empty dictionary for candidates
candidates = {}

# Loop through the votes list to get the total number of votes each candidate received
for row in votes:
    if row[2] not in candidates:
        candidates[row[2]] = 1
    else:
        candidates[row[2]] += 1

# Loop through each value in candidates to calculate the percentage of votes received by each candidate
for candidate in candidates:
    candidates[candidate] = [candidates[candidate], (candidates[candidate] / total_votes) * 100]

# Determine the winner using max() function
winner = max(candidates, key=lambda x: candidates[x][0])

# Print and export results
output = f"""
Election Results
-------------------------
Total Votes: {total_votes}
-------------------------
"""

# Adding candidate details to the output
for candidate, data in candidates.items():
    output += f"{candidate}: {data[1]:.3f}% ({data[0]})\n"

output += f"""
-------------------------
Winner: {winner}
-------------------------
"""

# Print output
print(output)

# Export results to text file
with open("Election_Results.txt", "w") as output_file:
    output_file.write(output)


