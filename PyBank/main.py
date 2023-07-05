import csv
from pathlib import Path

csv_path = Path('/Users/thanhle/GitHub/python-challenge/PyBank/Resources/budget_data.csv')

# Open the CSV file and read the data
with open(csv_path, 'r', encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)  # Skip header row
    #set variables and list 
    total_months = 0
    net_total = 0
    profit_losses = []
    dates = []
    
    #run for loop to look into each column and add to the list created 
    for row in csvreader:
        profit_losses.append(int(row[1]))
        dates.append(row[0])
        #find the total month.  use int to add net total starting at row 1 which is the second column
        total_months += 1
        net_total += int(row[1])

    # Calculate average change
    
    total_change = 0
    previous_profit_loss = profit_losses[0]
    for i in range(1, len(profit_losses)):
        current_profit_loss = profit_losses[i]
        change = current_profit_loss - previous_profit_loss
        total_change += change
        previous_profit_loss = current_profit_loss

    average_change = total_change / (total_months - 1)
    average_change_round = round(average_change, 2)
    
    # Find greatest increase and decrease in profits
    max_increase = 0
    max_decrease = 0
    max_increase_index = 0
    max_decrease_index = 0
    # use loop and if function to find the greatest increase
    # and decrease.  used max but got different answer so i use if get the difference and set a condition.  match with the date using index.
    for i in range(1, len(profit_losses)):
        if profit_losses[i] - profit_losses[i-1] > max_increase:
            max_increase = profit_losses[i] - profit_losses[i-1]
            max_increase_index = i
        elif profit_losses[i] - profit_losses[i-1] < max_decrease:
            max_decrease = profit_losses[i] - profit_losses[i-1]
            max_decrease_index = i

    max_increase_date = dates[max_increase_index]
    max_increase_amount = profit_losses[max_increase_index] - profit_losses[max_increase_index - 1]
    max_decrease_date = dates[max_decrease_index]
    max_decrease_amount = profit_losses[max_decrease_index] - profit_losses[max_decrease_index - 1]

    # Print financial analysis results
    print("Financial Analysis")
    print("-------------------------------")
    print("Total Months:", total_months)
    print("Total: $", net_total)
    print("Average Change: $", average_change_round)
    print("Greatest increase in profits:", max_increase_date, "($", max_increase_amount, ")")
    print("Greatest decrease in profits:", max_decrease_date, "($", max_decrease_amount, ")")



