class Solution:
    def interpret(self, command: str) -> str:
        final_string = ""
        char = 0
        while char < len(command): 
            print(char)
            if command[char] == 'G':
                final_string += 'G'
                char += 1
            else:
                if command[char + 1] == ')':
                    final_string += 'o'
                    char += 2
                else:
                    final_string += 'al'
                    char += 4
        return final_string
