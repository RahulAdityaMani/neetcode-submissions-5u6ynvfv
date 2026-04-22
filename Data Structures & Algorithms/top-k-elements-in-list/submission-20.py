class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k >= len(nums):
            return nums
        counts = Counter(nums)
        count_to_nums = [[] for _ in range(len(nums))]
        for num, count in counts.items():
            count_to_nums[count - 1].append(num)
        output = []
        for count in range(len(nums) - 1, -1, -1):
            while count_to_nums[count]:
                output.append(count_to_nums[count].pop())
                k -= 1
                if k == 0:
                    return output
        