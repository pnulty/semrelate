import parse_semeval
import cPickle
import random

class Paraphrase:
    def __init__(self,name,freq=0.0):
        self.name=name
        self.freq=freq
    def __eq__(self,other):
        return self.name==other.name

print "unpickling: priors"
priors=cPickle.load(open('/home/paul/mayThesis/pickles/allPriors'))
totals=sorted(priors.items(), key=lambda x: x[1], reverse=True)
for t in totals:print t

base=[]
for t in totals[0:5]:
    base.append(Paraphrase(t[0]))

print "unpickling prob table"
probs=cPickle.load(open('/home/paul/mayThesis/pickles/allProbs'))
ftrain=open("/home/paul/mayThesis/semEvalTask9/training.txt")
ftest=open("/home/paul/mayThesis/semEvalTask9/testing.txt")
train_pairs=parse_semeval.parse_file(ftrain)
test_pairs=parse_semeval.parse_file(ftest)
all_pairs=train_pairs+test_pairs
total=0.0
basetotal=0.0
errcount=0
for pair in all_pairs:
    paras=[]
    for p in pair.paraphrases:
        if p.freq>6.0: paras.append(p)
    number=len(paras)
    if len(paras)>4:
        subs=random.sample(paras,3)
    else: continue
    for p in paras:
        if p in subs: del(p)
    results=[]
    print pair.n1+" "+pair.n2
    for p in probs.keys():
        x=Paraphrase(p.strip())
        x.score=0.0
        results.append(x)
    for p in results:
        for s in subs:
            try:
                p.score+=(probs[p.name][s.name] ) / 1.0
                #print "done"
            except KeyError:
                errcount+=1
                print errcount
                pass
                #print "err"
    results.sort(key= lambda para: para.score, reverse=True)
    print "chosen subset:"
    for s in subs: print s.name
    print "\n"
    print "predicted paraphrases:"
    for r in results[0:10]: print r.name
    print "\n"
    print "actual"
    for p in paras[0:10]: print p.name
    score=0.0
    basescore=0.0
    for r in base[0:10]:
        if r in pair.paraphrases:basescore+=1.0
    for r in results[0:10]:
        if r in pair.paraphrases:score+=1.0
    print score/10.0
    total+=(score/10.0)
    basetotal+=(basescore/10.0)
    print "**\n\n**"
print "predictions:"
print total/len(all_pairs)
print
print "baseline:"
print basetotal/len(all_pairs)