class Solution:

    def encode(self, strs: List[str]) -> str:
        encode_parts = []
        for s in strs:
            encode_parts.append(str(len(s)))
            encode_parts.append("|")
            encode_parts.append(s)
        return "".join(encode_parts)
            

    def decode(self, s: str) -> List[str]:
        i, decoded = 0, []
        while i < len(s):
            length_chars = []
            j = i
            while j < len(s) and s[j] != "|":
                length_chars.append(s[j])
                j+=1
            length = int("".join(length_chars))
            curr_str = s[j+1:j+1+length]
            decoded.append(curr_str)
            i = j + 1 + length
        return decoded
            

