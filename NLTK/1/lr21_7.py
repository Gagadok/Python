# Variant 7
# https://www.un.org/en/sections/issues-depth/climate-change/index.html

import nltk, re
import codecs
# nltk.download()

from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords

class MyClass:
    
    f = codecs.open('Global warming.txt', 'r', 'utf-8-sig')
    text = f.read()
    f.close()
    
    textToken = word_tokenize(text)
    
    def tokens(self):
        return self.textToken
    
    def mostCommonToken(self):
        freq = nltk.FreqDist(self.textToken)
        maxKey = ''
        maxVal = 0
        for key,val in freq.items():
            if maxVal < val :
                maxKey = key
                maxVal = val
        return maxKey, maxVal
    
    def tokenRoot(self):
        root = []
        stemmer = PorterStemmer()
        for token in self.textToken:
            root.append(stemmer.stem(token))
        return root
    
    def wordPosition(self, word):
        position = []
        i = 0
        for token in self.textToken:
            if token == word:
                position.append(i)
            i = i + 1
        return position
    
    def regularExpression(self):
        z=[t for t in self.textToken if re.search('er$', t)]
        return z
    
    def subWord(self, word):
        sW = []
        for token in self.textToken:
            if token.find(word) != -1:
                sW.append(token)
        return sW
    
    def removeAllStopWords(self):
        clean_tokens = self.textToken[:]
        for token in self.textToken:
            if token in stopwords.words('english'):
                clean_tokens.remove(token)
        return clean_tokens
  
print ("Choice a variant")
print ("1 - Splitting text into tokens")
print ("2 - The most common token")
print ("3 - Output the token root")
print ("4 - Position of the word in the text")
print ("5 - Find all words ending in 'er'")
print ("6 - Find all words that contain the specified sub-word")
print ("7 - Remove all stop words from the text")
print ("0 - Exit")
t = True
while t:
    choice=input()
    
    if int(choice)<0 or int(choice)>7:
        print ("Select again")
        continue
    
    if int (choice) == 0:
        print ("Exit")
        break
    
    if int (choice) == 1:
        z=MyClass()
        print(z.tokens())
    
    if int (choice) == 2:
        z=MyClass()
        print("Token: " + z.mostCommonToken()[0] + "\nNumber of repetitions: " + 
              str(z.mostCommonToken()[1]))
        
    if int (choice) == 3:
        z=MyClass()
        print(z.tokenRoot())
        
    if int (choice) == 4:
        z=MyClass()
        word = input("Input a word: ")
        print("Position of the word '" + word + "': " + str(z.wordPosition(word)))
        
    if int (choice) == 5:
        z=MyClass()
        print (z.regularExpression())
        
    if int (choice) == 6:
        z=MyClass()
        subWord = input("Input a sub-word: ")
        print("Words containing a sub-word '" + subWord + "': " + str(z.subWord(subWord)))
        
    if int (choice) == 7:
        z=MyClass()
        print (z.removeAllStopWords())