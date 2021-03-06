'''
Created on 8 Feb 2010

@author: paul
'''
import random

class NounPair:
    def __init__(self,n1,n2):
        self.n1=n1
        self.n2=n2
    def __eq__(self,other):
        return (self.n1==other.n1 and self.n2==other.n2)

class Paraphrase:
    def __init__(self,name,freq=0.0):
        self.name=name
        self.freq=freq
    def __eq__(self,other):
        return self.name==other.name

def parse_file(file):
    '''reads the data file and makes a list of NounPair objects with 
    paraphrase objects as attributes'''
    lines=file.readlines()
    examples=[]
    old=""
    for line in lines:
        line=line.split('\t')
        if len(line)<2:continue
        cur=line[0].replace(' ','_')
        if not old==cur: # then we've reached the next pairs
            this_pair= NounPair(line[0].split()[0],line[0].split()[1])
            examples.append(this_pair)
            this_pair.paraphrases=[]
        freq=0.0
        if len(line)>2: freq=int(line[2])
        tmp=Paraphrase(line[1].strip(),freq)
        this_pair.paraphrases.append( tmp )
        old=line[0].replace(' ','_')
    return examples
