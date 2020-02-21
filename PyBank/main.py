import os
import csv


#filepath
budget_csv = os.path.join("Resources", "budget_data.csv")

with open(budget_csv, 'r') as csvfile:
    #initialize
    csvreader = csv.reader(csvfile,delimiter=",")
    header = next(csvreader)
    totalMonths = 0
    total = 0
    totalDelta = 0
    increase = 0
    decrease = 0
    increaseMonth = ""
    decreaseMonth = ""
    started = False
    #iterate
    for row in csvreader:
        totalMonths = totalMonths + 1
        newAmount = int(row[1])
        total = total + newAmount
        #if this is the first row, don't worry about deltas
        if started:
            #calculate change
            delta = newAmount - oldAmount
            totalDelta = totalDelta + delta
            if delta > increase:
                increase = delta
                increaseMonth = row[0]
            if delta < decrease:
                decrease = delta
                decreaseMonth = row[0]
        else:
            #set started to True to start calcuating deltas
            started = True
        #keep track of previous amount for delta calculations
        oldAmount = newAmount
    #write a file
    with open("analysis_results.txt","w") as textfile:
        textfile.write("Financial Analysis\n")
        textfile.write("----------------------------\n")
        textfile.write(f"Total months: {totalMonths}\n")
        textfile.write(f"Total: ${total}\n")
        textfile.write(f"Average Change: {format(totalDelta/(totalMonths-1),'.2f')}\n")
        textfile.write(f"Greatest Increase in Profits: {increaseMonth} (${increase})\n")
        textfile.write(f"Greatest Decrease in Profits: {decreaseMonth} (${decrease})\n")
        textfile.write("----------------------------")
    #print out to terminal
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total months: {totalMonths}")
    print(f"Total: ${total}")
    print(f"Average Change: {format(totalDelta/(totalMonths-1),'.2f')}")
    print(f"Greatest Increase in Profits: {increaseMonth} (${increase})")
    print(f"Greatest Decrease in Profits: {decreaseMonth} (${decrease})")
    print("----------------------------")