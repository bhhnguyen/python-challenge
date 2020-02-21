import os
import csv

budget_csv = os.path.join("Resources", "budget_data.csv")

with open(budget_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    header = next(csvreader)
    count = 0
    totalMonths = 0
    total = 0
    totalDelta = 0
    increase = 0
    decrease = 0
    increaseMonth = ""
    decreaseMonth = ""
    started = False
    for row in csvreader:
        totalMonths = totalMonths + 1
        newAmount = int(row[1])
        total = total + newAmount
        if started:
            delta = newAmount - oldAmount
            totalDelta = totalDelta + delta
            if delta > increase:
                increase = delta
                increaseMonth = row[0]
            if delta < decrease:
                decrease = delta
                decreaseMonth = row[0]
        else:
            started = True
        oldAmount = newAmount
    with open("analysis_results.txt","w") as textfile:
        textfile.write("Financial Analysis\n")
        textfile.write("----------------------------\n")
        textfile.write(f"Total months: {totalMonths}\n")
        textfile.write(f"Total: ${total}\n")
        textfile.write(f"Average Change: {format(totalDelta/(totalMonths-1),'.2f')}\n")
        textfile.write(f"Greatest Increase in Profits: {increaseMonth} (${increase})\n")
        textfile.write(f"Greatest Decrease in Profits: {decreaseMonth} (${decrease})\n")
        textfile.write("----------------------------")
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total months: {totalMonths}")
    print(f"Total: ${total}")
    print(f"Average Change: {format(totalDelta/(totalMonths-1),'.2f')}")
    print(f"Greatest Increase in Profits: {increaseMonth} (${increase})")
    print(f"Greatest Decrease in Profits: {decreaseMonth} (${decrease})")
    print("----------------------------")