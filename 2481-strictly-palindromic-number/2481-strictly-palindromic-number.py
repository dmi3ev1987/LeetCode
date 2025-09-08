class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        # For n >= 4, base n-2 gives "12" which is not palindrome.
        # For n=1,2,3: no bases in the range [2, n-2]
        # (since n-2 < 2), so vacuously true.
        if n <= 3:
            return True
        else:
            return False