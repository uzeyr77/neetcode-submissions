class Solution:
        def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
                # sort the strings and then group in hashmap
                # hashmap stored as {sorted_string: [str1, str2, str3]} where str1...strn 
                # sorted is equal to sorted_string
                # make a map with key as sorted_string, then loop through and check if 
                # any string is equivalent as anagram
                map = dict()
                result = list()
                for i in range(0, len(strs)):
                        map["".join(sorted(strs[i]))]= []

                for s in strs:
                        if "".join(sorted(s)) in map:
                                map["".join(sorted(s))].append(s)


                return list(map.values())       