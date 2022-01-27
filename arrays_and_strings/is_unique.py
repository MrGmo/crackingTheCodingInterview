# Implement an algorithm to determine if a string has all unique characters. Don't use additional data structures.

# Time: O(nlog(n)), Space: O(n)
def is_unique(string):
    s = sorted(string)
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            return False
    return True


# Time: O(n^2), Space O(1)
def is_unique(string):
    for i in range(len(string)):
        for j in range(i + 1, len(string)):
            if string[i] == string[j]:
                return False
    return True