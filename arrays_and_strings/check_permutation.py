# Given two strings, write a method to decide if one is a permutation of the other.

# Time: O(n), Space: O(n)
def check_permutation(str1, str2):
    obj = {}

    if len(str1) != len(str2):
        return False

    for char in str1:
        if char not in obj:
            obj[char] = 1
        else:
            obj[char] += 1

    for char in str2:
        if char not in obj:
            return False
        else:
            obj[char] -= 1
    return True
