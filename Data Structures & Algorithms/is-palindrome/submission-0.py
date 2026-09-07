class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while i < j:
            left = s[i]
            right = s[j]
            if not left.isalnum():
                i += 1
                continue
            if not right.isalnum():
                j -= 1
                continue
            if left.lower()!= right.lower():
                return False
            i += 1
            j -= 1
        return True
            

        