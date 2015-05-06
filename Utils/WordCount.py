'''
Created on Apr 24, 2015

@author: root
'''
class WordCount():
    def __init__(self,tag,count,total):
        self.tag = tag
        self.count = count
        self.total = total
    def __repr__(self):
        return str(self.count)+self.tag+str(self.total)
