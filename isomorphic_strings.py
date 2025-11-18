# https://leetcode.com/problems/isomorphic-strings/

# In this program to check the isomorphic string, created two hashmaps. Iterated over the hashmaps and checked whether the character in one hashmap mapped to the same character in other map.
# Time Complexity O(n) - Because of the iteration over the two string 2n but we consider it as n. 
# Space Complexity O(1) becuase the only the characters are coming which is 26 means it's constant


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # created two hashmaps for two strings
        sMap = {}
        tMap = {}

        # iterating over both strings
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

# using zip function

def isIsomorphic(self, s: str, t: str) -> bool:
    sMap = {}
    tMap = {}

    for sc, tc in zip(s, t):
        if sc in sMap and sMap[sc] != tc:
            return False
        if tc in tMap and tMap[tc] != sc:
            return False
        
        sMap[sc] = tc
        tMap[tc] = sc

    return True


sh =Solution()
print(sh.isIsomorphic("egg",'add'))
print(sh.isIsomorphic("foo",'bar'))