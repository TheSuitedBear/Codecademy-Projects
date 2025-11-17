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



# Takes an input and returns the number to the power of 10

def tenth_power(num):
  return num ** 10

print(tenth_power(1))
# 1 to the 10th power is 1
print(tenth_power(0))
# 0 to the 10th power is 0
print(tenth_power(2))
# 2 to the 10th power is 1024



# Takes an input and returns the square root of the input

def square_root(num):
  return num ** 0.5

print(square_root(16))
# Should return 4
print(square_root(100))
# Should return 10



# Calculates the average win rates based on how many games were won and lost

def win_percentage(wins, losses):
  total_games = wins + losses
  win_rate = 100 / total_games * wins
  return win_rate

print(win_percentage(5, 5))
# Should return 50
print(win_percentage(10, 0))
# Should return 100
print(win_percentage(17, 23))
# Should return 42.5



# Takes 2 numbers and returns the average

def average(num1, num2):
  combined = num1 + num2
  average_num = combined / 2
  return average_num

print(average(1, 100))
# The average of 1 and 100 is 50.5
print(average(1, -1))
# The average of 1 and -1 is 0

# Simplified version

def average_simple(num1, num2):
  return (num1 + num2) / 2

print(average_simple(5, 50))
# Should return 27.5



# Returns the remainder of 2 numbers, in which the first value was multipled by 2, and the second being divided by 2

def remainder(num1, num2):
  new_one = num1 * 2
  new_two = num2 / 2
  return int(new_one % new_two)

print(remainder(15, 14))
# Should return 2
print(remainder(9, 6))
# Should return 0



# Takes an input and prints the first 3 multiples of the input, then returns the 3rd multiple

def first_three_multiples(num):
  print(num * 1)
  print(num * 2)
  print(num * 3)
  return num * 3

first_three_multiples(10)
# Should print 10, 20, 30, and return 30
first_three_multiples(0)
# Should print 0, 0, 0, and return 0

# Alternate version

def first_three_multiples_alt(num):
  for i in range(1, 4):
    print(num * i)
    i += 1
  return num * 3

first_three_multiples_alt(9)



# Takes 2 values, one being the cost of a meal, and the other the percentage tip you'd like to leave, and the function calculates how much you would need to pay.

def tip(total, percentage):
  total_tip = (total * percentage) / 100
  return total_tip

print(tip(10, 25))
# Should print 2.5
print(tip(0, 100))
# Should print 0.0



# Recreates the iconic "Bond, James Bond" quote with any first and last name as an input

def introduction(first_name, last_name):
  return last_name + ", " + first_name + " " + last_name

print(introduction("James", "Bond"))
# Should print Bond, James Bond
print(introduction("Maya", "Angelou"))
# Should print Angelou, Maya Angelou
print(introduction("Callum", "Smith"))
# Should print Smith, Callum Smith


# Takes a name and age, and calculates how old they would be in dog years

def dog_years(name, age):
  dog_age = age * 7
  return name + ", you are " + str(dog_age) + " years old in dog years"

print(dog_years("Lola", 16))
# should print "Lola, you are 112 years old in dog years"
print(dog_years("Baby", 0))
# should print "Baby, you are 0 years old in dog years"



# Takes 4 numbers, adds the first 2 together, subtracts the final 2, then multiplies the results together and then gets the remainder of the total from the first value

def lots_of_math(a, b, c, d):
   a_b = a + b
   print(a_b)
   c_d = c - d
   print(c_d)
   total = a_b * c_d
   print(total)
   return total % a

print(lots_of_math(1, 2, 3, 4))
# should print 3, -1, -3, 0
print(lots_of_math(1, 1, 1, 1))
# should print 2, 0, 0, 0



# Counts each unique letter in a word/sentence and returns the final count, uppercase and lowercase are counted as seperate letters.

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

def unique_english_letters(word):
  letter_index = []
  count = 0
  for letter in word:
    if letter in letter_index:
      continue
    else:
      letter_index.append(letter)
      count += 1
  return count

print(unique_english_letters("mississippi"))
# should print 4
print(unique_english_letters("Apple"))
# should print 4



# Takes a string and a letter and returns a total of how many times that letter appears in the string.

def count_char_x(word, x):
  count = 0
  for letter in word:
    if letter.lower() == x.lower():
      count += 1
    else:
      continue
  return f"There is {count} instances of the letter {x} in this string!".format(count=count, x=x)

print(count_char_x("mississippi", "s"))
# should print "There is 4 instances of the letter s in this string!"
print(count_char_x("mississippi", "m"))
# should print "There is 1 instances of the letter m in this string!"



# Takes a word or string and returns the amount of times a certain amount of multiple characters appears, like "iss" in Mississippi.

def count_multi_char_x(word, x):
  split_string = word.split(x)
  return (len(split_string)-1)

print(count_multi_char_x("mississippi", "iss"))
# should print 2
print(count_multi_char_x("apple", "pp"))
# should print 1



# Takes a word, a starting letter, and an end letter and gives you a sliced string of the letters between the start and end, if neither letter exists in the string, it returns the whole word.

def substring_between_letters(word, start, end):
  starting_point = word.find(start)
  ending_point = word.find(end)
  if starting_point > -1 and ending_point > -1:
    return(word[starting_point+1:ending_point])
  else:
    return word

print(substring_between_letters("apple", "p", "e"))
# should print "pl"
print(substring_between_letters("apple", "p", "c"))
# should print "apple"



# Takes a string and a number, and returns True if all words in the sentence are equal to or larger in length to the number inputted.

def x_length_words(sentence, x):
  sliced_sentence = sentence.split(" ")
  for word in sliced_sentence:
    if (len(word)) >= x:
      continue
    else:
      return False
  return True

print(x_length_words("i like apples", 2))
# should print False
print(x_length_words("he likes apples", 2))
# should print True



# Function takes a greeting/sentence and a name and returns true if the name is within the sentence.

def check_for_name(sentence, name):
  split_sentence = sentence.split(" ")
  for word in split_sentence:
    if word.lower() == name.lower():
      return True
    else:
      continue
  return False

print(check_for_name("My name is Jamie", "Jamie"))
# should print True
print(check_for_name("My name is jamie", "Jamie"))
# should print True
print(check_for_name("My name is Samantha", "Jamie"))
# should print False

# This can also be simplified into one line

def check_for_name_simple(sentence, name):
  return name.lower() in sentence.lower()

print(check_for_name_simple("My name is Jamie", "Jamie"))
# should print True
print(check_for_name_simple("My name is jamie", "Jamie"))
# should print True
print(check_for_name_simple("My name is Samantha", "Jamie"))
# should print False



# Function takes a string and puts every other letter into a new string and returns it

def every_other_letter(word):
  every_other = ""
  for i in range(0, len(word), 2):
    every_other += word[i]
  return every_other

print(every_other_letter("Codecademy"))
# should print Cdcdm
print(every_other_letter("Hello world!"))
# should print Hlowrd
print(every_other_letter(""))
# should print



# Reverses a string and returns it

def reverse_string(word):
  reversed_string = ""
  for i in range(len(word)-1, -1, -1):
    reversed_string += word[i]
  return reversed_string

print(reverse_string("Codecademy"))
# should print ymedacedoC
print(reverse_string("Hello world!"))
# should print !dlrow olleH
print(reverse_string(""))
# should print



# Swaps the first letter of 2 words and returns the 2 words as a sentence

def make_spoonerism(word1, word2):
  new_word1 = word2[0] + word1[1:]
  new_word2 = word1[0] + word2[1:]
  new_sentence = new_word1 + " " + new_word2
  return new_sentence

print(make_spoonerism("Codecademy", "Learn"))
# should print Lodecademy Cearn
print(make_spoonerism("Hello", "world!"))
# should print wello Horld!
print(make_spoonerism("a", "b"))
# should print b a



# Keeps adding ! to a string if the string is under 20 characters, once the string is 20 characters or more, it is returned

def add_exclamation(word):
  while(len(word) < 20):
    word += "!"
  return word 

print(add_exclamation("Codecademy"))
# should print Codecademy!!!!!!!!!!
print(add_exclamation("Codecademy is the best place to learn"))
# should print Codecademy is the best place to learn



# Returns the sum of all the values in a dictionary.

def sum_values(my_dictionary):
  count = 0
  for i in my_dictionary.values():
    count += i
  return count

print(sum_values({"milk":5, "eggs":2, "flour": 3}))
# should print 10
print(sum_values({10:1, 100:2, 1000:3}))
# should print 6



# Returns the sum of values from keys that are even numbers.

def sum_even_keys(my_dictionary):
  total = 0
  for i in my_dictionary.keys():
    if i % 2 == 0:
      total += my_dictionary[i]
  return total

print(sum_even_keys({1:5, 2:2, 3:3}))
# should print 2
print(sum_even_keys({10:1, 100:2, 1000:3}))
# should print 6



# Adds 10 to each value in a dictionary.

def add_ten(my_dictionary):
  for i in my_dictionary.keys():
    my_dictionary[i] += 10
  return my_dictionary

print(add_ten({1:5, 2:2, 3:3}))
# should print {1:15, 2:12, 3:13}
print(add_ten({10:1, 100:2, 1000:3}))
# should print {10:11, 100:12, 1000:13}



# Returns a list of keys that are also values in other parts of a dictionary.

def values_that_are_keys(my_dictionary):
  total = []
  for value in my_dictionary.values():
    for key in my_dictionary.keys():
      if value == key:
        total.append(value)
  return total

print(values_that_are_keys({1:100, 2:1, 3:4, 4:10}))
# should print [1, 4]
print(values_that_are_keys({"a":"apple", "b":"a", "c":100}))
# should print ["a"]



# Iterates through a dictionary and returns the key with the largest value associated with it.

def max_key(my_dictionary):
  largest_key = float("-inf")
  largest_value = float("-inf")
  for key, value in my_dictionary.items():
    if value > largest_value:
      largest_key = key
      largest_value = value
  return largest_key

print(max_key({1:100, 2:1, 3:4, 4:10}))
# should print 1
print(max_key({"a":100, "b":10, "c":1000}))
# should print "c"