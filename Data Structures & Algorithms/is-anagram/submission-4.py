# import string
from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # if(len(s) != len(t)):
        #     return False

        return Counter(s) == Counter(t)

        # alphabet_map_s = {letter: 0 for letter in string.ascii_lowercase}
        # alphabet_map_t = {letter: 0 for letter in string.ascii_lowercase}


        # for item in s:
        #     alphabet_map_s[item] += 1

        # for item in t:
        #     alphabet_map_t[item] += 1  

        # return alphabet_map_s == alphabet_map_t
        