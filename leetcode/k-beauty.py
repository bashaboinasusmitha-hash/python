class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int: 
        n = str(num)
        # edge case: if k > length, no substrings possible
        if k > len(n):
            return 0
        s = ""
        temp = []
        ans = 0
        # create substrings
        for r in range(len(n)):
            s += n[r]
            if len(s) > k:
                s = s[1:]
            if len(s) == k:
                temp.append(int(s))
        # check divisibility
        for i in range(len(temp)):
            if temp[i] != 0 and num % temp[i] == 0:
                ans += 1
        return ans