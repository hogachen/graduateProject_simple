#encoding=utf-8
'''
Created on Apr 14, 2015

@author: root
'''
class CountAndTag():
    def __init__(self,count,tag):
        self.count=count
        self.tag = tag
    def __repr__(self):
        return str(self.count)+self.tag