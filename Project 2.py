#   Dylan Wearing
#   This code calculates the sample standard deviation of a 5 point data set
#   Need to import math to use square root function
import math
print("Hello, I am a code that can tell you the sample standard deviation of a data set of 5 points.\nYou will give me your inputs and I will calculate it for you.\n")
#   Get them to input their data points and store them
point1 = float(input("Type one of your data points and hit enter.\nDo this until you have entered all five of your data points.\n"))
point2 = float(input())
point3 = float(input())
point4 = float(input())
point5 = float(input())

#   Have to calculate the mean to find the standard deviation
mean = round((point1+point2+point3+point4+point5)/5,3)
print("Okay, the average/mean of your data set is " + str(mean))

#   You have to square the data point minus the mean (5 times) so I'll do that here
p1manipulated = math.pow((point1 - mean),2)
p2manipulated = math.pow((point2 - mean),2)
p3manipulated = math.pow((point3 - mean),2)
p4manipulated = math.pow((point4 - mean),2)
p5manipulated = math.pow((point5 - mean),2)
#   I will calculate the numerator inside the square root here
numerator = p1manipulated + p2manipulated + p3manipulated + p4manipulated + p5manipulated

#   This finds the standard deviation
standard_deviation = round(math.sqrt((numerator)/(4.0)),3)
print("The sample standard deviation of your data set is " + str(standard_deviation))

#   I used my graphing calculator to double check these and they work
#   You don't have to enter the data points from least to greatest or anything like that