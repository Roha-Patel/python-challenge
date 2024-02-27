# Dependencies
import os
import csv

# specify the file to write from
election_csv = os.path.join ("Resources", "election_data.csv")

# declare variables for initialing values
total_votes = 0
candidate_votes = 0
won_candidate_votes = 0
winner = 0

# Lists to store data
candidate_list = []
voted_candidate_list = []
vote_count_list = []
percentage_list = []

# reading CSV file using csv module
with open("/Users/rohapatel/week3/workHere/PyPoll/Resources/election_data.csv") as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter = ",")
    # move pointer through header to start reading csv file
    csv_header = next(csvreader)

    

    # interate through rows 
    for row in csvreader:

        # store the data in lists
        candidate_list.append(row[2])
        

        # the total number of votes
        total_votes += 1
        
        # list of candidate, who received votes
        candidate = row[2]
        if candidate not in voted_candidate_list:
            voted_candidate_list.append(candidate)
        
    # calculate total number and percentage of votes to determine the winner
    for candidate_name in voted_candidate_list:

        candidate_votes = candidate_list.count(candidate_name)

        vote_percentage = round(((candidate_votes / total_votes)*100), 3)

        # store values
        vote_count_list.append(candidate_votes)
        percentage_list.append(vote_percentage)

        if candidate_votes > winner:
            winner = candidate_votes
            winner_candidate = candidate_name

        candidate_votes = 0

# print the results in the terminal
print(f'Election Results')
print(f'----------------------------')
print(f'Total Votes = {total_votes}')
print(f'----------------------------')
for (name, percentage, count) in zip(voted_candidate_list, percentage_list, vote_count_list):
    print(f'{name}: {percentage}% ({count})')
print(f'----------------------------')
print(f'Winner: {winner_candidate}')
print(f'----------------------------')

# path for the output in a text file
output_path = os.path.join("analysis", "election_data_analysis.txt")

# write the result in a text file
with open("/Users/rohapatel/week3/workHere/PyPoll/analysis/election_data_analysis.txt", 'w') as csvfile:
    csvfile.write(f'Election Results\n')
    csvfile.write(f'----------------------------\n')
    csvfile.write(f'Total Votes = {total_votes}\n')
    csvfile.write(f'----------------------------\n')
    for (name, percentage, count) in zip(voted_candidate_list, percentage_list, vote_count_list):
        csvfile.write(f'{name}: {percentage}% ({count})\n')
    csvfile.write(f'----------------------------\n')
    csvfile.write(f'Winner: {winner_candidate}\n')
    csvfile.write(f'----------------------------\n')
