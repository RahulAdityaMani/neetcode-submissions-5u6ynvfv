class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_parts = []
        for s in strs:
            encoded_parts.append(str(len(s)))
            encoded_parts.append("@")
            encoded_parts.append(s)
        return "".join(encoded_parts)

    def decode(self, s: str) -> List[str]:
        i = 0
        output = []
        while i < len(s):
            j = i
            while j < len(s) and s[j] != "@":
                j += 1    
            curr_len = int(s[i:j])
            output.append(s[j+1:j+1+curr_len])
            i = j + curr_len + 1
        return output
            

