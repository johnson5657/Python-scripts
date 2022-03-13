import re

log = "balbalblbal p[3432432423] fdslfjdslkfjsd [1232] fdsfsdf[333]"
regex = r"\[(\d+)\]"  # regex to return string inside square brackets
result = re.search(regex, log)  # search the first match of a regex expression inside log string
result2 = re.findall(regex, log)  # return all matching occurences of regex inside a string

print(result)

print(re.search(r"A.*a", "Argentina"))
print(re.search(r"A.*a",
                "Azerbaijan"))  # notice that regex didn't match the entire string that is beacuse we didn't specifiy to check the entire string only the first match
print(re.search(r"^A.*a$",
                "Azerbaijan"))  # here we didn't get a match as we specifi we wanted the entire string to be matched

pattern = r"^[a-zA-Z_][a-zA-Z0-9_]*$"  # the following pattern will match a variable name that start with letter or _ and then have letters numbers and underscors until the end of the string

text = "Is this is a sentence?"
result = re.search(r"^[A-Z][a-z ]*[\.\?\!]$", text)

print(result)

################################################################################################################
# REGEX CAPTURE GROUPS
##############################################################################

#The capturing group catches regex expression and put it into a gourp in the example below we have two groups
#both will catch \w* with is alpha numerci characters
#The result.groups() will return us a tuple that have all the groups we capture using regex as elements inside the tuple
result = re.search(r"^(\w*), (\w*)$", "Lovelace, Ada")
print(result)
print(result.group())
# capturing group at position 0 result.group(0) will print the entire list of matches
print("This is the first regex expression group :"+result.group(1))
print("This is the second regex expression group :"+result.group(2))

##############################################################################
#Repetition Qualifiers
#######################################################################
#Using the curly brackets we can tell how much repetition we want to match
#in the example below we wants to match 5 characters
# notice we only got the ghost string as it matches 5 characters in  a raw it didn't include the a characters as it has whitespace after is which is not matching our regex
print(re.search(r"[a-zA-Z]{5}","a ghost"))

#Here we have more matches to our regex but the function will retrun only the first one as we used search and not findall
print(re.search(r"[a-zA-Z]{5}","a scary ghost"))
#findall will return all the maching values as a list
print(re.findall(r"[a-zA-Z]{5}","a scary ghost"))

#extracting function PID from a log file
def extract_pid(log):
    regex = r"\[(\d+)\]"
    result = re.search(regex,log)
    if result is None: # if we didn't any match to our regex string we returning an empty string
        return ""
    return result[1]


#notice we only see full words beacuse we add the \b the inidicate word boundries as such part of the APPEARED word wasn't presented as its also match our regex of 5 characters
print(re.findall(r"\b[a-zA-Z]{5}\b","a scary ghost appeared"))

#Another way to set the repition is with curly brackets and setting an upper limit
#the below example will match repetition of characters between 5 to 10 characters in a raw
print(re.findall(r"\w{5,10}","a scary ghost appeared"))

#here as we have no upper limit it will match words with 5 characters or higher as there is no upper limit
print(re.findall(r"\w{5,}","a scary ghost appeared and strawberries"))

#below we look for a pattern that start with a S and can be as high as 20 characters
#so we got the follwing matching  ['scary', 'st', 'strawberries']
print(re.findall(r"s\w{,20}","a scary ghost appeared and strawberries"))
######################################################################################################
#SPLITTING AND REPLACING
################################################################
#the split fucntion uses regex values to split the string notice that the regex value itself is not present in the result strings
print(re.split(r"[.?!]","One sentence.Another one? And the lastone!"))
#if we want to include the regex signs as well we need to a () brackets
print(re.split(r"([.?!])","One sentence.Another one? And the lastone!"))




import re
#Question 2
#The multi_vowel_words function returns all words with 3 or more consecutive vowels (a, e, i, o, u). Fill in the regular expression to do that.
def multi_vowel_words(text):
  pattern = r"\b(?=\w*[aioue]{3,})\w+\b"
  result = re.findall(pattern, text)
  return result

print(multi_vowel_words("Life is beautiful"))
# ['beautiful']



import re
def show_time_of_pid(line):
  pattern = r"\[\d+\]"
  result = re.search(pattern, line)
  return result

print(show_time_of_pid("Jul 6 14:01:23 computer.name CRON[29440]: USER (good_user)")) # Jul 6 14:01:23 pid:29440

print(show_time_of_pid("Jul 6 14:02:08 computer.name jam_tag=psim[29187]: (UUID:006)")) # Jul 6 14:02:08 pid:29187

print(show_time_of_pid("Jul 6 14:02:09 computer.name jam_tag=psim[29187]: (UUID:007)")) # Jul 6 14:02:09 pid:29187