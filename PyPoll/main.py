
import csv
from pathlib import Path

#create path
csv_path = Path('/Users/thanhle/GitHub/python-challenge/PyPoll/Resources/election_data.csv')
#create list and dictionaries set them to 0
candidate_list = []
candidate_vote = {}
line = ("-----------------------------------------")
header = ("Election Results")
space = (" ")
with open(csv_path, encoding='UTF-8') as csvfile: #open csv
    csvreader = csv.reader(csvfile, delimiter=",") #reader csv
    print(header)
    print(space)
    print(line)
    header = next(csvreader) #skip header
    total_vote = 0
    for row in csvreader:       #loop through row to tally total vote use append to add one to the list
        total_vote  +=1
        if row [2] not in  candidate_list:
            candidate_list.append(row[2])
            candidate_vote[row[2]] = 0
        candidate_vote[row[2]] += 1
    
    winner = " "
    max_vote = 0
    print(space)
    print("Total votes: " , total_vote)
    print(space)
    print(line)
    for candidate in candidate_vote: #loop through candidate and get their vote
        percent_vote = candidate_vote[candidate] / total_vote * 100 #function to find percent

        percent_vote = round(percent_vote,3)  #rounding to 3 digits
        print(f'{candidate}: {percent_vote}% ({candidate_vote[candidate]})') #print string
        
        if candidate_vote[candidate] > max_vote:  #use if function to find candidate with highest vote
            max_vote = candidate_vote[candidate]
            winner = candidate
    print(space)
    print(line)
print("winner is " ,winner)
print(space)
print(line)
