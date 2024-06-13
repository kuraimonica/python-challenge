#Import the os module
import os
#Import Module for reading CSV Files
import csv

# Path to collect data from the Resources folder
budget_data_csv = os.path.join('Resources','budget_data.csv')
output_file = os.path.join('Analysis','financial_analysis.txt')
#Define variables
total_months = 0
net_total = 0
changes = []
dates = []

#Open the csv file
with open(budget_data_csv, encoding='UTF-8') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    
    #Skip the header labels
    header = next(csv_reader)
          
    #loop through the rows in the stored file
    for row in csv_reader:
        
       #Count the total of months
        total_months += 1
        
        #Calculate the total net total
        net_total += int(row[1])
      
        
    #loop through the profits to obtain the change in profit/losses
        if dates:
            changes.append(int(row[1]) - prev_profit_loss)
        dates.append(row[0])
        prev_profit_loss = int(row[1])
        
#Calculate average changes in profit
         
average_change = sum(changes)/ len(changes)
greatest_increase = max(changes)
greatest_decrease = min(changes)
        
#Match greatest increase and decrease in profit to the proper date and index from max and min
greatest_increase_date = dates[changes.index(greatest_increase) + 1]
greatest_decrease_date = dates[changes.index(greatest_decrease) + 1]
        
# Print and export results
output = f"""
Financial Analysis
----------------------------
Total Months: {total_months}
Total: ${net_total}
Average Change: ${average_change:.2f}
Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})
Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})
"""

print(output)

with open("financial_analysis.txt", "w") as output_file:
    output_file.write(output)
   



        
        


   
