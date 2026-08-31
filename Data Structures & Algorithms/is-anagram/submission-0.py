import string

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if(len(s) != len(t)):
            return False

        alphabet_map_s = {letter: 0 for letter in string.ascii_lowercase}
        alphabet_map_t = {letter: 0 for letter in string.ascii_lowercase}


        for item in s:
            alphabet_map_s[item] += 1

        for item in t:
            alphabet_map_t[item] += 1
        # alphabet_array = [chr(i) for i in range(97, 123)]
        # print(alphabet_array)   

        return alphabet_map_s == alphabet_map_t
        