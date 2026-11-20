class Solution:
    def isPalindrome(self, s: str) -> bool:

        ct="".join(char.lower() for char in s if char.isalnum())

        if ct==ct[::-1]:
            return True
        else:
            return False
        