

class CircularBufferException(Exception):
    pass

class BufferFullException(CircularBufferException):
    pass


class BufferEmptyException(CircularBufferException):
    pass


class CircularBuffer():
    def __init__(self, size):
        self._buffer = [None] * size
        self._top = 0
        self._len = 0

    def read(self):
        if self._is_empty():
            raise BufferEmptyException()

        value = self._buffer[self._top]
        self._top = self._next_top()
        self._len -= 1
        return value

    def write(self, value):
        if self._is_full():
            raise BufferFullException()

        self._buffer[self._bottom()] = value
        self._len += 1

    def overwrite(self, value):
        if self._is_full():
            self.read()
        self.write(value)

    def clear(self):
        self._len = 0

    def _is_empty(self):
        return self._len == 0

    def _is_full(self):
        return self._len == len(self._buffer)

    def _next_top(self):
        return (self._top + 1) % len(self._buffer)

    def _bottom(self):
        return (self._top + self._len) % len(self._buffer)
