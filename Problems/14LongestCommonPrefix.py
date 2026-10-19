class Solution:
    def longestCommonPrefix(
            self, 
            strs: list[str]
            ) -> str:
        """
        Task        :   write a function that finds the longest common prefix amongst
                        an array of strings; if there is no common prefix, return an
                        empty string
        Approach    :   vertical col scanning ("walk" chr positions)

            index:  0  1  2  3  4  5
                    ----------------
            flower  f  l  o  w  e  r
            flow    f  l  o  w
            flight  f  l  i  g  h  t

            1) Outer loop walks chr positions (cols) up to len of shortet word
            2) First chr of first word is used as reference
            3) Compare first chr of each word with reference:
                - Mismatch: return current build of prefix
                - All match: append reference to prefix
        """

        prefix = ""
        for i in range(len(min(strs, key=len))):   
            reference = strs[0][i] 
            for word in strs:
                if word[i] != reference:
                    return prefix
            prefix += reference
        return prefix
    

    def main(self):
        input = ["dog", "car", "flight"]
        print(self.longestCommonPrefix(input))


if __name__ == "__main__":
    Solution().main() 