#Marco Villegas
#Date: 4/24/23

#Program 1
print("\n\nProgram 1")
print("Hello World")
#this program prints out message 'Hello World'


#Program 2
print("\n\nProgram 2")
what_is_your_name = input("What is your name? ")
print("Hello and welcome!", what_is_your_name)
#this program ask's for the user names and welcomes them 

#Program 3
print("\n\nProgram 3")
what_is_your_name = input("What is your name? ")
if what_is_your_name == 'Marco' or what_is_your_name == 'Likoudis':
    print("Hello and welcome:", what_is_your_name)
#this program ask's for the user name, if it is "Marco" or "Likoudis" you are
#allowed access if you enter anything else you are denied access
    

#Program 4
print("\n\nProgram 4")
radius = float(input("What is the radius of the circle?"))

pi = 3.14

radius_of_circle = (pi * radius**2)
print("The answer for the radius of the circle is")
print(radius_of_circle)
#this program ask's the user for a number and then it multiples that number by pi=3.14
#and the number given 'squared' to get the radius of a circle


#Program 5
print("\n\nProgram 5")
miles = int(input("What are the number of miles driven?"))
gallons = int(input("What are the number of gallons used?"))

mpg = miles / gallons 
print("Your car delivers ", '{:.2f}'.format(mpg), "miles per gallon of fuel.")
#this program calculates the miles per gallon of fuel used during a trip, it ask's
#the user for the number of miles and gallons used; finally, it then divides by
#both to get the answer


#Program 6
print("\n\nProgram 6")
fahrenheit = int(input("What are the degrees in Fahrenheit?"))

celsius_ans = (fahrenheit - 32)*5/9
print("After the conversion of Fahrenheit to Celsius you get an answer of", '{:.2f}'.format(celsius_ans))
#this program ask's the user for a number in Fahrenheit and then it goes through the formula
#(number given - 32)x5/9, which will give the user the conversion of Fahrenheit to Celsius


#Program 7
print("\n\nProgram 7")
start_day = int(input("Which day, 0-6, is your start date for your vacation?"))
length_of_stay = int(input("What is the length of your stay at this vacation?"))

ans = (length_of_stay + start_day) % 7
print("The day of your return will be on", ans)
#this program calculates the day of return, using 0-6, 0=sunday...6=saturday (a full week),
#and then it adds both numbers and with, the modulus, it gives out the remainder and lets you know
#on what day of the week you will return



