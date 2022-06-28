import io

class Tokenizer: 
    def __init__(self, filename):
        self.file = open(filename, 'r')
        self.readFile()

    def readFile(self):
        lines = self.file.readlines()
        text = ""
        for line in lines:
            text = text + line.__str__()
        print(text)
        return text

token = Tokenizer("Tokens.py")