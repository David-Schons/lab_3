"""
Your Name
Date

Description of what this program does
"""
import sys


taxOwed = 0.0

earnedIncome = float(input("Enter the amount of income you earned in 2021: "))
if earnedIncome < 0:
	print("You made less than $0. Contact an accountant")
	sys.exit()

print("Are you married or single?")
maritalStatus = input("Type m for married and s for single: ")


#Ensures you have a valid marital status
while maritalStatus != "m" and maritalStatus != "s":
	print("you entered an invalid marital status")
	maritalStatus = input("Type m for married and s for single: ")




# Your code goes here

#The first bracket is easy to calculate, it is simply 10% of the total

bracketOne = earnedIncome * 0.1

if maritalStatus == "s" and earnedIncome <= 9950:
	print ("this year you owe", bracketOne, "in taxes")
if maritalStatus == "m" and earnedIncome <= 19900:
	print ("this year you owe", bracketOne, "in taxes")
#bracket two is more complicated, I have two tax single and married people differently now so i made
#two variables to keep track. Basically it is the max they can pay from the last tax bracket plus 12% of whatever is left over

bracketTwoS = 995 + (.12* (earnedIncome - 9950))
bracketTwoM = 1990 + (.12 * (earnedIncome - 19900))

if maritalStatus == "s" and earnedIncome <= 40525 and earnedIncome > 9950:
		print("this year you owe", bracketTwoS, "in taxes")
if maritalStatus == "m" and earnedIncome <= 81050 and earnedIncome > 19900 :
		print("this year you owe", bracketTwoM, "in taxes")
#Bracket three is the most complicated. I took the max of the first two brackets then added 22% of what is left over
bracketThreeS = 4664 + (.22* (earnedIncome - 50475))
bracketThreeM = 9328 + (.22* (earnedIncome- 81050))

if maritalStatus == "s" and earnedIncome <= 86375 and earnedIncome > 40525:
		print("this year you owe", bracketThreeS, "in taxes")
if maritalStatus == "m" and earnedIncome <= 172750 and earnedIncome > 81050:
		print("this year you owe", bracketThreeM, "in taxes")
# these two if statements are just cleaning up the code to make sure noone above the third bracket uses the calc.
if maritalStatus == "s" and earnedIncome > 86375:
	print("you make too much money for this calculator")

if maritalStatus == "m" and earnedIncome > 172750:
	print("you make too much money for this calculator")





