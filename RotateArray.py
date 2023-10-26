from typing import List


def rotate(nums: List[int], k: int) -> None:
    if k >= len(nums):
        k = k % len(nums)
    if len(nums) == 1 or k == 0:
        return nums
    nums[:k], nums[k:] = nums[-k:], nums[:-k]
    return nums


if __name__ == "__main__":
    array = {1,2,3,4,5,6,7}
    rotate(array, 3)
    print(array)