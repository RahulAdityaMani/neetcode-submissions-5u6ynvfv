class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for s in strs:
            encoded.append(str(len(s)))
            encoded.append("@")
            encoded.append(s)
        print(encoded)
        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        print(s)
        while i < len(s):
            length = []
            while s[i] != "@":
                length.append(s[i])
                i += 1
            length_str = "".join(length)
            length_num = int(length_str)
            i += 1
            j = 0
            curr = []
            for j in range(i, i + length_num):
                curr.append(s[j])
            curr_str = "".join(curr)
            decoded.append(curr_str)
            i += length_num
        return decoded