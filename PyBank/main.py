import csv

csvpath = "Resources/budget_data.csv"
#Define and set variables
profit = []
months = []
initial_profit = 0
monthly_changes = []
count = 0

print("Financial Analysis")

print("------------------------------------")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)
    
    for row in csvreader:
        #count number of rows
        count = count + 1
        #set months and profit as seperate lists
        months.append(row[0])
        profit.append(int(row[1]))
        profit2 = int(row[1])
        #Formula to calculate change in profit
        if initial_profit != 0:
            delta_profit = profit2 - initial_profit
            monthly_changes.append(int(delta_profit))
        initial_profit = profit2
    total_change = sum(monthly_changes)
    average_change = round((total_change/(count-1)),2)
    greatest_increase = max(monthly_changes)
    greatest_decrease = min(monthly_changes)
    greatest_increase_month = months[monthly_changes.index(greatest_increase)]
    greatest_decrease_month = months[monthly_changes.index(greatest_decrease)]
        
        

print(f"Total Months: {count}")
print(f"Total Profits: ${sum(profit)}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {greatest_increase_month} ${greatest_increase}")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} ${greatest_decrease}")

with open("output.txt", "w") as text_file:
    text_file.write("Financial Analysis\n")
    text_file.write("------------------------------------\n")
    text_file.write(f"Total Months: {count}\n")
    text_file.write(f"Total Profits: ${sum(profit)}\n")
    text_file.write(f"Average Change: ${average_change}\n")
    text_file.write(f"Greatest Increase in Profits: {greatest_increase_month} ${greatest_increase}\n")
    text_file.write(f"Greatest Decrease in Profits: {greatest_decrease_month} ${greatest_decrease}\n")


