from typing import List


class OrderedStream:
    def __init__(self, n: int):
        self.stream = [0] * n
        self.last_seen = 0

    def insert(self, idKey: int, value: str) -> List[str]:
        self.stream[idKey - 1] = value
        return_list = []
        print(self.last_seen)
        while self.last_seen < len(self.stream) and self.stream[self.last_seen] != 0:
            return_list.append(self.stream[self.last_seen])
            self.last_seen += 1
        return return_list


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)
