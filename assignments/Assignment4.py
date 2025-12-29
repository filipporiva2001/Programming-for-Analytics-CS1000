# -*- coding: utf-8 -*-
# Filippo Riva
# CS1000
# Fall 2024
#
# =============================================================================
# Homework Assignment #4 (Chapter 8 - Booleans)
# 5 questions worth 10 points each.
# Only base Python is allowed (no imports).
#
# Files used (update paths if needed):
#   - planets.txt
#   - students.txt
#   - clickstream.csv
# =============================================================================

PLANETS_PATH = "/Users/filipporiva/Documents/CS1000/planets.txt"
STUDENTS_PATH = "/Users/filipporiva/Documents/CS1000/students.txt"
CLICKSTREAM_PATH = "/Users/filipporiva/Documents/CS1000/clickstream.csv"


# =============================================================================
# Question #1
#
# In the game of Scrabble, players score points determined by the words they put
# on a board. Each letter is assigned a certain value, and the word score is the
# sum of the letter values.
#
# Write a program that allows the user to evaluate the score of any word.
# For this exercise:
#   - assume the value of any character is ord(character) - 97
#   - consider only the lowercase version of the given word (.lower())
#   - do NOT use real Scrabble tile values
#
# Your program must use a sentinel loop to allow the user to evaluate as many
# words as they would like, until they enter the word "quit".
# =============================================================================
def question1():
    while True:
        word = input('Enter a word (type "quit" to exit): ').strip()
        if word.lower() == "quit":
            break

        score = 0
        for ch in word.lower():
            score += ord(ch) - 97

        print("Your score is:", score)


# =============================================================================
# Question #2
#
# Write a program that reads a text file of planetary data, and uses a sentinel
# loop to let the user enter the names of planets and display the number of
# Earth days it takes for that planet to orbit the sun.
#
# The program should end when the user enters a blank name.
# If the planet is not found, display: "Planet not found."
# Users should be able to enter the planet in upper/lower/mixed case.
#
# planets.txt file contents are:
#   Mercury 88
#   Venus 225
#   Earth 365
#   Mars 687
#   Jupiter 4332
#   Saturn 10760
#   Uranus 30700
#   Neptune 60200
# =============================================================================
def question2():
    # Read file once and store data in a dictionary
    planet_days = {}

    f = open(PLANETS_PATH, "r", encoding="utf-8")
    for line in f:
        line = line.strip()
        if line == "":
            continue
        parts = line.split()
        if len(parts) >= 2:
            name = parts[0].lower()
            days = parts[1]
            planet_days[name] = days
    f.close()

    while True:
        planet = input("Enter the name of a planet (blank to quit): ").strip()
        if planet == "":
            break

        key = planet.lower()
        if key in planet_days:
            print(planet.title(), "takes", planet_days[key], "days to orbit the sun")
        else:
            print("Planet not found.")


# =============================================================================
# Question #3
#
# Using a while loop:
# Prompt the user for the best football team.
# If they answer with any response other than "chiefs", tell them they are incorrect.
# If they answer "chiefs", print a congratulatory message and exit the loop.
# =============================================================================
def question3():
    while True:
        team = input("Which is the best football team in the world? ").strip()
        if team.lower() == "chiefs":
            print("This is the right answer! Let's go Chiefs!")
            break
        else:
            print("Wrong answer! Try again")


# =============================================================================
# Question #4
#
# Students are trying to get into CS 3000 but space is limited.
# The students who want to get in are in the file students.txt
# This class only allows 15 students.
#
# Read the file students.txt and create a list of who is in the class.
# Stop adding students when total enrollment reaches 15.
# Print the list of students who have been enrolled.
# =============================================================================
def question4():
    students = []

    f = open(STUDENTS_PATH, "r", encoding="utf-8")
    for line in f:
        if len(students) >= 15:
            break
        name = line.strip()
        if name != "":
            students.append(name)
    f.close()

    print("This is the list of the students registered for CS 3000:\n")
    for s in students:
        print(s)


# =============================================================================
# Question #5 (uses clickstream.csv)
#
# Using the file clickstream.csv, read entries until you find a row where
# the number of occurrences is greater than 1000.
#
# When you hit this limit, print out the entire line where occurrences first
# exceeded 1000.
#
# Reminder of columns in clickstream.csv:
#   Source, Current Page, Type, Occurrences
# =============================================================================
def question5():
    f = open(CLICKSTREAM_PATH, "r", encoding="utf-8")

    for line in f:
        line_stripped = line.strip()
        if line_stripped == "":
            continue

        cols = line_stripped.split(",")

        # skip header if present
        if cols[0].lower() in ["referrer/source", "referrer", "source"]:
            continue

        if len(cols) < 4:
            continue

        try:
            occ = int(cols[3].strip())
        except:
            continue

        if occ > 1000:
            # print the full line (clean)
            print("First line where occurrences exceeded 1000:")
            print(cols[0].strip(), cols[1].strip(), cols[2].strip(), cols[3].strip())
            break

    f.close()


# =============================================================================
# RUN ALL QUESTIONS (comment out any you do not want to run)
# =============================================================================
def main():
    print("===== Question 1 =====")
    question1()
    print()

    print("===== Question 2 =====")
    question2()
    print()

    print("===== Question 3 =====")
    question3()
    print()

    print("===== Question 4 =====")
    question4()
    print()

    print("===== Question 5 =====")
    question5()
    print()


main()

# Source note:
# ChatGPT was used for help with questions 3, 4, and 5.
# In question 4, names are printed vertically for better visualization.
