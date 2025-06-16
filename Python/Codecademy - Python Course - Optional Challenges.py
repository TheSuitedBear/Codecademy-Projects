# PLEASE BE ADVISED
# Challenges entirely provided by Codeacademy
# All solutions provided are my own with no external tools used, nor with no hints used unless disclosed.

# Returns True if the sum of 2 numbers is NOT equal to 10

num1 = 6
num2 = 3

if num1 + num2 != 10:
    not_ten = True
else:
    not_ten = False
    
print("Is the sum of the numbers not equal to 10? " + str(not_ten))



# The sum of all bills is assigned to "total" which is then compared with the budget to see if it is overbudget, if so, then over_budget gets assigned True

budget = 2000

food_bill = 200
electricity_bill = 100
internet_bill = 60
rent = 1500

total = food_bill + electricity_bill + internet_bill + rent

if total > budget:
    over_budget = True
else:
    over_budget = False
    
print("Total: " + str(total))
print("Is it over budget? " + str(over_budget))



# Returns True if "base" to the power of "exponent" is greater than 5000

def large_power(base, exponent):
    if base ** exponent > 5000:
        return True
    else:
        return False
    
print(large_power(2, 13))
# Should result in True
print(large_power(2, 12))
# Should result in False



# Returns True if num1 is larger than num2 doubled.

def twice_as_large(num1, num2):
    if num1 > (num2 * 2):
        return True
    else:
        return False
    
print(twice_as_large(10, 5))
# Should result in False
print(twice_as_large(11, 5))
# Should result in True



# Returns True if "num" is divisible by 10

def divisible_by_ten(num):
    if (num % 10) == 0:
        return True
    else:
        return False
    
print(divisible_by_ten(20))
# Should result in True
print(divisible_by_ten(25))
# Should result in False



# Function takes 3 inputs, a number, and 2 "range" numbers, and then returns true or false if the first number is within the range of the other 2 numbers

def in_range(num, lower, upper):
  if num >= lower and num <= upper:
    return True
  else:
    return False

print(in_range(10, 10, 10))
# should print True
# First number is the number being checked, the second number is the lower value, and the third is the higher value.
print(in_range(5, 10, 20))
# should print False



# Checks if 2 names are identical and returns true if so, if not, then returns false

def same_name(your_name, my_name):
  if str(your_name) == str(my_name):
    return True
  else:
    return False
print(same_name("Colby", "Colby"))
# should print True
print(same_name("Tina", "Amber"))
# should print False



# A function which is an intentional contradiction, returning false no matter what, true cannot be achieved.

def always_false(num):
  if num > num or num < num:
    return True
  else:
    return False

print(always_false(0))
# should print False
print(always_false(-1))
# should print False
print(always_false(1))
# should print False



# A movie rating function which returns a response based on a number inputted between 1 - 10, I also added a response to any numbers outside of the listed range.

def movie_review(rating):
  if int(rating) <= 5 and int(rating) >= 1:
    return "Avoid at all costs!"
  elif int(rating) > 5 and int(rating) < 9:
    return "This one was fun."
  elif int(rating) >= 9 and int(rating) < 11:
    return "Outstanding!"
  else:
    return "Rating is outside regular parameters, the number should be between 1 and 10"

print(movie_review(9))
# should print "Outstanding!"
print(movie_review(4))
# should print "Avoid at all costs!"
print(movie_review(6))
# should print "This one was fun."



# Checks which number out of a series of 3 inputs is the largest number, if the top number is tied with another number, it returns "It's a tie!"

def max_num(num1, num2, num3):
  if num1 > num2 and num1 > num3:
    return num1
  elif num2 > num1 and num2 > num3:
    return num2
  elif num3 > num1 and num3 > num2:
    return num3
  else:
    return "It's a tie!"

print(max_num(-10, 0, 10))
# should print 10
print(max_num(-10, 5, -30))
# should print 5
print(max_num(-5, -10, -10))
# should print -5
print(max_num(2, 3, 3))
# should print "It's a tie!"