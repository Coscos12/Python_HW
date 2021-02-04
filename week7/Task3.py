class CircleIterator:

    def __init__(self, text, end):
        self.text = text
        self.counter = 0
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < self.end:
            self.counter += 1
            return self.text[self.counter % len(self.text)]
        else:
            raise StopIteration
