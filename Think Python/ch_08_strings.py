'''Think Python - Allen B Downey'''

#1 Takes a string as an argument and displays the letters backwards
def backwards(str):
    index = 1
    while index <= len(str):
        letter = str[len(str) - index]
        print(letter)
        index += 1

#2 Print _Make Way for Ducklings_ names in order & spelled correctly
prefixes = 'JKLMNOPQ'
suffix = 'ack'

for letter in prefixes:
    if letter == 'O' or letter == 'Q':
        print(letter + 'u' + suffix)
    else:
        print(letter + suffix)
        
#3 Given that fruit is a string, what does fruit[:] mean?
In [1]: fruit = 'fruit'

In [2]: fruit[:]
Out[2]: 'fruit'

#4 Find a given letter in string, starting at a given point
def find(word, letter, start):
    index = start
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1

#5 Count the number of times a letter appears in a string, starting at a given point
def count(word, letter, start = 0):
    count = 0
    for search_letter in word[start:]:
        if search_letter == letter:
            count += 1
    print(count)
    
count('rabbit','b',0)
count('rabbit','b',2)
count('rabbit','b',3)

# String Methods
word = 'banana'
new_word = word.upper()
new_word

word = 'banana'
index = word.find('a')
index

# The in Operator
def in_both(word1, word2):
    for letter in word1:
        if letter in word2:
            print(letter)

# Debugging
def is_reverse(word1, word2):
    if len(word1) != len(word2):
        return False
        
    i = 0
    j = len(word2)-1
    
    while j >= 0:
        print(i, j)
        if word1[i] != word2[j]:
            return False
        i += 1
        j -= 1
    
    return True

is_reverse('pots', 'stop')

# Exercise 8-1
# read

# Exercise 8-2 Count the number of a's in "banana"
def count_letters(word, letter):
    return word.count(letter)   # Invoke count on word

# Exercise 8-3 is_palindrome using [::-1]

word1 = 'banana'
for letter in word1[::-1]:
    print(letter)


def is_palindrome(word1):

    str = ""

    for letter in word1[::-1]:
        str = str + letter 
   
    if str == word1:
        return True
        
    return False
    
# Exercise 8-4

def any_lowercase(s):
    for c in s:
        if not c.islower():
            return False
        else:
            return True

# Exercise 8-5

def rotate_word(word, amount = 13):

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    str = ""

    for letter in word:
    
        if alphabet.find(letter) >= 0:

            index = alphabet.find(letter) + amount
    
            while index not in range(26):
                if index < 0:
                    index += 26
                else:
                    index -= 26
    
            str = str + alphabet[index]
        
        else:
            
            str = str + letter

    return str

rotate_word('Zntargvp sebz bhgfvqr arne pbeare')