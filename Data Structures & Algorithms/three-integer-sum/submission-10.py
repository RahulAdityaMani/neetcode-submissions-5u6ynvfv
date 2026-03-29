class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = set()
        nums = sorted(nums)
        for l in range(len(nums)):
            l_to_zero = 0 - nums[l]
            m = l + 1
            r = len(nums) - 1
            while m < r:
                m_r_sum = nums[m] + nums[r]
                if m_r_sum == l_to_zero:
                    triplets.add(tuple([nums[l], nums[m], nums[r]]))
                    m += 1
                    r -= 1
                elif m_r_sum > l_to_zero:
                    r -= 1
                else:
                    m += 1
        return list(triplets)