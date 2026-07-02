class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # does that mean if s2 contains all the letters of s1 then return true?
        # because a permutation can be random right
        # s2 = loehfdo and s1 = food would count?
        # No because a permuation ensures that the all the letters are still
        # in place, so 'lhedoof' would count because the letters in 'food'
        # are all there beside eachother just arranged in the wrong order
        # so permuation is scrammbling of the string without introducing chars
        # in between

        # sorting both strings wont work because s2 has equal to or more letters than
        # s1 and so if s1 = hey it would be sorted as ehy and if s2 = afbcyhe it is
        # abcefhy so that f would get in the way

        # create a map to have the (char, frequency) for the string s1
        # have two pointers left and right
        # have a loop through the string s2
        # window logic:
        # using right pointer if you run into a char in the s1_map, put it into 
        # s2_map and move right if the char is not in s1_map, dump the entire map
        # when the char read is in s1_map do not move the left pointer to create the window
        # when the char is not in s1_map move the pointer to be where right pointer is
        # stop when the maps are equal?
        if len(s2) < len(s1):
            return False
        s1Count = [0] * 26
        s2Count = [0] * 26

        # get the counts of each char in each string
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1
        matches = 0

        # count the matches in freq of each char
        for i in range(26):
            if s2Count[i] == s1Count[i]:
                matches += 1
        
        l = 0
        
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            # shift right adds a new char
            index = ord(s2[r]) - ord('a') # index of char at r
            s2Count[index] += 1
            if s2Count[index] == s1Count[index]:
                matches += 1
            elif s2Count[index] == s1Count[index] + 1:
                matches -= 1
            # shift of left pointer leaves a char behind
            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1
            if s2Count[index] == s1Count[index]:
                matches += 1
            elif s2Count[index] == s1Count[index] - 1:
                matches -= 1
            l += 1
        return matches == 26

        

        