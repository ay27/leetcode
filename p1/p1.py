__author__ = 'ay27'


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        flag = {}
        for i in range(len(nums)):
            if target-nums[i] in flag:
                return [flag[target-nums[i]]+1, i + 1]
            else:
                flag[nums[i]] = i


sol = Solution()
ll = []
targ = 0
with open('p1/in.txt', 'r') as f:
    ll = list(map(int, f.readline().split(',')))
    targ = int(f.readline())
print(sol.twoSum(ll, targ))
