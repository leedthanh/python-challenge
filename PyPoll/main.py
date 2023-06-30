import pandas as pd
from pathlib import Path

csv_path = Path('/Users/thanhle/GitHub/python-challenge/PyPoll/Resources/election_data.csv')

poll_df = pd.read_csv(csv_path)

poll_df.head()
print("Election Resullts")
print("----------------------------------")

total_vote_df = poll_df["Ballot ID"].nunique()

print("Total Votes:",total_vote_df)
print("----------------------------------")


