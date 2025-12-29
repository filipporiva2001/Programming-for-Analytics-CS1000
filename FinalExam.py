# -*- coding: utf-8 -*-
# Filippo Riva
#
# =============================================================================
# Programming for Analytics – Final / Exam Coding Assignment
#
# This file contains solutions for Questions 1–5.
# Only existing code structures were used where required.
# External libraries are used ONLY where explicitly allowed (pandas).
# =============================================================================


# =============================================================================
# Question #1
#
# This program prompts the user for a sentence, then for a letter.
# It prints the number of times the letter occurs in the sentence.
# Case is ignored.
#
# Restrictions:
# - You must NOT use the count() method
# - You must use the provided for-loop structure
# =============================================================================
def search_for_letter(sentence, letter):
    occurrences = 0
    for l in sentence:
        if l.lower() == letter.lower():
            occurrences += 1
    return occurrences


def question1_main():
    s = input("Please enter a sentence: ")
    letter = input("Enter the letter you want to search for: ")
    cnt = search_for_letter(s, letter)
    print("The number of times the letter", letter, "occurs is", cnt)


question1_main()


# =============================================================================
# Question #2
#
# Using FINAL_ClickStream.csv and the pandas library:
# Print:
#   - Total number of rows
#   - Total number of columns
#   - Mean of Occurrences
#   - Standard deviation of Occurrences
#   - Minimum Occurrences value
#   - Maximum Occurrences value
# =============================================================================
import pandas as pd

def question2():
    df = pd.read_csv("FINAL_ClickStream.csv")

    print("ClickStream information:")
    print("Total number of rows:", df.shape[0])
    print("Total number of columns:", df.shape[1])
    print("Mean of occurrences:", df["Occurrences"].mean())
    print("Standard deviation of occurrences:", df["Occurrences"].std())
    print("Minimum value in occurrences:", df["Occurrences"].min())
    print("Maximum value in occurrences:", df["Occurrences"].max())


question2()


# =============================================================================
# Question #3
#
# Using the click stream data, find and print the 5 most frequent
# referring sources (based on largest Occurrences values).
#
# If there is a tie for 5th place, print all tied rows.
# Order does NOT matter.
# =============================================================================
def question3():
    df = pd.read_csv("FINAL_ClickStream.csv")

    top5 = df.nlargest(5, "Occurrences", keep="all")
    print("Top 5 referring sources:")
    print(top5)


question3()


# =============================================================================
# Question #4
#
# Implement a CashRegister class.
#
# Requirements:
# - start_transaction(): resets total to 0.00
# - scan_item(amount): adds amount to total
# - total(): returns total due
#
# Class methods must NOT print anything.
# Output must be handled in test code.
# =============================================================================
class CashRegister:
    def __init__(self):
        self.total_amount = 0.00

    def start_transaction(self):
        self.total_amount = 0.00

    def scan_item(self, amount):
        self.total_amount += amount

    def total(self):
        return self.total_amount


def question4_tests():
    cr1 = CashRegister()
    cr1.start_transaction()
    cr1.scan_item(4.00)
    cr1.scan_item(5.50)
    print("Total due is $%.2f" % cr1.total())

    cr2 = CashRegister()
    cr2.start_transaction()
    cr2.scan_item(2.75)
    cr2.scan_item(3.25)
    cr2.scan_item(1.50)
    print("Total due is $%.2f" % cr2.total())

    cr3 = CashRegister()
    cr3.start_transaction()
    cr3.scan_item(10.00)
    cr3.scan_item(3.99)
    cr3.scan_item(0.99)
    print("Total due is $%.2f" % cr3.total())


question4_tests()


# =============================================================================
# Question #5
#
# Automatic change dispenser.
#
# Prompt the user for a number from 0 to 99 (change due).
# Print the number of:
#   - quarters
#   - dimes
#   - nickels
#   - pennies
#
# Grammar rules:
# - Singular form if quantity is 1
# - Plural otherwise
# =============================================================================
def calculate_change(change):
    quarters = change // 25
    change = change % 25

    dimes = change // 10
    change = change % 10

    nickels = change // 5
    change = change % 5

    pennies = change

    print("Change due the customer is:")

    print("1 quarter" if quarters == 1 else str(quarters) + " quarters")
    print("1 dime" if dimes == 1 else str(dimes) + " dimes")
    print("1 nickel" if nickels == 1 else str(nickels) + " nickels")
    print("1 penny" if pennies == 1 else str(pennies) + " pennies")


def question5_main():
    change_due = int(input("Enter the amount of change due (0 to 99): "))
    calculate_change(change_due)


question5_main()


# =============================================================================
# Source Note:
# ChatGPT was used for assistance.
# =============================================================================
