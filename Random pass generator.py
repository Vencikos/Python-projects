import random

#A function do shuffle all the characters of a string

def shuffle(string):
  tempList = list(string)
  random.shuffle(tempList)
  return ''.join(tempList)

#Generate uppercase letter
uppercaseLetter1=chr(random.randint(65,90)) #Generate a random Uppercase letter (based on ASCII code)
uppercaseLetter2=chr(random.randint(65,90)) #Generate a random Uppercase letter (based on ASCII code)
uppercaseLetter3=chr(random.randint(65,90)) #Generate a random Uppercase letter (based on ASCII code)
uppercaseLetter4=chr(random.randint(65,90)) #Generate a random Uppercase letter (based on ASCII code)

#Generate lowercase letters
lowercaseLetter1=chr(random.randint(97,122)) #Generate a random Lowercase letter (based on ASCII code)
lowercaseLetter2=chr(random.randint(97,122)) #Generate a random Lowercase letter (based on ASCII code)
lowercaseLetter3=chr(random.randint(97,122)) #Generate a random Lowercase letter (based on ASCII code)
lowercaseLetter4=chr(random.randint(97,122)) #Generate a random Lowercase letter (based on ASCII code)

#Generate digits
digit1=chr(random.randint(48,57)) #Generate a random Digit (based on ASCII code)
digit2=chr(random.randint(48,57)) #Generate a random Digit (based on ASCII code)
digit3=chr(random.randint(48,57)) #Generate a random Digit (based on ASCII code)
digit4=chr(random.randint(48,57)) #Generate a random Digit (based on ASCII code)

#Generate punctuation sign
punc_sign1=chr(random.randint(33,152)) #Generate a random Punctuation sign (based on ASCII code)
punc_sign2=chr(random.randint(33,152)) #Generate a random Punctuation sign (based on ASCII code)
punc_sign3=chr(random.randint(33,152)) #Generate a random Punctuation sign (based on ASCII code)
punc_sign4=chr(random.randint(33,152)) #Generate a random Punctuation sign (based on ASCII code)

#Generate password using all the characters, in random order
password = uppercaseLetter1 + uppercaseLetter2 + uppercaseLetter3 + uppercaseLetter4 + lowercaseLetter1 + lowercaseLetter2 + lowercaseLetter3 + lowercaseLetter4 + digit1 + digit2 + digit3 + digit4 + punc_sign1 + punc_sign2 + punc_sign3 + punc_sign4
password = shuffle(password)

#Ouput
print(password)