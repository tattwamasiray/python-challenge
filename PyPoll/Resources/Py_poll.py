import os
import csv
csvpath = os.path.join("..", "Resources", "election_data.csv")

#Initialize variables
total_votes = 0
candidates = []
candidate_votes = []
# Open the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    print(csvreader)
    next(csvreader)# skip header row

    for row in csvreader:
        total_votes +=1
    #Get candidate name
    candidate_name = row[2]
    if candidate_name not in candidates:
        candidates.append(candidate_name)
        candidate_votes[candidate_name] = 0
    #Increment vote count for candidate
    candidate_votes[candidate_name] +=1]

#Initialize variable for winner
winner = ""
winner_votes = 0

print("Election Results")
print("------------------------")

#print total vote count
print(f"Total Votes: {total_votes}")
print("---------------------------")

#print each candidate's vote count and percentage of votes

for candidate in candidates:
    votes = candidate_votes[candidate]
    percentage = votes / total_votes * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})")
    #Winner
    if votes > winner_votes:
        winner = candidate
        winner_votes = votes
#print winner
print("--------------------")
print(f"Winner: {winner}")
print("-----------------------")




