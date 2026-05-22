class TimeMap:
    def __init__(self):
        self.dict = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dict.setdefault(key, []).append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        values = self.dict.get(key, [])
        left = 0
        right = len(values) - 1
        best = ""

        while left <= right:
            mid = (left + right) // 2

            mid_value, mid_time = values[mid]

            if mid_time <= timestamp:
                best = mid_value
                left = mid + 1
            else:
                right = mid - 1

        return best