class conversion:
    def __init__(self, text):
        self.text = text

    def to_ascii(self):
        return [ord(char) for char in self.text]


    



