class Solution:

    def encode(self, strs: List[str]) -> str:
        # if the list is empty then return nothing
        if not strs:
            return ""
        encoded_string =  ""
        
        for s in strs:
            encoded_string += str(len(s)) + "#" + s
        
        return encoded_string



    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        i = 0
        while i < len(s):
            j = i;
            while s[j] != "#":
                j = j + 1 #  going upto the hash symbol 
            length = int(s[i:j])
            # j is at the hash symbol, j + 1 is where the string starts
            i = j + 1
            j = i + length
            decoded_strs.append(s[i:j])
            i = j
            
        return decoded_strs
            
