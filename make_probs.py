'''
Created on 8 Feb 2010

@author: paul
'''
import copy
import cPickle
import random
import parse_semeval


def make_priors(all_pairs):
    priors={}
    for pair in all_pairs:
        for p in pair.paraphrases:
            print p.freq
            if p.freq<7.0: continue
            if p.name in priors:
                priors[p.name]+=(1.0)
            else:
                priors[p.name]=(1.0)
    return priors

def make_prob_table(all_pairs,priors):
    cooc={}
    print "%d compounds" % len(all_pairs)
    for x in priors.keys(): cooc[x]={}
    print len(cooc.keys())
    counter=0
    for pair in all_pairs:
        print pair.n1
        counter+=1
        print counter
        currentParas=[]
        for x in pair.paraphrases:
            if x.freq>7.0: currentParas.append(x.name)
        i=0
        while(i<len(currentParas)):
            j=0
            a=currentParas[i]
            while(j<len(currentParas)):
                if j==i:
                    j+=1
                    continue
                b=currentParas[j]
                if b in cooc[a]: cooc[a][b]+=1.0
                else: cooc[a][b]=1.0
                j+=1
            i+=1
    probs={}
    for x in cooc.keys(): probs[x]={}
    for a in cooc.keys():
        for b in cooc.keys():
            if b in cooc[a]:
                probs[a][b]=cooc[a][b]/priors[b]
            else:
                probs[a][b]=0.0
    return probs

allParaphrases={}
trainFile=open('/home/paul/mayThesis/semEvalTask9/training.txt')
testFile=open('/home/paul/mayThesis/semEvalTask9/testing.txt')
train_pairs=parse_semeval.parse_file(trainFile)
test_pairs=parse_semeval.parse_file(testFile)
all_pairs=train_pairs+test_pairs
print "Number of compounds:"
print len(all_pairs)
print "\n"
priors=make_priors(all_pairs)
totals=sorted(priors.items(), key=lambda x: x[1])
for t in totals: print t
probs=make_prob_table(all_pairs,priors)
print "dumping"
print len(priors)
cPickle.dump(priors,open('/home/paul/mayThesis/pickles/allPriors','wb'), protocol=cPickle.HIGHEST_PROTOCOL)
cPickle.dump(probs,open('/home/paul/mayThesis/pickles/allProbs','wb'), protocol=cPickle.HIGHEST_PROTOCOL)
exit()