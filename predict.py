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
priors=cPickle.load(open('/home/paul/thesis/data/pickles/trainingPriors'))
print "unpickling prob table"
probs=cPickle.load(open('/home/paul/thesis/data/pickles/trainingProbs'))
f=open("/home/paul/thesis/data/SemEval2Task9/SemEval2_task9_testing_keys/FINAL_GOLD.txt")
all_pairs=parse_semeval.parse_file(f)
total=0.0
for pair in all_pairs:
    paras=[]
    for p in pair.paraphrases:
        if p.freq>2:paras.append(p) 
    number=len(paras)
    subs=random.sample(paras,3)
    results=[]
    print pair.n1+" "+pair.n2
    for p in probs.keys():
        x=Paraphrase(p.strip())
        x.score=0.0
        results.append(x)
    for p in results:
        for s in subs:
            try:
                p.score+=(probs[p.name][s.name] ) /1.0
                #print "done"
            except KeyError:
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
    for p in pair.paraphrases[0:10]: print p.name
    score=0.0
    for r in results[0:10]:
        if r in pair.paraphrases:score+=1.0
    print score/10.0
    total+=(score/10.0)
    print "**\n\n**"

print total/len(all_pairs)
