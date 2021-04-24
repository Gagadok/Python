# Variant 7
# https://www.un.org/en/sections/issues-depth/climate-change/index.html

import codecs
import difflib
# import nltk

# nltk.download()

from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords

class MyClass:
    
    f = codecs.open('Global warming (errors in the words).txt', 'r', 'utf-8-sig')
    text = f.read()
    f.close()
    
    textToken = word_tokenize(text)
    sentenceToken = sent_tokenize(text)
    
    def tokens(self):
        return self.textToken
    
    def removeAllStopWords(self):
        clean_tokens = self.textToken[:]
        for token in self.textToken:
            if token in stopwords.words('english'):
                clean_tokens.remove(token)
        return clean_tokens
    
    def similarity(self, word, pattern):
        return difflib.SequenceMatcher(a=word.lower(), b=pattern.lower()).ratio()
    
    def wordFrequency(self, text):
        threshold = 0.6
        word_counts={}
        skips = [".", ",", ":", ";", "'", '"', '“', '”', '(', ')', '‘', '’']
        for token in text:
            if token in skips:
                text.remove(token)        
        for word in text:
            word_counts[word] = 0 
        for i in range(len(text)):
            w = text[i]
            if w !="_":
                for k in range(len(text)):
                    w2 = text[k]
                    if self.similarity(w, w2) > threshold:
                        word_counts[w]+= 1
                        text[k]="_"
        word_counts = {k:v for k, v in word_counts.items() if v  != 0}
        return word_counts
    
    def searchSentences(self, word):
        threshold = 0.6
        sentence = []
        wordToken = word_tokenize(word)
        i = 0
        for sen in self.sentenceToken:
            sentenceWord = word_tokenize(sen)
            d = self.wordFrequency(sentenceWord)
            
            for w in wordToken:
                for wD in d.keys():
                     if self.similarity(wD, w) > threshold:
                         i = i + 1
            
            if i > 1:
                sentence.append(sen)
            
            i = 0
        return sentence
  
print ("Choice a variant")
print ("1 - Splitting text into tokens")
print ("2 - Remove all stop words from the text")
print ("3 - Calculate the frequency of word occurrences, including misspelled words")
print ("4 - Search for suggestions by words")
print ("0 - Exit")
t = True
while t:
    choice=input()
    
    if int(choice)<0 or int(choice)>4:
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
        print (z.removeAllStopWords())
        
    if int (choice) == 3:
        z=MyClass()
        print (z.wordFrequency(z.removeAllStopWords()))
        
    if int (choice) == 4:
        z=MyClass()
        word = input("Input a word: ")
        sentences = z.searchSentences(word)
        if sentences:
            print (z.searchSentences(word))
        else:
            print ("Not found. Enter more keywords and check their spelling")