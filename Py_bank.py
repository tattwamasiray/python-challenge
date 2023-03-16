import os
import csv

csv_path = os.path.join("/Users/tattwamasiray/Downloads/Tat classin activity/BootCamp _Homework/python-challenge/PyBank/Py_bank.py"/Resources/budget_data.csv)

with open(csv_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    print(csvreader)
    next(csvreader)# skip header row

    # Initialize variables
total_months = 0
net_total = 0
prev_profit = 0
monthly_changes = []
greatest_increase = ['',0]
greatest_decrease = ['',0]



    #Loop through each row in the csv file
for row in csvreader:
        #Count the number of months
        total_months +=1

        #Calculate the net total amount of "profit/Losses" over the entire period
        if prev_profit != 0:
            monthly_change = int(row[1]) - prev_profit
            monthly_changes.append(monthly_change)

        
            
           
            if monthly_change > greatest_increase[1]:
                greatest_increase[0] = row[0]
                greatest_increase[1] = monthly_change
                
                
                
            # Determine the greatest decrease in losses and the date of occurrence
            if monthly_change < greatest_decrease[1]:
                greatest_decrease[0] = row[0]
                greatest_decrease[1] = monthly_change

        prev_profit = int(row[1])

        average_change = sum(monthly_changes) / len(monthly_changes)

        #print the results
        print("Financial Analysis")
        print("---------------------------")
        print(f"Total Months: {total_months}")
        print(f"Total: ${net_total})")
        print(f"Average Change: ${round(average_change, 2)}")
        print(f"Greatest Increse in profits: {greatest_increase[0]} (${greatest_increase[1]})")
        print(f"Greatest Decrese in profits: {greatest_decrease[0]} (${greatest_decrease[1]})")

                                                                      
                                                                      
        
        

          



