# Implement a method to perform basic string compression using the counts of repeated characters. For example, the string aabcccccaaa would become a2b1c5a3. If the "compressed" string would not become smaller than the original string, your method should return the original string. You can assume the string has only uppercse and lowercase letters (a-z).


# Time: O(n), Space: O(n)
def compress(string):
    result_list = []
    length = 1
    for i in range(len(string) - 1):
        if string[i] != string[i + 1] or length == 9:
            result_list.append(string[i] + str(length))
            length = 0
        length += 1
    result_list.append(string[len(string) - 1] + str(length))
    return "".join(result_list)
