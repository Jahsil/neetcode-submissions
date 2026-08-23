class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        N = len(s)
        length, longest = 0, 0
        count = dict()
        for i in range(65, 91):
            count[chr(i)] = 0
        left = 0 

        for right in range(N):
            length = right - left + 1
            count[s[right]] = count[s[right]] + 1
            while (length - max(count.values()) > k) and count[s[left]] > 0:
                count[s[left]] = count[s[left]] - 1
                left += 1
                length = right - left + 1
            
            longest = max(longest, length)

        return longest

            
        