###Question 1
Team = input("Enter the winning team:")
#Allows user to type what the winning team was
MVP = input("Enter the MVP's name:")
#Allows user to input the MVP of this game
for i in range(5):
#Repeats the winner and MVP 5 times
print(Team)
print(MVP)
###Question 2
num1= float(input("Enter number 1: "))
#user inputs the frist number
num2= float(input("Enter number 2:" ))
#user inputs 2nd number to use for (1st number)^2nd number power
print("Number 1 to the Number 2 power equals", num1 ** num2)
#prints the sulution
###Question 3
l = [2,4,5,8,10,12,14,16,18,20]
#given, defines l as this list
print("The value of each item in the list",l,"multiplied by 100 is: ")
#explains what list is about to be printed
for i in l:
print(i*100)
#prints each number in the list * 100 until the list is complete
###Question 4
print("This code prints the odd numbers from 0 to 20")
#explains what list is about to be printed
for i in range(1,20,2):
#odd numbers so range starts with 1, ends at 19 (excludes 20) so 2nd number in range is 20, and every other number starting with 1 will be every odd number so interval is 2
print(i)
#prints the list starting at 1 and counting by 2 until 20
###Question 5
m = 2
b = 5
#defines variables in the function given y=mx+b
x = float(input("What is the x intercept?"))
#user selects what the x intercept of the function is to find the y intecept
y = (m * x) +b
#finds the y intercept of the function given inputted x intercept from user
print("For this function, when the x intercept is ...")
print("y-intercept is:", y) #y-intercept is: (value of y will be printed)
#tells the user what the y intercept is based on the x intercept used.
