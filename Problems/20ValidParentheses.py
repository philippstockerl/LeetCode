class Solution:
    def isValid(self, s: str) -> bool:
        """
        Task :   given a string containing just the characters '(',  ')', '{', '}', '[', and ']',
                determine if the input string is valid.
                
                An input string is valid if:
                - Open brackets must be closed by the same type of brackets
                - Open brackets must be closed in the correct order
                - Every closed bracket has a corresponding open bracket of the same type

                => Use a stack (FILO)
                char  action                     stack afterwards
                (     push                       [ (         ]
                [     push                       [ (, [      ]
                {     push                       [ (, [, {   ]
                }     pop "{" matches "}"        [ (, [      ]
                ]     pop "[" matches "]"        [ (         ]
                )     pop "(" matches ")"        [           ]

        Approach    :   for each character in string s, compare against pairs dict (compare against keys).
                        if the character is not a closing bracket (key in dict), it gets appended to the stack.
                        for each closing bracket, check that the stack is not empty and that the popped opener matches
                        a pairs dict key.
                        only return true if the stack is empty (no leftovers)
        """

        pairs = {")" : "(", "]" : "[", "}" : "{"}
        stack = []

        for parentheses in s:
            if parentheses in pairs:   
                if not stack or stack.pop() != pairs[parentheses]:      
                    return False
                
            else:
                stack.append(parentheses)
        
        return not stack    

    def main(self):
        input = "()[]"
        print(self.isValid(input))


if __name__ == "__main__":
    Solution().main()