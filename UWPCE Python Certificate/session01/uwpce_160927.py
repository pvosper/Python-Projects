# wtf bbedit adding docs to projects makes no sense
# "trial by annoyance" - zed a. shaw

# dir() function lists the methods available on an object
# dir(a)

# tab = 4 spaces (auto-expand, default & language prefs)
# edit -> text options

# Python for You & Me
# http://pymbook.readthedocs.io/en/latest/

print("foo")

foo = 15
bar = foo

print(foo,bar)

foo = 20

print(foo,bar)

# ====== HOMEWORK =====
# Task 1: Set Up a Great Dev Environment
# Task 2: Python Pushups
# Task 3: Explore Errors

# ===== CodingBat code practice =====
# There are 8 sets of puzzles. Do as many as you can, but try to at least get 
# all the “Warmups” done.

# ===== Warmup 1 ======
# Warmup-1 > sleep_in 
# The parameter weekday is True if it is a weekday, and the parameter vacation 
# is True if we are on vacation. We sleep in if it is not a weekday or we're on 
# vacation. Return True if we sleep in.

def sleep_in(weekday, vacation):
  if not weekday or vacation:
    return True
  else:
    return False

# Warmup-1 > monkey_trouble 
# We have two monkeys, a and b, and the parameters a_smile and b_smile indicate 
# if each is smiling. We are in trouble if they are both smiling or if neither 
# of them is smiling. Return True if we are in trouble.

def monkey_trouble(a_smile, b_smile):
  if a_smile and b_smile:
    return True
  elif not a_smile and not b_smile:
    return True
  else:
    return False
    
# Warmup-1 > sum_double 
# Given two int values, return their sum. Unless the two values are the same, 
# then return double their sum.

def sum_double(a, b):
  if a == b:
    return 2 * (a + b)
  else:
    return a + b
    
# Warmup-1 > diff21 
# Given an int n, return the absolute difference between n and 21, except return
# double the absolute difference if n is over 21.

def diff21(n):
  if n > 21:
    return abs(2 * (21 - n))
  else:
    return abs(21 - n)

# Warmup-1 > parrot_trouble 
# We have a loud talking parrot. The "hour" parameter is the current hour time 
# in the range 0..23. We are in trouble if the parrot is talking and the hour is
# before 7 or after 20. Return True if we are in trouble.

def parrot_trouble(talking, hour):
  if talking == True and hour < 7:
    return True
  elif talking == True and hour > 20:
    return True
  else:
    return False

# Warmup-1 > makes10 
# Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.

def makes10(a, b):
  if a == 10 or b == 10:
    return True
  elif a + b == 10:
    return True
  else:
    return False

# Warmup-1 > near_hundred 
# Given an int n, return True if it is within 10 of 100 or 200. Note: abs(num) 
# computes the absolute value of a number.

def near_hundred(n):
  if abs(100 - n) <= 10:
    return True
  elif abs(200 - n) <= 10:
    return True
  else:
    return False
    
# Warmup-1 > pos_neg 
# Given 2 int values, return True if one is negative and one is positive. 
# Except if the parameter "negative" is True, then return True only if both 
# are negative.

def pos_neg(a, b, negative):
  if a < 0 and b > 0 and negative == False:
    return True
  elif a > 0 and b < 0 and negative == False:
    return True
  elif a < 0 and b < 0 and negative == True:
    return True
  else:
    return False

# Warmup-1 > not_string 
# Given a string, return a new string where "not " has been added to the front.
# However, if the string already begins with "not", return the string unchanged.

def not_string(str):
  if str[0:3] == "not":
    return str
  else:
    return "not " + str

# Warmup-1 > missing_char 
# Given a non-empty string and an int n, return a new string where the char at
# index n has been removed. The value of n will be a valid index of a char in
# the original string (i.e. n will be in the range 0..len(str)-1 inclusive).

def missing_char(str, n):
  return str[0:n] + str[n+1:len(str)]

# Warmup-1 > front_back 
# Given a string, return a new string where the first and last chars have been
# exchanged.

def front_back(str):
  if len(str) <= 1:
    return str
  else:
    return str[-1] + str[1:len(str)-1] + str[0]

# mid = str[1:len(str)-1]  # can be written as str[1:-1]
  
  # last + mid + first
#return str[len(str)-1] + mid + str[0]

# Warmup-1 > front3 
# Given a string, we'll say that the front is the first 3 chars of the string.
# If the string length is less than 3, the front is whatever is there. Return 
# a new string which is 3 copies of the front.
def front3(str):
  return str[0:3]*3

# ===== Warmup-2 =====
# Warmup-2 > string_times
# Given a string and a non-negative int n, return a larger string that is n 
# copies of the original string.
def string_times(str, n):
  return str*n
  
# Warmup-2 > front_times 
#Given a string and a non-negative int n, we'll say that the front of the
# string is the first 3 chars, or whatever is there if the string is less than
# length 3. Return n copies of the front;
def front_times(str, n):
  return str[0:3]*n

# Warmup-2 > string_bits 
# Given a string, return a new string made of every other char starting with
# the first, so "Hello" yields "Hlo"
def string_bits(str):
    newstr = ""
    for i in range(0,len(str),2): # range - start / end
        newstr = newstr + str[i]
    return newstr

Warmup-2 > string_splosion 
prev  |  next  |  chance
Given a non-empty string like "Code" return a string like "CCoCodCode".

string_splosion('Code') → 'CCoCodCode'
string_splosion('abc') → 'aababc'
string_splosion('ab') → 'aab'

def string_splosion(str):

Warmup-2 > last2 
prev  |  next  |  chance
Given a string, return the count of the number of times that a substring length 2 appears in the string and also as the last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end substring).

last2('hixxhi') → 1
last2('xaxxaxaxx') → 1
last2('axxxaaxx') → 2

def last2(str):

Warmup-2 > array_count9 
prev  |  next  |  chance
Given an array of ints, return the number of 9's in the array.

array_count9([1, 2, 9]) → 1
array_count9([1, 9, 9]) → 2
array_count9([1, 9, 9, 3, 9]) → 3

def array_count9(nums):

Warmup-2 > array_front9 
prev  |  next  |  chance
Given an array of ints, return True if one of the first 4 elements in the array is a 9. The array length may be less than 4.

array_front9([1, 2, 9, 3, 4]) → True
array_front9([1, 2, 3, 4, 9]) → False
array_front9([1, 2, 3, 4, 5]) → False

def array_front9(nums):

Warmup-2 > array123 
prev  |  next  |  chance
Given an array of ints, return True if .. 1, 2, 3, .. appears in the array somewhere.

array123([1, 1, 2, 3, 1]) → True
array123([1, 1, 2, 4, 1]) → False
array123([1, 1, 2, 1, 2, 3]) → True

def array123(nums):

Warmup-2 > string_match 
prev  |  next  |  chance
Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring. So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in the same place in both strings.

string_match('xxcaazz', 'xxbaaz') → 3
string_match('abc', 'abc') → 2
string_match('abc', 'axc') → 0

def string_match(a, b):


