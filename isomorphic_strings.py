# https://leetcode.com/problems/isomorphic-strings/

# In this program to check the isomorphic string, created two hashmaps. Iterated over the hashmaps and checked whether the character in one hashmap mapped to the same character in other map.
# Time Complexity O(n), Space Complexity O(1)

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # handel the edge case
        if len(s) != len(t):
            return False

        # create two hashmaps for two strings
        sMap = {}
        tMap = {}

        # iterate over both strings
        for i in range(len(s)):
            sChar = s[i]
            tChar = t[i]
            # check the string 's' characters
            if sChar in sMap:
                #  if we are checking the same 's' character, then it should map to same 't' character
                if sMap[sChar] != tChar:
                    # if it's not equal return False
                 return False
            # if we are checking the character for the first time
            else:
                # add into the map
                sMap[sChar] = tChar
            # check the string 't' characters
            if tChar in tMap:
                # if we are checking the same 't' character, then it should map to same 's' character
                if tMap[tChar] != sChar:
                    return False
            # if we are checking the character for the first time
            else:
                tMap[tChar] = sChar
        return True


sh =Solution()
print(sh.isIsomorphic("egg",'add'))
print(sh.isIsomorphic("foo",'bar'))