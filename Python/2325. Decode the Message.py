class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        message_list = list(message)
        key_dict = {" ": " "}
        key = key.replace(" ", "")
        key_chars = []
        for c in key:
            if c not in key_chars:
                key_chars.append(c)
        for i in range(len(key_chars)):
            key_dict[key_chars[i]] = chr(97 + i)
        print(key_dict)
        for char in range(len(message_list)):
            message_list[char] = key_dict[message_list[char]]

        return "".join(message_list)
