class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_arr = []
        for s in strs:
            encoded_arr.append(str(len(s)))
            encoded_arr.append("&")
            encoded_arr.append(s)
        return "".join(encoded_arr)

    def decode(self, s: str) -> List[str]:
        i = 0
        output = []
        while i < len(s):
            j = i
            while j < len(s) and s[j] != "&":
                j += 1
            length = int(s[i:j])
            i = j + 1
            while j < len(s) and j < i + length:
                j += 1
            string = s[i:j]
            output.append(string)
            i = j
        return output