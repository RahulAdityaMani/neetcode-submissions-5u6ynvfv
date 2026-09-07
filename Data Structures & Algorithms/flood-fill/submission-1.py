class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        start = image[sr][sc]
        def helper(r, c):
            if r < 0 or c < 0 or r >= len(image) or c >= len(image[0]) or image[r][c] != start or image[r][c] == color:
                return
            image[r][c] = color
            helper(r + 1, c)
            helper(r - 1, c)
            helper(r, c + 1)
            helper(r, c - 1)
        helper(sr, sc)
        return image
        