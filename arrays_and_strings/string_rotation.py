# Assume you have a method isSubstring which checks if one word is a substring of another. Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one call to isSubstring (e.g. "waterbottle" is a rotation of "erbottlewat")

# Time: O(), Space: O()

# Time: O(n), Space: O(1)
def is_substring(s1, s2):
    count = 0
    while count < len(s1):
        s2 = s2[1:] + s2[0]
        if s1 == s2:
            return True
        count += 1
    return False
