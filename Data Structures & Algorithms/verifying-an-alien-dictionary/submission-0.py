class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        alien_dict = {}
        for i, c in enumerate(order):
            alien_dict[c] = i
        for i in range(len(words) - 1):
            word_1, word_2 = words[i], words[i + 1]
            j = 0
            match_so_far = True
            while j < len(word_1) and j < len(word_2) and match_so_far:
                c1, c2 = word_1[j], word_2[j]
                print(c1, c2)
                if c1 != c2:
                    match_so_far = False
                if alien_dict[c2] < alien_dict[c1]:
                    return False
                j += 1
            if j < len(word_1) and match_so_far:
                return False
        return True
            