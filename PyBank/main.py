import pandas as pd
from pathlib import Path

csv_path = Path('/Users/thanhle/GitHub/python-challenge/PyBank/Resources/budget_data.csv')

budget_df = pd.read_csv(csv_path)

budget_df.head(10)

print("Financial Analysis")
print("-------------------------------")
average_change=[]
date = []
amount = []
net_total = []
total_months=[]
max_increase_row =[]

total_months = budget_df["Date"].nunique()


print("Total Month:",total_months)

net_total = budget_df["Profit/Losses"].sum()
print("Total: $", net_total)
budget_df["Profit/Losses_change"] = budget_df["Profit/Losses"].diff()
average_change = budget_df["Profit/Losses_change"].mean()
average_change_round = round(average_change, 2)

print("Average Change: $", average_change_round)

budget_df['Profit/Losses_Change'] = budget_df['Profit/Losses'].diff()
max_increase_index = budget_df['Profit/Losses_Change'].idxmax()

date = budget_df.loc[max_increase_index, 'Date']

amount = budget_df.loc[max_increase_index, 'Profit/Losses_Change']
#amount_round = round(amount,2)
print("Greatest increase in profits:", date , "($" , amount ,")")


budget_df['Profit/Losses_Change'] = budget_df['Profit/Losses'].diff()
max_decrease_index1 = budget_df['Profit/Losses_Change'].idxmin()
date1 = budget_df.loc[max_decrease_index1, 'Date']
amount1 = budget_df.loc[max_decrease_index1, 'Profit/Losses_Change']
print("Greatest decrease in profits:", date1 , "($" , amount1 ,")")



