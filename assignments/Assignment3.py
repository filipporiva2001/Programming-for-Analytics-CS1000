#-*- coding: utf-8 -*-
# homework assignment #3
# 5 questions worth 10 points each.
# Only the base installation of python is allowed
# do not use/import any extra/external libraries
# =============================================================================
# Question1 #1 #2 & #3 use the file clickstream.csv
# available in the assignment section of module #3
#
# This file contains a subset of click stream data from wikipedia. All of this
# data is for the page Star Trek IV The Voyage Home, a movie from 1986.
#
# The columns in the file are:
# Referrer/Source: Where the user came from
# Current page/Article: Where the user went. Since all of our data is on the page
# Star Trek IV, all of these values are the same.
# Type: How did the user get here.
# Link - Followed a link from inside wikipedia
# external - Came from an external site
# other - Came from wiki, but not via link - probably a search from
homepage
# Occurrences: How many times has this referrer/current occurred during the
# data capture window.
#
# Example
# Catherine_Hicks
# Star_Trek_IV:_The_Voyage_Home
# link
# 264
#
# Source was the Catherine Hicks page
# User followed a link to the Star Trek IV page
# This happened 264 times
#
# =============================================================================
# =============================================================================
# Question #1. In the click stream data how many times has the Star Trek IV page
# been referred by a source containing the word "Spock" or "Nimoy" (case
insensitive)?
#
# Basically go through each line of the file and if the source contains one
# of these words add the occurences value to your total. Print out the total number
of
# occurences
#
# Place all your code inside the cell definition below
# =============================================================================
#%% question 1 response here
# Switching directory to where the file is saved.
def checkSpockNimoy(): # Defining a function
total_count = 0 # Initialization
f = open("/Users/filipporiva/Documents/CS1000/ClickStream.csv", "r") # Open the
file in read mode
for lne in f: # Goes through each line of the file
lne = lne.strip('\n') # Remove newline character at the end of the line
addrlist = lne.split(",") # Split the line into a list
# Check if the first column (source) contains the word "Spock" or "Nimoy",
ignoring case sensitivity
if "spock" in addrlist[0].lower() or "nimoy" in addrlist[0].lower():
#converts all the words to lowercase
total_count += int(addrlist[3]) # Add the value from the fourth column
(occurrences) to `total_count`
f.close() # Close the file
print('The total number of times Star Trek IV was referred by a Spock or Nimoy
related page is:', total_count)
# Call the function to execute it
checkSpockNimoy()
# =============================================================================
# Question #2. In the click stream data, what page has referred to Star Trek IV
# the most? From a web standpoint, this would tell us where most of our
# web traffic is coming from. Essentially, which record has the greatest number
# of occurrences.
#
# Print out the source, type, and occurrences value for that record
#
# Place all your code inside the cell definition below
# =============================================================================
#%% question 2 response here
# This function reads the CLickStream.csv file and prints the source with the most
clicks
def checktraffic():
largest = 0 #initialization
f = open("/Users/filipporiva/Documents/CS1000/ClickStream.csv", "r") #open the
file in read mode
for lne in f: # Goes through each line of the file
lne = lne.strip('\n') # Remove newline character at the end of the line
addrlist = lne.split(",") # Split the line into a list
# Checking if the number of occurrences in the fourth column is greater than
the current `largest` value
if int(addrlist[3]) > largest:
largest = int(addrlist[3]) #if the current line has more occurences ,
update "largest" with this new value
source = addrlist[0] # Store the source (the first column) corresponding
to the largest occurrences.
typ = addrlist[2] # Store the type (the third column) of the source with
the largest occurrences.
f.close() #close the opened file
print("Source:",source,"Type:",typ,"Occurrences:" ,largest) #print the results
checktraffic() #call the function
#%%
# =============================================================================
#
# Question #3. Create a program to allow the user to enter their search term.
# Scan the click stream data and return the total number of occurrences.
# The user should be able to specify whether they want to search for a source
# or a type. Use the function structure below and complete the necessary code
#
# Functions must include getSearch, search, and main.
# parameters as already specified for those functions must remain. If you like
# of if you feel it necessary, you can add additional parameters or return
# values. It is left to you on deciding where/how to process the file
# operations open/read/close/etc.
#
# Place all your code inside the cell definition below
#
# =============================================================================
#%% question 3 response here. Complete the code
#find what term and type to search for
def get_search():
word = input("Enter your search term: ").strip().lower()
_type = input("Source or Type? (case-insensitive) ").strip().lower()
#Error code if input for search type is not "source" or "type"
while _type not in ["source", "type"]:
_type = input("Please enter 'source' or 'type': ").strip().lower()
return word, _type
#runs through each line of the clickstream file
def search(word, _type):
total_count = 0
# Open the file using full path
with open("/Users/filipporiva/Documents/CS1000/ClickStream.csv", "r") as f:
for line in f:
line = line.strip() # remove extra characters
columns = line.split(',') # Split by commas
#perform search for both types of searches
if _type == "source":
if word in columns[0].lower(): # Source is in column 0
total_count += int(columns[3]) # Count is in column 3
elif _type == "type":
if word in columns[2].lower(): # Type is in column 2
total_count += int(columns[3]) # Count is in column 3
return total_count
def main():
word, _type = get_search() #define variables word and type
within get_search()
total_count = search(word, _type) #defines total_count within
search() using parameters word, _type
print(f"The total number of times '{word}' was referenced by {_type} is
{total_count}") #prints with correct variables
#Run function
main()
#%%
# =============================================================================
# Question #4 # 5 use the file rand.csv. This file can be found in the assignment
# section for module #3
#
# rand.csv has one column that contains random numbers between
# 1 and 10000.
#
# =============================================================================
#%%
# =============================================================================
# Question #4.
# Read all the values of the rand.csv file and determine the minimum value,
# mean (average) value, and the maximum value.
#
# Functions must include minMax, mean, and main.
# parameters as already specified for those functions must remain. If you like
# of if you feel it necessary, you can add additional parameters or return
# values. It is left to you on deciding where/how to process the file
# operations open/read/close/etc.
#
# Place all your code inside the cell definition below.
#
# =============================================================================
#%% Question 4. complete the code.
def rand(): #defying rand function
f = open("/Users/filipporiva/Documents/CS1000/Rand.csv", "r") #open the file
rand = [] #create an empty list
for lne in f: #loop to go through each single line in the file
lne = lne.strip('\n')
rand.append(int(lne))
f.close
return rand #return the list
def minMax(mainlist):
# This function finds and returns the lowest number (min) and the greatest
number (max) in mainlist
minVal, maxVal = min(mainlist),max(mainlist)
return(minVal,maxVal)
def mean(mainlist): #this function finds the mean of mainlist using the mean
formula below
meanlist = (sum(mainlist)/len(mainlist))
return(meanlist)
def main():
mainlist = rand() #call the rand() function which reads the numbers from the csv
file and return them as a list
minv,maxv = minMax(mainlist) #call the minMax function and store the value in
minv, maxv
meanvalue = mean(mainlist) #call the mean function and store the value in
#meanvalue
print('The values range from',minv,'to',maxv)
print('the value of the mean is:', meanvalue)
main()
#%%
# =============================================================================
# Question #5. As well as the average there are two other measures of central
# tendency we use very frequently: median and mode.
#
# Median brief description from
# https://en.wikipedia.org/wiki/Median
#
#
# The median of a finite list of numbers is the "middle" number, when those
# numbers are listed in order from smallest to greatest.
# If the data set has an odd number of observations, the middle one is selected.
# For example, the following list of seven numbers,
# 1, 3, 3, 6, 7, 8, 9
# has the median of 6, which is the fourth value.
#
# A set of an even number of observations has no distinct middle value and the
# median is usually defined to be the arithmetic mean of the two middle values.
# For example, the data set
# 1, 2, 3, 4, 5, 6, 8, 9
# has a median value of 4.5, that is ( 4 + 5 ) / 2
#
##
# Mode brief description from
# https://en.wikipedia.org/wiki/Mode_(statistics)
#
# The mode of a sample is the element that occurs most often in the collection.
# For example, the mode of the sample
# [1, 3, 6, 6, 6, 6, 7, 7, 12, 12, 17] is 6.
# Given the list of data
# [1, 1, 2, 4, 4]
# its mode is not unique.
# A dataset, in such a case, is said to be bimodal,
# while a set with more than two modes may be described as multimodal.
#
# Read all the values from the rand.csv file and calcuate the median
# and mode
#
# Functions must include median, mode, and main.
# parameters as already specified for those functions must remain. If you like
# of if you feel it necessary, you can add additional parameters or return
# values. It is left to you on deciding where/how to process the file
# operations open/read/close/etc.
#
# Place all your code inside the cell definition below.
# =============================================================================
#%% Question 5. complete the code.
#find the median
def median(numbers):
# Sort the numbers
sorted_numbers = sorted(numbers)
n = len(sorted_numbers)
# If number of values is odd return middle value
if n % 2 == 1:
medVal = sorted_numbers[n // 2]
else:
# If even, return the average of 2 middle values
mid1 = sorted_numbers[n // 2 - 1]
mid2 = sorted_numbers[n // 2]
medVal = (mid1 + mid2) / 2
return medVal
# Function to calculate the mode
def mode(numbers):
frequency = {} # Dictionary to store frequencies of each number in the csv
# Count the frequency of each number in the
for num in numbers:
if num in frequency:
frequency[num] += 1
else:
frequency[num] = 1
# Find the maximum frequency aka mode
max_count = max(frequency.values())
# Find all numbers that have the maximum frequency if more than just 1
modeVal = [num for num, count in frequency.items() if count == max_count]
if len(modeVal) == 1:
return modeVal[0] # Return the mode if there's only one
else:
return modeVal # Return the list if there are multiple modes (bimodal or
multimodal)
# Function to read data from the CSV file
def read_data():
numbers = []
# Open file and read each line
with open("/Users/filipporiva/Documents/CS1000/Rand.csv", "r") as file:
for line in file:
# Assuming each line has a number, convert intagers to a list
numbers.append(int(line.strip()))
return numbers
# Main function
def main():
# Read data from file
numbers = read_data()
# find median and mode
me = median(numbers)
mo = mode(numbers)
# print results
print('The median value of the data set is:', me)
if len(mo)>1:
print('The modes of the dataset are:', mo)
else:
print('The mode of the dataset is:', mo)
# Run function
main()
#%%
