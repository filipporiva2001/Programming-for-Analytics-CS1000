# -*- coding: utf-8 -*-
# Filippo Riva
# CS1000
# Fall 2024
#
# =============================================================================
# NOTES
# - Only base Python is used (no imports).
# - Update CLICKSTREAM_PATH if your file is stored somewhere else.
# =============================================================================

CLICKSTREAM_PATH = "/Users/filipporiva/Documents/CS1000/ClickStream.csv"


# =============================================================================
# Question #1
#
# Inside the for loop provided, evaluate the individual integers.
# If the integer is divisible by 3 print "Rock" rather than the integer.
# If the integer is divisible by 5 print "hurst" rather than the integer.
# If the integer is divisible by both 3 and 5 print "Rockhurst" rather than the integer.
#
# There should only be one thing printed for each integer:
#   - 1 prints 1
#   - 15 prints Rockhurst
#
# Place all of your code in the cell below.
# =============================================================================
def question1():
    for x in range(1, 31):
        if x % 3 == 0 and x % 5 == 0:
            print("Rockhurst")
        elif x % 3 == 0:
            print("Rock")
        elif x % 5 == 0:
            print("hurst")
        else:
            print(x)


# =============================================================================
# Question #2
#
# Prompt the user for a number between 5 and 50 (inclusive).
# If the user enters an invalid value, print an error message and end the program.
#
# You can assume the user only enters whole numbers (no try/except required).
#
# If the user enters a valid value calculate the sum of numbers 1 through the
# value entered, including the value entered.
# Example: if user enters 5 → sum = 1+2+3+4+5 = 15
#
# Use the code framework below.
# Functions must include calcSum and main.
# =============================================================================
def calcSum(uv):
    """
    Returns the summation from 1 through uv (inclusive).
    """
    total = 0
    for i in range(1, uv + 1):
        total += i
    return total


def question2_main():
    userVal = input("Enter an integer between 5 and 50 inclusive: ").strip()

    # assume whole numbers only, but still validate digit
    if not userVal.isdigit():
        print("Invalid input, must be a whole number.")
        return

    userVal = int(userVal)

    if userVal < 5 or userVal > 50:
        print("Out of range. Please enter a value between 5 and 50.")
        return

    result = calcSum(userVal)
    print(f"The summation of values from 1 to {userVal} is: {result}")


# =============================================================================
# Question #3
#
# Given a list of names in mixed case, write python code to change the values
# to proper/title case and print the list in sorted order by:
#   last name + first name (ascending)
#
# proper/title case:
#   first letter of each first and last name is uppercase,
#   remainder is lowercase.
#
# Example input:
#   ['George WASHINGTON','JoHn AdAmS','thomas jefferson','JAMES Madison']
#
# Output should be sorted by last name, then first name.
# =============================================================================
def question3():
    nameList = ["George WASHINGTON", "JoHn AdAmS", "thomas jefferson", "JAMES Madison"]

    formatted = []
    for name in nameList:
        proper = name.title()             # "George Washington"
        parts = proper.split(" ")         # ["George", "Washington"]
        last_first = parts[1] + " " + parts[0]  # "Washington George"
        formatted.append(last_first)

    formatted.sort()
    print(formatted)


# =============================================================================
# Question #4
#
# This code is supposed to generate email addresses for Rockhurst students.
# Student email addresses look like:
#   lastname + firstinitial @hawks.rockhurst.edu
# Example:
#   Matt Heinrich -> heinrichm@hawks.rockhurst.edu
#
# Correct the code by updating the existing code/functions.
# =============================================================================
def makeEmail(fname, lname):
    first_initial = fname[0].lower()
    last = lname.lower()
    email = last + first_initial + "@hawks.rockhurst.edu"
    return email


def question4_main():
    fName = input("Enter your first name: ").strip()
    lName = input("Enter your last name: ").strip()

    em = makeEmail(fName, lName)
    print("Your email address is:", em)


# =============================================================================
# Question #5 (uses ClickStream.csv)
#
# Using the click stream data, accumulate the number of occurrences based on
# the type field.
#
# Print out the type and the corresponding total occurrences for each type.
#
# Example data:
#   somePage,Star Trek IV,link,12
#   otherPage,Star Trek IV,link,14
#   google,Star Trek IV,external,15
#   yahoo,Star Trek IV,other,7
#
# Output (format not important, values are):
#   link 26
#   external 15
#   other 7
# =============================================================================
def question5():
    totals = {"link": 0, "external": 0, "other": 0}

    f = open(CLICKSTREAM_PATH, "r", encoding="utf-8")

    for line in f:
        line = line.strip()
        if line == "":
            continue

        cols = line.split(",")

        # skip header if present
        if cols[0].lower() in ["referrer/source", "referrer", "source"]:
            continue

        if len(cols) < 4:
            continue

        typ = cols[2].strip().lower()
        try:
            occ = int(cols[3].strip())
        except:
            continue

        if typ in totals:
            totals[typ] += occ

    f.close()

    print("link", totals["link"])
    print("external", totals["external"])
    print("other", totals["other"])


# =============================================================================
# RUN ALL QUESTIONS
# Comment out anything you do not want to run.
# =============================================================================
def main():
    print("===== Question 1 =====")
    question1()
    print()

    print("===== Question 2 =====")
    question2_main()
    print()

    print("===== Question 3 =====")
    question3()
    print()

    print("===== Question 4 =====")
    question4_main()
    print()

    print("===== Question 5 =====")
    question5()
    print()


main()

# ChatGPT was used to help answering question 2.
