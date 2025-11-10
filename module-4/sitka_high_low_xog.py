# Xavier Grunitzky
# Module 4.2 Assignment
# 11/9/25
# Make changes to existing high and low temperature program.

import csv
from datetime import datetime
from matplotlib import pyplot as plt

filename = 'sitka_weather_2018_simple.csv'

while True:
    #New code: Ask user for choice
    decision = input("Enter 'high', 'low', or 'exit': ").strip().lower()

    #New code: Exit the loop if user chooses to quit
    if decision == "exit":
        print("Exiting program...")
        break

    #New code: Validate input
    if decision not in ("high", "low"):
        print("Invalid choice. Please enter 'high', 'low', or 'exit'.")
        continue

    # Open and read the CSV file
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        dates, highs, lows = [], [], []

        for row in reader:
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            dates.append(current_date)

            #New code: Get data depending on user's choice
            if decision == "high":
                high = int(row[5])
                highs.append(high)
            elif decision == "low":
                low = int(row[6])
                lows.append(low)

    # New code:Plot the selected temperatures
    fig, ax = plt.subplots()

    if decision == "high":
        ax.plot(dates, highs, c='red')
        plt.title("Daily High Temperatures - 2018", fontsize=24)
    else:
        ax.plot(dates, lows, c='blue')
        plt.title("Daily Low Temperatures - 2018", fontsize=24)

    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()
