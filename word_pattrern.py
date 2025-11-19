# https://leetcode.com/problems/word-pattern/

# In this program to check the pattern and string, split the string into the words. Used two hashmaps for the string and pattern. Iterated over the string and checked that each pattern character always maps to the same word and each word maps to the same pattern character.
# Time Complexity O(n), Space Complexity O(n)

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # split the string into words so that pattern and words can be iterated together because pattern map to words not characters
        words = s.split()
        # handle the edge case
        if len(pattern) != len(words):
            return False
        # create two hashmaps
        patternmap = {}
        stringmap = {}
        # iterate over the pattern(string 's' also has the same length so considered only 'pattern') 
        for char in range(len(pattern)):
            pchar = pattern[char]
            schar = words[char]
            # check the pattern characters
            if pchar in patternmap:
                # if we are checking the previously present 'pattern' character, then it should map to same 's' character
                if patternmap[pchar] != schar:
                    # if it's not equal return False
                    return False
            # if we are checking the character for the first time, add into the map
            else:
                # add into the map
                patternmap[pchar] = schar
            # check the string 's' characters
            if schar in stringmap:
                # if we are checking the previously present 's' character, then it should map to same 'pattern' character
                if stringmap[schar] != pchar:
                    # if it's not equal return False
                    return False
            # if we are checking the character for the first time, add into the map
            else:
                stringmap[schar] = pchar
        return True


sh = Solution()
print(sh.wordPattern('abba','dog cat cat dog'))
print(sh.wordPattern('abba','dog cat cat fish'))