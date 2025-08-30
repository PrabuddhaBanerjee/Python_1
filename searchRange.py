class Solution(object):
    def searchRange(self, nums, target):
        """
        34. Find First and Last Position of Element in Sorted Array
        Given an array of integers nums sorted in non-decreasing order, 
        find the starting and ending position of a given target value.

        If target is not found in the array, return [-1, -1].

        You must write an algorithm with O(log n) runtime complexity.

        Input: nums = [5,7,7,8,8,10], target = 8
        Output: [3,4]
        
        Input: nums = [5,7,7,8,8,10], target = 6
        Output: [-1,-1]

        Input: nums = [], target = 0
        Output: [-1,-1]

        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Time Complexity = O(log N)
        left = self.binSearch(nums, target, True)
        right = self.binSearch(nums, target, False)

        return [left, right]


    def binSearch(self, nums, target, leftbias):
        l, r = 0 , len(nums)-1
        i = -1
        while l<=r:
            m = l+r//2
            if target > nums[m]:
                l = m + 1
            elif target < nums[m]:
                r = m - 1
            else:
                i = m
                if leftbias:
                    r = m - 1
                else:
                    l = m + 1
        return i