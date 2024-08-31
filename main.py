class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_map = {}  # Dictionary to store the number and its index
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i


# Example usage:
if __name__ == "__main__":
    solution = Solution()

    # Example 1
    nums1 = [2, 7, 11, 15]
    target1 = 9
    print(solution.twoSum(nums1, target1))  # Output: [0, 1]

    # Example 2
    nums2 = [3, 2, 4]
    target2 = 6
    print(solution.twoSum(nums2, target2))  # Output: [1, 2]

    # Example 3
    nums3 = [3, 3]
    target3 = 6
    print(solution.twoSum(nums3, target3))  # Output: [0, 1]
