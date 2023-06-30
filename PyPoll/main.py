
import csv
from pathlib import Path

csv_path = Path('/Users/thanhle/GitHub/python-challenge/PyPoll/Resources/election_data.csv')
candidate_list = []
candidate_vote = {}
with open(csv_path, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    header = next(csvreader)
    total_vote = 0
    for row in csvreader:
        total_vote  +=1
        if row [2] not in  candidate_list:
            candidate_list.append(row[2])
            candidate_vote[row[2]] = 0
        candidate_vote[row[2]] += 1

    for candidate in candidate_vote:
        percent_vote = candidate_vote[candidate] / total_vote * 100

        print(f'{candidate}: {percent_vote}% {candidate_vote[candidate]}')

print(candidate_vote)
print(candidate_list)
print(total_vote)
