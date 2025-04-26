class Counter:
    def __init__(self):
        self._count = 0
        self._closed = False

    def add(self):
        if self._closed:
            raise ValueError("Ресурс закрыт!")
        self._count += 1

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._closed = True