from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        duplicate_nums = set()
        for number in nums:
            if number in duplicate_nums:
                return True
            else:
                duplicate_nums.add(nums)
        return False

#     seen = set()
#         for num in nums:
#             if num in seen:
#                 return True
#             seen.add(num)
#         return False


if __name__ == '__main__':
    Solution().containsDuplicate()
