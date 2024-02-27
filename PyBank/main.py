# Dependencies
import os
import csv

# specify the file to write from
budget_data_csv = os.path.join ("Resources", "budget_data.csv")

# declare variables for initialing values
months = 0
net_total = 0
first_profit = 0
total_change = 0
average_changes = 0
period = 0

# Lists to store data
month_list = []
profit_loss_list = []
changes = []
greatest_increase = {"date": "", "amount":0}
greatest_decrease = {"date": "", "amount":0}


# reading CSV file using csv module
with open("/Users/rohapatel/week3/workHere/PyBank/Resources/budget_data.csv") as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter = ",")
    # move pointer through header to start reading csv file
    csv_header = next(csvreader)

    

    # interate through rows 
    for row in csvreader:

        # store the data in lists
        month_list.append(row[0])
        profit_loss = int(row[1])
        profit_loss_list.append(profit_loss)

        # the net total amount of "Profit/Losses" over the entire period
        net_total += profit_loss
        
        # not having a value to compare change
        if first_profit != 0:

            average_changes = profit_loss - first_profit
            changes.append(average_changes)

            total_change += average_changes

        first_profit = profit_loss

        # calculate the greatest increase in profit
        if average_changes > greatest_increase["amount"]:
            greatest_increase["amount"] = average_changes
            greatest_increase["date"] = row[0]

        # calculate the greatest decrease in profit
        if average_changes < greatest_decrease["amount"]:
            greatest_decrease["amount"] = average_changes
            greatest_decrease["date"] = row[0]

# calculate the average of profit changes
period = len(changes)
average_changes = round((total_change / period), 2)

# calculate the total number of months
months = len(month_list)

# print the results in the terminal
print(f'Financial Analysis')
print(f'----------------------------')
print(f'Total Months = {months}')
print(f'Total: ${net_total}')
print(f'Average Change: ${average_changes}')
print(f'Greatest Increase in Profits: {greatest_increase["date"]} (${greatest_increase["amount"]})')
print(f'Greatest decrease in Profits: {greatest_decrease["date"]} (${greatest_decrease["amount"]})')

# path for the output in a text file
output_path = os.path.join("analysis", "budget_data_analysis.txt")

# write the result in a text file
with open("/Users/rohapatel/week3/workHere/PyBank/analysis/budget_data_analysis.txt", 'w') as csvfile:
    csvfile.write(f'Financial Analysis\n')
    csvfile.write(f'----------------------------\n')
    csvfile.write(f'Total Months = {months}\n')
    csvfile.write(f'Total: ${net_total}\n')
    csvfile.write(f'Average Change: ${average_changes}\n')
    csvfile.write(f'Greatest Increase in Profits: {greatest_increase["date"]} (${greatest_increase["amount"]})\n')
    csvfile.write(f'Greatest decrease in Profits: {greatest_decrease["date"]} (${greatest_decrease["amount"]})\n')