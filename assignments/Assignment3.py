# -*- coding: utf-8 -*-
# =============================================================================
# Programming for Analytics (CS1000)
# Homework Assignment #3
#
# This assignment contains 5 questions, worth 10 points each.
# Only the base installation of Python is allowed.
# Do NOT import or use any external libraries.
#
# Files used:
#   - ClickStream.csv  (Questions 1–3)
#   - Rand.csv         (Questions 4–5)
# =============================================================================


# =============================================================================
# FILE PATHS (update if needed)
# =============================================================================
CLICKSTREAM_PATH = "/Users/filipporiva/Documents/CS1000/ClickStream.csv"
RAND_PATH = "/Users/filipporiva/Documents/CS1000/Rand.csv"


# =============================================================================
# HELPER FUNCTIONS
# =============================================================================
def read_clickstream_rows(filepath):
    """
    Reads ClickStream.csv and returns a list of rows.
    Each row has the format:
        [source, current_page, type, occurrences]
    """
    rows = []
    f = open(filepath, "r", encoding="utf-8")

    for line in f:
        line = line.strip()
        if line == "":
            continue

        cols = line.split(",")

        # Skip header if present
        if cols[0].lower() in ["referrer/source", "referrer", "source"]:
            continue

        if len(cols) < 4:
            continue

        source = cols[0]
        current_page = cols[1]
        typ = cols[2]

        try:
            occurrences = int(cols[3])
        except:
            continue

        rows.append([source, current_page, typ, occurrences])

    f.close()
    return rows


def read_rand_numbers(filepath):
    """
    Reads Rand.csv (one number per line)
    and returns a list of integers.
    """
    numbers = []
    f = open(filepath, "r", encoding="utf-8")

    for line in f:
        line = line.strip()
        if line != "":
            numbers.append(int(line))

    f.close()
    return numbers


# =============================================================================
# QUESTION 1
# =============================================================================
"""
Question #1
-----------
In the click stream data, how many times has the Star Trek IV page
been referred by a source containing the word "Spock" or "Nimoy"
(case-insensitive)?

Go through each line of the file and if the source contains one of
these words, add the occurrences value to a running total.
Print the final total.
"""
def q1_spock_nimoy_total(filepath):
    rows = read_clickstream_rows(filepath)
    total = 0

    for row in rows:
        source = row[0].lower()
        occurrences = row[3]

        if "spock" in source or "nimoy" in source:
            total += occurrences

    return total


# =============================================================================
# QUESTION 2
# =============================================================================
"""
Question #2
-----------
In the click stream data, what page has referred to Star Trek IV the most?

Print:
  - Source
  - Type
  - Occurrences

This corresponds to the record with the greatest number of occurrences.
"""
def q2_most_referrals(filepath):
    rows = read_clickstream_rows(filepath)

    max_occurrences = -1
    max_source = ""
    max_type = ""

    for row in rows:
        source = row[0]
        typ = row[2]
        occurrences = row[3]

        if occurrences > max_occurrences:
            max_occurrences = occurrences
            max_source = source
            max_type = typ

    return max_source, max_type, max_occurrences


# =============================================================================
# QUESTION 3
# =============================================================================
"""
Question #3
-----------
Create a program that allows the user to enter a search term and specify
whether they want to search by source or type.

Scan the click stream data and return the total number of occurrences.

Required functions:
  - getSearch
  - search
  - main
"""
def getSearch():
    term = input("Enter your search term: ").strip().lower()
    category = input("Search Source or Type? ").strip().lower()

    while category not in ["source", "type"]:
        category = input("Please enter 'source' or 'type': ").strip().lower()

    return term, category


def search(filepath, term, category):
    rows = read_clickstream_rows(filepath)
    total = 0

    for row in rows:
        source = row[0].lower()
        typ = row[2].lower()
        occurrences = row[3]

        if category == "source" and term in source:
            total += occurrences
        elif category == "type" and term in typ:
            total += occurrences

    return total


def main_q3():
    term, category = getSearch()
    total = search(CLICKSTREAM_PATH, term, category)
    print(f"Total occurrences where {category} contains '{term}': {total}")


# =============================================================================
# QUESTION 4
# =============================================================================
"""
Question #4
-----------
Read all values from Rand.csv and determine:
  - Minimum value
  - Mean (average)
  - Maximum value

Required functions:
  - minMax
  - mean
  - main
"""
def minMax(numbers):
    return min(numbers), max(numbers)


def mean(numbers):
    return sum(numbers) / len(numbers)


def main_q4():
    numbers = read_rand_numbers(RAND_PATH)
    mn, mx = minMax(numbers)
    avg = mean(numbers)

    print("Minimum value:", mn)
    print("Maximum value:", mx)
    print("Mean value:", avg)


# =============================================================================
# QUESTION 5
# =============================================================================
"""
Question #5
-----------
Calculate two additional measures of central tendency:
  - Median
  - Mode

Required functions:
  - median
  - mode
  - main
"""
def median(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)

    if n % 2 == 1:
        return sorted_numbers[n // 2]
    else:
        mid1 = sorted_numbers[n // 2 - 1]
        mid2 = sorted_numbers[n // 2]
        return (mid1 + mid2) / 2


def mode(numbers):
    frequency = {}

    for num in numbers:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1

    max_count = max(frequency.values())
    modes = []

    for num in frequency:
        if frequency[num] == max_count:
            modes.append(num)

    if len(modes) == 1:
        return modes[0]
    return modes


def main_q5():
    numbers = read_rand_numbers(RAND_PATH)
    med = median(numbers)
    mo = mode(numbers)

    print("Median:", med)
    if type(mo) == list:
        print("Modes:", mo)
    else:
        print("Mode:", mo)


# =============================================================================
# MAIN EXECUTION
# =============================================================================
def main():
    print("===== QUESTION 1 =====")
    q1_total = q1_spock_nimoy_total(CLICKSTREAM_PATH)
    print("Total Spock/Nimoy referrals:", q1_total)
    print()

    print("===== QUESTION 2 =====")
    src, typ, occ = q2_most_referrals(CLICKSTREAM_PATH)
    print("Source:", src)
    print("Type:", typ)
    print("Occurrences:", occ)
    print()

    print("===== QUESTION 3 =====")
    main_q3()
    print()

    print("===== QUESTION 4 =====")
    main_q4()
    print()

    print("===== QUESTION 5 =====")
    main_q5()


main()
