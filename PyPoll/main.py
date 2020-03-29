import os
import csv

#path to csv file
file = os.path.join('Resources', 'election_data.csv')

#read csv file & skip header
with open(file) as datafile:
    csvreader = csv.reader(datafile, delimiter=",")
    header = next(csvreader)

    #set variables
    candidates = []
    ind_votes = []
    num_votes = 0

    #loops through rows
    for row in csvreader:
        #counts rows in csv. num_votes variable set to 0 above so not to count header row.
        num_votes = num_votes + 1
        #reads candidate name from csv
        candidate = (row[2])
        #find if candidate has already been found and has votes 
        #then locate the candidate using index # 
        #then add to vote count
        if candidate in candidates:
            candidate_index = candidates.index(candidate)
            ind_votes[candidate_index] = ind_votes[candidate_index] + 1
        else:
            #if "candidate" was not found in "candidates", append list
            candidates.append(candidate)
            ind_votes.append(1)

#set variables
percent = []
most_votes = ind_votes[0]
max_index = 0

#loops through number range equal to number of candidates
for x in range(len(candidates)):
    #calculates and updates the vote percentage for candidates. x is the loop count through total number of candidates.
    vote_pct = round(ind_votes[x]/num_votes*100, 2)
    percent.append(vote_pct)
    
    if ind_votes[x] > most_votes:
        most_votes = ind_votes[x]
        max_index = x

winner = candidates[max_index] 

#Prints results
print('                ')
print('Election Results')
print('-------------------------')
print(f'Total Votes: {num_votes}')
print('-------------------------')
for x in range(len(candidates)):
    print(f'{candidates[x]}: {percent[x]}% ({ind_votes[x]})')
print('-------------------------')
print(f'Winner = {winner}')
print('-------------------------')

#output txt file
output_file = os.path.join("pypoll_results.txt")
with open(output_file, "w", newline="") as datafile:
    datafile.write('                \n')
    datafile.write('Election Results\n')
    datafile.write('-------------------------\n')
    datafile.write(f'Total Votes: {num_votes}\n')
    datafile.write('-------------------------\n')
    for x in range(len(candidates)):
        datafile.write(f'{candidates[x]} : {percent[x]}% ({ind_votes[x]})\n')
    datafile.write('-------------------------\n')
    datafile.write(f'Election winner: {winner.upper()}\n')
    datafile.write('-------------------------\n')
