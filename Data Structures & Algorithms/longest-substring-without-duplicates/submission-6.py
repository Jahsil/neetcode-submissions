class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        N = len(s)
        length, longest = 0, 0 
        seen = set()
        left = 0 

        for right in range(N):
            if s[right] in seen:
                while s[left] != s[right]:
                    seen.remove(s[left])
                    left += 1
                seen.remove(s[left])
                left += 1
                seen.add(s[right])
                
            else:
                seen.add(s[right])
            length = right - left + 1   
            longest = max(longest, length)

        return longest
