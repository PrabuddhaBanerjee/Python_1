class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        3. Longest Substring Without Repeating Characters

        Given a string s, find the length of the longest 
        substring without duplicate characters.

        Input: s = "abcabcbb"
        Output: 3
        Explanation: The answer is "abc", with the length of 3.

        Input: s = "bbbbb"
        Output: 1
        Explanation: The answer is "b", with the length of 1.

        Input: s = "pwwkew"
        Output: 3
        Explanation: The answer is "wke", with the length of 3.
        Notice that the answer must be a substring, "pwke" is a 
        subsequence and not a substring.

        :type s: str
        :rtype: int
        """
        # Time Complexity O(n)
        charSet = set()
        l = 0
        result = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            result = max(result, r - l + 1)
        
        return result