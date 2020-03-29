import os
import csv

# Create the file path to import the budget_data csv file
file = os.path.join("Resources", "budget_data.csv")

# Declare varaibles for analysis
total_months = 0
total_profit = 0
greatest_inc = 0
greatest_inc_month = ""
greatest_dec = 0
greatest_dec_month = ""

# Track the profit/loss of prior month for the changes variable
prev_pl = 0

# A list of all pl changes from mo to mo
changes = []

#Open the file and read data with csv.reader: save header row
with open(file) as data:
    csvreader = csv.reader(data, delimiter = ",")
    header = next(csvreader)

    #Loop through each row in csv, store values in named variables
    for row in csvreader:
        date = row[0]
        pl = int(row[1])
        #add the current months pl to the total
        total_profit += pl
        # Add on to the count of total months
        total_months += 1
        # Sumbtract the previous months pl from the current month
        # If this is the first month, discard the value. If this is 
        # not the first month, append the change to the changes list.
        change = pl - prev_pl
        if total_months != 1:
            changes.append(change)
        # Compare the change from the current month to the greatest_inc
        # variable: if change is greater than greates_in, replace
        # greatest_inc with change and update greatest_inc month with
        # month from current row. If change is less than greatest_dec,
        # replace greatest_dec with change and update greatest_dec_month
        # with month from current row.
        if change > greatest_inc:
            greatest_inc = change
            greatest_inc_month = data
        if change < greatest_dec:
            greatest_dec = change
            greatest_dec_month = date
        #Replace prev_pl with pl for next loop
        prev_pl = pl

# Calculate average change by summing the changes list and dividing by
# the length of the list. Round to 2 decimals.
avg_change = round(sum(changes)/len(changes), 2)

# Folling line was deprecated due to clarity on instructions.
# monthly_avg_profit = int(round(total_profit/total_months, ))

# Create a string for printing to the counsole and saving as a text file
# that displays all calculations requested.
analysis = f"""
Total Profit: ${total_profit}
Total Months: {total_months}
Average Monthly Change: ${avg_change}
Greatest Increase: {greatest_inc_month}, ${greatest_inc}
Greatest Decrease: {greatest_dec_month}, ${greatest_inc}
"""
# Print analysis string
print(analysis)

#Create a text file using the final analysis
output_file = "output.txt"
with open(output_file, "w") as doc:
    doc.write(analysis)