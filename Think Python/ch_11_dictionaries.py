eng2sp = {'one' : 'uno', 'two' : 'dos', 'three' : 'tres'}
eng2sp
eng2sp['one']
len(eng2sp)
'one' in eng2sp
vals = eng2sp.values() # key value pair
'uno' in vals

# hashtables 251

def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

d = {'a' : 1}
d.get('a', 0) # returns 1 (Value)/True
d.get('b', 0) # returns 0 (Default)/False

sample = "Accurate average letter frequencies can only be gleaned by analyzing a large amount of representative text"

''' ===== Excercize =====
    rewrite histogram using .get (eliminate if)
    
    get(key[, default])
    Return the value for key if key is in the dictionary, else default. If 
    default is not given, it defaults to None, so that this method never raises a KeyError.'''
    
def histogram(s):
    d = dict()
    for c in s.lower():
        d[c] = d.get(c, 0) + 1
    return d

def print_hist(h):
    for c in h:
        print(c, h[c])

def print_hist(h):
    for key in sorted(h):
        print(key, h[key])
        
def reverse_lookup(d, v):
    for k in d:
        if d[k] == v:
            return k
    raise LookUpError('value does not appear in the dictionary')

def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse

''' Memoization:
    In computing, memoization is an optimization technique used primarily to 
    speed up computer programs by storing the results of expensive function 
    calls and returning the cached result when the same inputs occur again.'''

known = {0:0, 1:1}

def fibonacci(n):
    if n in known:
        return known[n]
        
    res = fibonacci(n-1) + fibonacci(n-2)
    known[n] = res
    return res

''' ===== Ex 11-1 =====
    Write a function that reads the words in words.txt and stores them as keys
    in a dictionary'''

# echo "Accurate average letter frequencies can only be gleaned by analyzing a large amount of representative text" >> words.txt

def read_words():
    word_dictionary = {}
    word_list = open('words.txt').read().split(" ") # .split() does whitespace
    for word in word_list:
        word_dictionary[word.lower()] = word_dictionary.get(word.lower(), 0) + 1
    return word_dictionary
    
''' ===== Ex 11-2 =====
    Use dictionary method setdefault to write a more concise version of 
    invert_dict
    
    setdefault(key[, default])
    If key is in the dictionary, return its value. If not, insert key with a 
    value of default and return default. default defaults to None.
    ! Puts it in the dictionary for you'''
    
def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse