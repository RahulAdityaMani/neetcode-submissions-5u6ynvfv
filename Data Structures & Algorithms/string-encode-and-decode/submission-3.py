class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for s in strs:
            encoded.append(str(len(s)))
            encoded.append("@")
            encoded.append(s)
        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        while i < len(s):
            length_arr = []
            while i < len(s) and s[i] != "@":
                length_arr.append(s[i])
                i += 1
            length_str = "".join(length_arr)
            length_int = int(length_str)
            i += 1 # @
            curr_str_arr = []
            while i < len(s) and len(curr_str_arr) < length_int:
                curr_str_arr.append(s[i])
                i += 1
            curr_str_str = "".join(curr_str_arr)
            decoded.append(curr_str_str)
        return decoded