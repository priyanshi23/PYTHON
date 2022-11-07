# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# noinspection PyListCreation
timeTable = []
#Monday
timeTable.append(["History", "Maths", "PE", "Computer Science", "Music"])

#Tuesday
timeTable.append(["English", "Maths", "Spanish", "Geography", "Art"])

#Wednesday
timeTable.append(["PE", "English", "Science", "Art", "PE"])

#Thursday
timeTable.append(["Maths", "English", "Philosophy", "Spanish", "Music"])

#Friday
timeTable.append(["Science", "Drama", "History", "Geography", "Science"])

day = input("Day of the week?").title()
period = int(input("Lesson Number(1to5):"))
while period < 1 or period > 5:
    period = int(input("Lesson Number(1to5):"))
    lesson = ""
    if day == "Monday":
        lesson = timeTable[0][period-1]
    elif day == "Tuesday":
        lesson = timeTable[1][period-1]
    elif day == "Wednesday":
        lesson = timeTable[2][period-1]
    elif day == "Thursday":
        lesson = timeTable[3][period-1]
    elif day == "Friday":
        lesson = timeTable[4][period-1]
    else:
        print("Not a valid week day!")
        lesson = timeTable[2][period-1]

        if lesson != "":
            print("On" + day + ",lesson " + str(period) + " you have " + lesson + " .")
