'''
Created on Apr 9, 2015

@author: root
'''
class WordAndTag():
    
    def __init__(self,word,tag):
        self.word=word
        self.tag=tag
    def __repr__(self):
        return self.word+self.tag