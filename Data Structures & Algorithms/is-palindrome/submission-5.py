class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower_s = s.lower()
        cleaned = ""

        for char in lower_s:
            if char.isalpha() or char.isalnum():
                cleaned+=char

        print(cleaned)

        if cleaned !=cleaned[::-1]:
            return False

        return True

        