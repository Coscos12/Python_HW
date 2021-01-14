class Sentense:

    def __init__(self, text):
        self.text = text
        self.counter = 0
        self.lst = self.text.split()

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < len(self.lst):
            self.counter += 1
            return self.lst[self.counter - 1]
        else:
            raise StopIteration
