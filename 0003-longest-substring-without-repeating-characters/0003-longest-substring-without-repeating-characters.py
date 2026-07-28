class Solution(object):
    def lengthOfLongestSubstring(self, s):
        n = len(s)
        maxi_length = 0

        for i in range(n):
            my_set = set()

            for j in range(i, n):
                if s[j] in my_set:
                    break

                my_set.add(s[j])
                maxi_length = max(maxi_length, j - i + 1)

        return maxi_length