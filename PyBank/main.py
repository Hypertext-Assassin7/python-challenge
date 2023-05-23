# Import libraries
import os
import csv

# Path to access csv file
budget_csv = os.path.join("PyBank", "Resources", "budget_data.csv")

# Initialize variables
total_months = 0
net_total_profit_losses = 0
prev_profit_losses = 0
change_profit_losses = []
greatest_increase = ["", 0]
greatest_decrease = ["", float('inf')]

# Open csv
with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

# Sum up total months and net profit/loss
    for row in csvreader:
        total_months += 1
        net_total_profit_losses += int(row[1])

# Calculate change in profit/loss
        if total_months > 1:
            change = int(row[1]) - prev_profit_losses
            change_profit_losses.append(change)

# Calculate greatest increase in profits
            if change > greatest_increase[1]:
                greatest_increase[0] = row[0]
                greatest_increase[1] = change

# Calculate greatest decrease in profits
            if change < greatest_decrease[1]:
                greatest_decrease[0] = row[0]
                greatest_decrease[1] = change

# Set the current profit/loss as previous for the next iteration
        prev_profit_losses = int(row[1])

# Calculate the average change in profit/loss
average_change = sum(change_profit_losses) / len(change_profit_losses)

# Print the results
print(f'Total Months: {total_months}')
print(f'Total: ${net_total_profit_losses}')
print(f'Average Change: ${average_change:.2f}')
print(f'Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})')
print(f'Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})')

# Save results to a text file
with open('poll_results.txt', 'w') as file:
    file.write(f'Total Months: {total_months}\n')
    file.write(f'Total: ${net_total_profit_losses}\n')
    file.write(f'Average Change: ${average_change:.2f}\n')
    file.write(f'Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n')
    file.write(f'Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n')