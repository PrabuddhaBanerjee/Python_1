class Solution(object):
    def maximumTastiness(self, price, k):
        """
        2517. Maximum Tastiness of Candy Basket

        You are given an array of positive integers 
        price where price[i] denotes the price of the 
        ith candy and a positive integer k.

        The store sells baskets of k distinct candies. 
        The tastiness of a candy basket is the smallest 
        absolute difference of the prices of any two candies 
        in the basket.

        Return the maximum tastiness of a candy basket.

        Input: price = [13,5,1,8,21,2], k = 3
        Output: 8
        Explanation: Choose the candies with the prices [13,5,21].
        The tastiness of the candy basket is: min(|13 - 5|, |13 - 21|, 
        |5 - 21|) = min(8, 8, 16) = 8.
        It can be proven that 8 is the maximum tastiness that can be achieved.

        Input: price = [1,3,1], k = 2
        Output: 2
        Explanation: Choose the candies with the prices [1,3].
        The tastiness of the candy basket is: min(|1 - 3|) = min(2) = 2.
        It can be proven that 2 is the maximum tastiness that can be achieved.

        Input: price = [7,7,7,7], k = 2
        Output: 0
        Explanation: Choosing any two distinct candies from the candies we have will 
        result in a tastiness of 0.

        :type price: List[int]
        :type k: int
        :rtype: int
        """
        price.sort()
        lo = 0
        hi = max(price) - min(price)
        res = 0
        def check(mid):
            count = 1
            prev = price[0]
            i = 0

            while i<len(price) and count < k:
                if price[i] - prev >= mid:
                    prev = price[i]
                    count += 1
                i+=1
            
            return count == k

        while lo<=hi:
            mid = (lo + hi)//2

            if check(mid):
                lo = mid+1
                res = mid

            else:
                hi = mid - 1
        
        return res
