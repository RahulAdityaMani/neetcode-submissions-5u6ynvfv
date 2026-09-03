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
            start = i
            while s[i] != "@":
                i += 1
            s_len = int(s[start:i])
            i += 1
            s_str = s[i:i+s_len]
            decoded.append(s_str)
            i = i + s_len
        return decoded
