import os
import csv

election_csv = os.path.join("Resources", "election_data.csv")

with open(election_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    header = next(csvreader)
    voteDictionary = {}
    for row in csvreader:
        candidate = row[2]
        if(voteDictionary.get(candidate) == None):
            voteDictionary[candidate] = 0
        voteDictionary[candidate] += 1
    voteValues = voteDictionary.values()
    voteSum = sum(voteValues)
    with open("election_results.txt","w") as textfile:
        textfile.write("Election Results\n")
        textfile.write("----------------------------\n")
        textfile.write(f"Total Votes: {voteSum}\n")
        textfile.write("----------------------------\n")
        highestVotes = 0
        winner = ""
        for key in voteDictionary:
            votes = voteDictionary[key]
            if votes > highestVotes:
                highestVotes = votes
                winner = key
            textfile.write(f"{key}: {format((votes/voteSum)*100,'.2f')}% ({votes})\n")
        textfile.write("----------------------------\n")
        textfile.write(f"Winner: {winner}\n")
        textfile.write("----------------------------")
    print("Election Results")
    print("----------------------------")
    print(f"Total Votes: {voteSum}")
    print("----------------------------")
    for key in voteDictionary:
        votes = voteDictionary[key]
        print(f"{key}: {format((votes/voteSum)*100,'.2f')}% ({votes})")
    print("----------------------------")
    print(f"Winner: {winner}")
    print("----------------------------")