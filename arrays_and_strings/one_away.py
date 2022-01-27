# There are three types of edits that can be performed on strings: insert a character, remove a character, or replace a character. Given two strings, write a function to check if they are one edit(or zero edits) away.


# #Time: O(n), Space: O(1)
def one_away(s1, s2):
    initial_count = abs(len(s1) - len(s2))
    if initial_count > 1:
        return False
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            initial_count += 1
    return True if initial_count < 2 else False
