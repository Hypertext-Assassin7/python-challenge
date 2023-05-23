# Imports libraries
import os
import csv

# Path to access csv file
election_csv = os.path.join("PyPoll", "Resources", "election_data.csv")

# Empty dictionary for candidates and their vote count
election_results = {}

# Initialize a variable for the total vote count
total_votes = 0

# Open the CSV
with open(election_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)

# Iterate through each row in the csv
    for row in csvreader:
        total_votes += 1
        if row[2] in election_results:
            election_results[row[2]] += 1
        else:
            election_results[row[2]] = 1

# List of candidates
candidates = list(election_results.keys())

# List of vote counts
votes_per_candidate = list(election_results.values())

# Calculate vote percentage for each candidate
vote_percentage = [votes/total_votes*100 for votes in votes_per_candidate]

# Find winning candidate
winner = candidates[votes_per_candidate.index(max(votes_per_candidate))]

# Print out the election results
print(f"Total Votes: {total_votes}")
for i in range(len(candidates)):
    print(f"{candidates[i]}: {vote_percentage[i]:.3f}% ({votes_per_candidate[i]})")
print(f"Winner: {winner}")

# Save results to a text file
with open('election_results.txt', 'w') as file:
    file.write(f"Total Votes: {total_votes}\n")
    for i in range(len(candidates)):
        file.write(f"{candidates[i]}: {vote_percentage[i]:.3f}% ({votes_per_candidate[i]})\n")
    file.write(f"Winner: {winner}\n")