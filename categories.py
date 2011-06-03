class Word(object):
	def __init__(self, lemma):
		self.lemma=lemma


class Noun(Word):
	pass
		

class Prep(Word):
	def __init__(self, lemma):
		super(lemma)

class Adj(Word):
	def __init__(self, lemma):
		super(lemma)

class Relation:
	def __init__(self, lemma):
		self.lemma=lemma

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

x=Noun("dog")

print x.lemma



