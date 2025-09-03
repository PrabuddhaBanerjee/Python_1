class Solution(object):
    def longestPalindrome(self, s):
        """
        5. Longest Palindromic Substring

        Given a string s, return the longest palindromic substring in s.

        Input: s = "babad"
        Output: "bab"
        Explanation: "aba" is also a valid answer.

        Input: s = "cbbd"
        Output: "bb"
        
        Constraints:
        1 <= s.length <= 1000
        s consist of only digits and English letters.

        :type s: str
        :rtype: str
        """
        # Time complexity O(n^2)
        res = ""
        resLen = 0

        for i in range(len(s)):
            # Odd length
            l, r = i, i
            while l>=0 and r<len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l: r+1]
                    resLen = r - l + 1
                l -= 1
                r += 1
            # Even Length
            l, r = i, i+1
            while l>=0 and r<len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l: r+1]
                    resLen = r - l + 1
                l -= 1
                r += 1
                
        return res
        