sentence = "welcome to string methods"
print(sentence)

# REMOVE WHITESPACE
strip = sentence.strip()
print(strip)

# REMOVE LEFT SPACES
lstrip = sentence.lstrip()
print(sentence)

# REMOVE RIGHT SPACES
rstrip = sentence.rstrip()
print(rstrip)

# RETURN LIST, DELIMITER X
split = sentence.split('l')
print(split)

# CONVERT A LIST TO A STRING
# joint = sentence.join(t)
# print(joint)

# RETURN TRUE IF STRING STARTS WITH X
starts = sentence.startswith('w')
print(starts)

# RETURN TRUE IF STRING ENDS WITH X
ends = sentence.endswith('x')
print(ends)

# RETURN COPY, UPPERCASE ONLY
uppers = sentence.upper()
print(uppers)

# RETURN COPY, LOWERCASE ONLY
lowers = sentence.lower()
print(lowers)

# PUTS A STRING INTO SENTENCE CASE 
capitalize = sentence.capitalize()
print(capitalize)

# RETURNS THE STRING USING TITLE CASE
titled = sentence.title()
print(titled)

# RETURNS A NEW STRING WITH REPLACEMENTS
replace = sentence.replace("e","x") 
print(replace)

# RETURN THE LENGTH OF THE STRING
length = len(sentence)
print(length)

# RETURNS THE NUMBER OF OCCURANCES OF A CHARACTER
counts = sentence.count('m')
print(counts)

# RETURN THE INDEX OF A CHARACTER
indexing = sentence.index('c')
print(indexing)

# IN AND NOT IN SEARCHE STRINGS AND RETURN TRUE OR FALSE
exists01 = 'e' in sentence
print(exists01)

exists02 = 'a' not in sentence
print(exists02)

# CHECKS IF STRING IS DIGIT TYPE OR NOT
digit = sentence.isdigit()
print(digit)

# CHECKS IF STRING IS ALPHABETIC CHARACTER TYPE
letters = sentence.isalpha()
print(letters)
