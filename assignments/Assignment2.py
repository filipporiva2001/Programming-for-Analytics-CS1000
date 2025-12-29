# =============================================================================
# Question #1
# Given a list l, find the average of the values in the list.
# Print the average
#
# Place all of your code inside the cell definition below
#
# =============================================================================
# question 1 response here
l = [10,15,26,32,17,8,3,1,5,7,16,9]
average = sum(l)/len(l) #average formula sum of all numebr in the list / length of
the list
print(average)
#%%
# =============================================================================
# Question #2
#
# In bowling there is a handicap system that allows competition between
# individuals with different levels of skill/ability giving each an equal
# chance of winning.
#
# The formula for a bowling handicap uses:
# Basis score - For this exercise use 210
# Percentage factor - for this exercise use 90%
# Average Score - Average of recent scores
# When calculating drop any decimal places in result. Don't round.
#
# To calculate the handicap, subtract your average score from the basis
# score and multiply the result by the percentage factor. Again drop
# any fractional part - don't round.
#
# You are given a set of scores from recent games. Calcuate the handicap
# and update the print statement to print the handicap out.
#
# Basis score: 210
# Percentage factor: 90%
#
#
#
# Place all of your code inside the cell definition below
#
# =============================================================================
import math # importing the library math to have access to some functions
scores = [185,170,203,172,191,168]
average = sum(scores)/len(scores)
handicap = (210 - average) * .9 #for representing 90% I use 0.9, subtracting the
average score from basis score
handicap = int(handicap) #use int so I will get only the whole number and not the
#deicmals and I will not round
print("Your handicap is:", handicap)
# =============================================================================
#
# Question #3
#
#
# In statistics, the standard deviation is a calculation we use to determine
# how much variance exists in a set of values. If the standard deviation is
# small, it means the values are grouped tightly together. If it is large
# the values are more spread out.
#
# You calculate the standard deviation of a population by taking the square root
# of the average of the squared deviations from the average to the observation.
# The code below attempts to do this but has several errors. Correct them.
# If you need assistance understanding the calculation of a standard deviation
# here are some references.
#
# √(((Σ(X- μ))^2)/N)
#
# Σ - sum of what is inside parantheses
# μ - population mean
# X - each observed value
# N - number of observations
##
# https://en.wikipedia.org/wiki/Standard_deviation
# https://www.scribbr.com/statistics/standard-deviation/
##
# This code is attempting to calculate the POPULATION standard deviation.
# Correct the code in the cell below.
values = [8,2,17,16,3,-4,9,10,13]
avg = sum(values)/len(values) #removed the for loop and calculated the average of
the list normally
diff = 0 #iniziation of the difference
for i in values:
diff = diff + (i - avg) ** 2 #for every i it is calculating how far it is form
the mean
v = diff/len(values)
import math
sd = math.sqrt(v) #use the sqrt fucntion in the math library
print('The population standard deviation of the given list of values is:',sd)
# =============================================================================
# Questions #4 and #5 both use the file clickstream.csv
# available in the assignment section of module #2
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
# Question #4
#
# In the clickstream data, how many times has the page "Stark Trek IV The Voyage
Home"
# been referenced? (What is the total amount of the occurences column?)
#
# Write code to open the file, read the individual lines and total up the
# number of occurences and print out the total.
##
# Place all of your code inside the cell definition below
#
# =============================================================================
#%% question 4 response here
import os
os.chdir("/Users/filipporiva/Documents/CS1000") # switching directory to directory
in whch the file is saved
total_count = 0 #initialization
f = open("ClickStream.csv", "r") #open the file in read mode
for line in f: #loop goes through each line of the file, one at the time
line = line.strip() # Removes any extra spaces or newlines (make sure there are not unwanted cahraceters or spaces )
parts = line.split(",") # Splits the line into a list of values based on the
commas
total_count += int(parts[3]) # access the 4th value which refers to number of
occurences
print("Total number of clicks:", total_count)
f.close() #close the file
#%%
# =============================================================================
#
# Question #5
#
# Using the same click stream file, read in the file and replace any occurrence
# of the underscore character "_" with a space " " and write the data out to a
# new file called ClickStreamNew.txt.
##
# Place all of your code inside the cell definition below
#
# =============================================================================
#%% question 5 response here
import os
os.chdir("/Users/filipporiva/Documents/CS1000") # Change the directory to the
location of the file
f = open("ClickStream.csv", "r")# Open the files
new_file = open("ClickStreamNew.txt", "w") #opens a file in write mode
for line in f: #loop goes through every single line of the file
new_line = line.replace("_", " ") # Replace _ with space
new_file.write(new_line) # Write the new_line into the new file
f.close()# Close the files
new_file.close()
#Sources : ChatGPT was used to seek help to answer to question 5
