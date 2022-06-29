import io
import re
'''Reads text from file and breaks it down into tokens
'''
class Tokenizer: 
    def __init__(self, filename):
        self.file = open(filename, 'r')
        self.lines = self.file.readlines()
        self.getWords()
        
    def getWords(self):
        words = []
        for line in self.lines:
            words = words + re.findall(r'[a-zA-Z0-9]+|[\(\)+\-*/=]', line)
        print(words)
        self.tokens = words

    def nextToken(self):
        return self.tokens.pop(0)
    
    #for each token, create a token object
    def createToken(self, word):
        pass
