class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums = sorted(nums)
        for l in range(len(nums)):
            if l > 0 and nums[l] == nums[l - 1]:
                continue
            l_to_zero = 0 - nums[l]
            m = l + 1
            r = len(nums) - 1
            while m < r:
                m_r_sum = nums[m] + nums[r]
                print([nums[l], nums[m], nums[r]])
                if m_r_sum == l_to_zero:
                    triplets.append([nums[l], nums[m], nums[r]])
                    m += 1
                    r -= 1
                    while m < r and nums[m] == nums[m - 1]:
                        m += 1
                    while m < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif m_r_sum > l_to_zero:
                    r -= 1
                else:
                    m += 1
        return triplets