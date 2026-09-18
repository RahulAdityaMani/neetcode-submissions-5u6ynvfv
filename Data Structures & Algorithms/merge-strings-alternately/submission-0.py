class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        output = []
        i1, i2 = 0, 0
        while i1 < len(word1) and i2 < len(word2):
            if (i1 + i2) % 2 == 0:
                output.append(word1[i1])
                i1 += 1
            else:
                output.append(word2[i2])
                i2 += 1
        while i1 < len(word1):
            output.append(word1[i1])
            i1 += 1
        while i2 < len(word2):
            output.append(word2[i2])
            i2 += 1
        return "".join(output)