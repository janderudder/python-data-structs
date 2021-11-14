from typing import Any, List, Optional


class Queue:
    def __init__(self, *data) -> None:
        self._data       = []
        self._frontIndex = 0
        self.push(*data)

    def __str__(self) -> str:
        return f'{self.data()}'

    def push(self, *data) -> None:
        self._data.extend(data)

    def pop(self) -> Optional[Any]:
        self._frontIndex += 1
        return self._data[self._frontIndex-1]

    def popn(self, count=1) -> Optional[Any]:
        prevIndex = self._frontIndex
        count = min(count, self.length())
        self._frontIndex += count
        return self._data[prevIndex:self._frontIndex]

    def clear(self) -> None:
        self._data.clear()
        self._frontIndex = 0

    def length(self) -> int:
        return (len(self._data) - self._frontIndex)

    def isEmpty(self) -> bool:
        return (self.length() == 0)

    def data(self) -> List[Any]:
        return self._data[self._frontIndex:]
