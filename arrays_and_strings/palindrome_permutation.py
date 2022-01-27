# Given a string, write a function to check if it is a permutation of a palindrome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation is a rearrangmeent of letters. The palindrome does not need to be limited to just dictionary words. You can ignore casing and non-letter characters. 


# Time: O(n), Space: O(n)
def pali(string):
    s = string.replace(" ", "")
    obj = {}
    for char in s:
        if char not in obj:
            obj[char] = 1
        else:
            obj[char] += 1
    one_odd = 0
    for i, v in obj.items():
        if v % 2 == 1:
            one_odd += 1
    return True if one_odd == 1 else False


