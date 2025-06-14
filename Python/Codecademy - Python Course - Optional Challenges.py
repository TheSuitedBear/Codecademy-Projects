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