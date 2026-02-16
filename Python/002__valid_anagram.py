# Valid Anagram
#
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
#
# Example 1:
#
# Input: s = "anagram", t = "nagaram"
#
# Output: true
#
# Example 2:
#
# Input: s = "rat", t = "car"
#
# Output: false
#
# Constraints:
#
# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Check if t is an anagram of s.
        Time: O(n)
        Space: O(1) - since alphabet size is fixed (26)
        """
        if len(s) != len(t):
            return False

        freq = [0] * 26

        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        for ch in t:
            freq[ord(ch) - ord('a')] -= 1

        for count in freq:
            if count != 0:
                return False

        return True


def main():
    solution = Solution()

    # Test Case 1
    s = "anagram"
    t = "nagaram"
    print("Test Case 1 Output:", solution.isAnagram(s, t))  # True

    # Test Case 2
    s = "rat"
    t = "car"
    print("Test Case 2 Output:", solution.isAnagram(s, t))  # False

    # Additional Edge Case
    s = "aacc"
    t = "ccac"
    print("Test Case 3 Output:", solution.isAnagram(s, t))  # False


if __name__ == "__main__":
    main()
