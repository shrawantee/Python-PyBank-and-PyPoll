## Challenge 1: PyBank

#* In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company. 
# [budget_data.csv](PyBank/Resources/budget_data.csv). 
# The dataset is composed of two columns: `Date` and `Profit/Losses`. 

#* Your task is to create a Python script that analyzes the records to calculate each of the following:
#       1.	The total number of months included in the dataset
#       2.	The total net amount of "Profit/Losses" over the entire period
#       3.	The average change in "Profit/Losses" between months over the entire period
#       4.	The greatest increase in profits (date and amount) over the entire period
#       5.	The greatest decrease in losses (date and amount) over the entire period
#* As an example, your analysis should look similar to the one below:

  #Financial Analysis
  #----------------------------
  #Total Months: 86
  #Total: $38382578
  #Average  Change: $-2315.12
  #Greatest Increase in Profits: Feb-2012 ($1926159)
  #Greatest Decrease in Profits: Sep-2013 ($-2196167)
 
#* In addition, your final script should both print the analysis to the terminal and export a text file with the results.
#-----------------------------------------------------------------------------------------------------------------------

# ----------------------------
#    SOLUTION
# ----------------------------

# Notes to self: The data file that is provided has 41 obeservations and that too for the year 2018. 
# The file has a header.
# The sample output shows that the greatest increase and decrease in profits happened in two different years. 
# But budget_data.csv file has only one year (2018) of monthly data. 
# I am not sure what the total number of months imply, YET. 
# Does it mean that the code needs to check for the unique number of months in 2018 (that would be redundant!) that has some financial information???
# Also, treat the second column as Profits/Loss, not revenue. Maybe consider renaming that column as profits. 
# We need to use git to submit this assignment!!!


# Objective 1: Import modules os and csv

import os
import csv

# Objective 2: Set the path for the CSV file in PyBankcsv

PyBankcsv = os.path.join("Resources","budget_data.csv")

# Objective 3: Create the lists to store data. 

profit = []
monthly_changes = []
date = []

# Initialize the variables as required.
 
count = 0
total_profit = 0
total_change_profits = 0
initial_profit = 0

# Open the CSV using the set path PyBankcsv

with open(PyBankcsv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    # Conducting the ask
    for row in csvreader:    
      # Use count to count the number months in this dataset
      count = count + 1 

      # Will need it when collecting the greatest increase and decrease in profits
      date.append(row[0])

      # Append the profit information & calculate the total profit
      profit.append(row[1])
      total_profit = total_profit + int(row[1])

      #Calculate the average change in profits from month to month. Then calulate the average change in profits
      final_profit = int(row[1])
      monthly_change_profits = final_profit - initial_profit

      #Store these monthly changes in a list
      monthly_changes.append(monthly_change_profits)

      total_change_profits = total_change_profits + monthly_change_profits
      initial_profit = final_profit

      #Calculate the average change in profits
      average_change_profits = (total_change_profits/count)
      
      #Find the max and min change in profits and the corresponding dates these changes were obeserved
      greatest_increase_profits = max(monthly_changes)
      greatest_decrease_profits = min(monthly_changes)

      increase_date = date[monthly_changes.index(greatest_increase_profits)]
      decrease_date = date[monthly_changes.index(greatest_decrease_profits)]
      
    print("----------------------------------------------------------")
    print("Financial Analysis")
    print("----------------------------------------------------------")
    print("Total Months: " + str(count))
    print("Total Profits: " + "$" + str(total_profit))
    print("Average Change: " + "$" + str(int(average_change_profits)))
    print("Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")")
    print("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits)+ ")")
    print("----------------------------------------------------------")

with open('financial_analysis.txt', 'w') as text:
    text.write("----------------------------------------------------------\n")
    text.write("  Financial Analysis"+ "\n")
    text.write("----------------------------------------------------------\n\n")
    text.write("    Total Months: " + str(count) + "\n")
    text.write("    Total Profits: " + "$" + str(total_profit) +"\n")
    text.write("    Average Change: " + '$' + str(int(average_change_profits)) + "\n")
    text.write("    Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")\n")
    text.write("    Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits) + ")\n")
    text.write("----------------------------------------------------------\n")

# Note to TA: The output does not look like the one provided in the HW instructions. 
# I believe the budget_data.csv file is not the same as one used to come up with the sample text. 
