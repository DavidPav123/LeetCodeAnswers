class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {"A", "a", "E", "e", "I", "i", "O", "o", "U", "u"}
        string_list = list(s)
        str_vowels = []
        vowel_pos = []

        for char in enumerate(s):
            if char[1] in vowels:
                str_vowels.append(char[1])
                vowel_pos.append(char[0])

        str_vowels.reverse()
        for chars in enumerate(str_vowels):
            string_list[vowel_pos[chars[0]]] = chars[1]

        s = ""

        return s.join(string_list)
