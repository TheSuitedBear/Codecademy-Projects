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



# Takes a list and adds the lists length to the end of the list and returns it

def append_size(my_list):
  list_length = len(my_list)
  my_list.append(list_length)
  return my_list

print(append_size([23, 42, 108]))
# Should print [23, 42, 108, 3]



# Function takes a list, gets the sum of the last 2 values in the list, and adds it onto the end of the list, it then does this 2 more times before returning the list

def append_sum(added_list):
  for i in range(3):
    added_list.append(added_list[-1] + added_list[-2])
  return added_list

print(append_sum([1, 1, 2]))
# Should print [1, 1, 2, 3, 5, 8]
print(append_sum([1, 4, 9]))
# Should print [1, 4, 9, 13, 22, 35]



# This function compares 2 lists, if one list has more elements than the other, the last element of the longer list is returned, if both lists are equal, it returns list 1's last element.

def larger_list(my_list1, my_list2):
  if len(my_list1) > len(my_list2):
    return my_list1[-1]
  elif len(my_list2) > len(my_list1):
    return my_list2[-1]
  else:
    return my_list1[-1]

print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10]))
# Should print 5



# This function takes a list of numbers, and returns true if the specified number in "item" is in the list more than "n" times, otherwise it returns false.

def more_than_n(product_list, item, n):
  if product_list.count(item) > n:
    return True
  else:
    return False

print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))
# Should return True



# This function combines 2 seperate lists and then returns that combined list, after sorting in numerical order.

def combine_sort(my_list1, my_list2):
  new_list = my_list1 + my_list2
  return sorted(new_list)

print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))
# Should print [-10, 2, 2, 4, 5, 5, 10, 10]



# Checks how many numbers in a list of numbers are divisible by 10 without decimels, then returns the total number

def divisible_by_ten(nums):
  counter = 0
  for i in nums:
    if i % 10 == 0:
      counter += 1
    else:
      continue
  return counter

print(divisible_by_ten([20, 25, 30, 35, 40]))
# Should return 3



# Takes a list of names and appends a greeting to each individual to a list called "greetings", then returns the list

def add_greetings(names):
  greetings = []
  for i in names:
    greetings.append('Hello, ' + i)
  return greetings

print(add_greetings(["Owen", "Max", "Sophie"]))
# Should return ['Hello, Owen', 'Hello, Max', 'Hello, Sophie']



# Function goes through a list of numbers and for each even number at the start of the list it removes it until it reaches an odd number as its first number, in which case it returns the finalised list

def delete_starting_evens(my_list):
  while len(my_list) > 0 and my_list[0] % 2 == 0:
    my_list = my_list[1:]
  return my_list

print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
# Should print [11, 12, 15]
print(delete_starting_evens([4, 8, 10]))
# Should print []



# This function takes a list of numbers and adds all numbers with an odd index to a new list, because of the way indexes work, this would mean the 2nd number would be first, then the 4th, etc.

def odd_indices(my_list):
  new_list = []
  for i in range(1, len(my_list), 2):
    new_list.append(my_list[i])
  return new_list
  
print(odd_indices([4, 3, 7, 10, 11, -2]))
# Should print [3, 10, -2]



# Function takes 2 lists, the first being base numbers, and the second being a list of powers, the function iterates through each base, multiplying it to the power of each number in "powers", it does this with every number with every power.

def exponents(bases, powers):
  new_list = []
  for i in bases:
    for a in powers:
      new_list.append(i ** a)
  return new_list
  
print(exponents([2, 3, 4], [1, 2, 3]))
# Should return [2, 4, 8, 3, 9, 27, 4, 16, 64]
print(exponents([3, 5, 7, 9], [2, 4, 6, 8]))
# Should return [9, 81, 729, 6561, 25, 625, 15625, 390625, 49, 2401, 117649, 5764801, 81, 6561, 531441, 43046721]



# Function adds up the sum of 2 different lists and returns the list that has the higher total sum, if both lists are equal in value then it returns list 1

def larger_sum(lst1, lst2):
  total1 = 0
  total2 = 0
  for i in lst1:
    total1 = total1 + i
  for e in lst2:
    total2 = total2 + e
  if total1 > total2:
    return lst1
  elif total2 > total1:
    return lst2
  else:
    return lst1

print(larger_sum([1, 9, 5], [2, 3, 7]))
# Should return [1, 9, 5]

# More condesed version of the prior challenge using the sum() function
def large_sum_one_line(lst3, lst4):
  if sum(lst3) >= sum(lst4):
    return lst3
  else:
    return lst4

print(large_sum_one_line([5, 7, 4], [2, 4, 8]))
# Should return [5, 7, 4]



# Function takes a list as an input and adds the numbers to the total sum one at a time until either the list is finished or the number exceeds 9000 by any amount, in which case the total number is returned

def over_nine_thousand(lst):
  total = 0
  for i in lst:
    total += i
    if total > 9000:
      break
  return total

print(over_nine_thousand([8000, 900, 120, 5000]))
# Should return 9020



# A function that takes a list of numbers and returns the largest number from the list, this can be simplified with max() but for this challenge I was required to do it manually, a version using the max() function can be found below this solution

def max_num(nums):
  big_num = nums[0]
  for i in nums:
    if i > big_num:
      big_num = i
  return big_num

print(max_num([50, -10, 0, 75, 20]))
# Should return 75

# Condensed version with max()

def max_num_condense(nums):
  return max(nums)

print(max_num_condense([10, 20, 45, -50, 4, 60, 100, 25]))
# Should return 100



# Function takes 2 lists, compares each index on both lists one by one, and if the numbers of the same index match, it adds the index to a list called "index" and then returns the list at the end

def same_values(lst1, lst2):
  index = []
  for count in range(0, len(lst1)):
    if lst1[count] == lst2[count]:
      index.append(count)
  return index

print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))
# Should return [0, 2, 3]



# This function takes 2 lists, and checks whether a list 1 is the same as list 2 in reverse, it does this by checking each index vs the opposite index on list 2 by using a specific equation to ensure we are at the right index

def reversed_list(lst1, lst2):
  for i in range(len(lst1)):
    if lst1[i] != lst2[len(lst2) - 1 - i]:
      return False
  return True

print(reversed_list([1, 2, 3], [3, 2, 1]))
# Should return True
print(reversed_list([1, 5, 3], [3, 2, 1]))
# Should return False

# Simplified version of the code above

def reversed_list_simple(lst1, lst2):
  lst2_reverse = list(reversed(lst2))
  if lst1 != lst2_reverse:
    return False
  else:
    return True

print(reversed_list_simple([5, 6, 7], [7, 6, 5]))
# Should return True
print(reversed_list_simple([5, 6, 7], [7, 8, 5]))
# Should return False