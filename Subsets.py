from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans_list = [[]]
        # Adding single values
        for i in range(len(nums)):
            add_to_list = [nums[i]]
            ans_list.append(add_to_list)

        # Add last value
        ans_list.append(nums)
        return ans_list


if __name__ == '__main__':
    print(Solution().subsets([1,2,3,4]))
