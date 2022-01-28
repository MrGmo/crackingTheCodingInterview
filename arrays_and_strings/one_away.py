# There are three types of edits that can be performed on strings: insert a character, remove a character, or replace a character. Given two strings, write a function to check if they are one edit(or zero edits) away.


# #Time: O(n), Space: O(1)
def one_away(s1, s2):
    initial_count = abs(len(s1) - len(s2))
    if initial_count > 1:
        return False
    p1, p2 = 0, 0
    madeEdit = False

    while p1 < len(s1) and p2 < len(s2):
        if s1[p1] == s2[p2]:
            p1 += 1
            p2 += 1
        elif not madeEdit:
            madeEdit = True
            if len(s1) == len(s2):
                p1 += 1
                p2 += 1
            elif len(s1) < len(s2):
                p2 += 1
            else:
                p1 += 1
        else:
            return False
    return True
