# first solution


class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        s=[]
        for i in range(len(candies)):
            s.append(extraCandies+candies[i] >=max(candies))
        return s

# second solution

class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        c=max(candies)
        b=[]
        a=len(candies)
        for i in range(a):
            b.append(extraCandies+candies[i] >= c)
        return b



