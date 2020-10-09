# You are given a string of lowercase English letters. 
# First, remove all occurrences of its first letter, e.g. "abacaba" -> "bcb". 
# Then, return the longest prefix of the remaining string which doesn't contain two different letters. 
# The initial string is at least 5 and no more than 100000 characters long.

def remove_letter(s):
    to_remove = s[0]
    others = ""
    #store needed chars from 2nd element of string till the end as 1st needs to be removed
    for i in range (1, len(s)):
        if to_remove != s[i]:
            others += s[i]
    return others

def prefix(s_removed):
    # in first loop charwill always be the same as 0th element prefix
    prefix = s_removed[0]
    # now we need to match subsequent ones to the prefix
    for char in range(1, len(s_removed)):
        if prefix[0] == s_removed[char]:
            prefix += s_removed[char]
        else:
            break
    return prefix

s = input("Please insert the string that you want to conduct this experiment on: ")
s_removed = remove_letter(s)

print(prefix(s_removed))