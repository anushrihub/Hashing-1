# https://leetcode.com/problems/group-anagrams/

# To group the anagrams together, we used a hashmap. Firstly, iterate over the given array of string. Then sort the each individual string aplhabetically. Create the sorted string as the key and map the original order strings inside the hashmap as the values.
# Time complexity- O(n * k log k) Space complexity- O(n * k)
class Solution:
    def groupAnagrams(self, strs):
        #  creating an empty hashmap
        map = {}

        # interate through the given string
        for words in strs:
            # we are using sort function to sort the word in aphabetical order after doing that we get individual character of a word to bind them using join fucntion
            sorted_string = ''.join(sorted(words))

            # if the sorted_string is not present in the map create an empty list for them
            if sorted_string not in map:
                map[sorted_string] = []

            #  append the word into the sorted string means it's own sorted gorup of character's
            map[sorted_string].append(words)

        return list(map.values())

sh = Solution()
print(sh.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))

