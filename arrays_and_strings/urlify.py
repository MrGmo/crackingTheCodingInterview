# Write a method to repalce all spaces in a string with '%20'. You may assume that the string has sufficient space at the end to hold the additional characters, and that you are given the "true" length of the string.

import re

def urlify(string):
    return re.sub(r" +", "%20", string)
