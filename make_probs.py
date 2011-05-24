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
            if p.name in priors:
                priors[p.name]+=(1.0)
            else:
                priors[p.name]=(1.0)
    return priors

def make_prob_table(all_pairs,priors):
    cooc={}
    for x in priors.keys(): cooc[x]={}
    print len(cooc.keys())
    for pair in all_pairs:
        print pair.n1
        currentParas=[]
        for x in pair.paraphrases:
            if x.freq>1.0: currentParas.append(x.name)
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
file=open('/home/paul/thesis/data/SemEval2Task9/SemEval2_task9_training/TRAINING_FILE_UPDATED_2.txt')
#file=open('/home/paul/thesis/data/SemEval2Task9/SemEval2_task9_testing/TEST_FILE_3.txt')
all_pairs=parse_semeval.parse_file(file)
print "Number of compounds:"
print len(all_pairs)
print "\n"
priors=make_priors(all_pairs)
probs=make_prob_table(all_pairs,priors)
for p in priors.keys():
	if priors[p]<2.0: 
		del priors[p]
		del probs[p]
print "dumping"
cPickle.dump(priors,open('/home/paul/thesis/data/pickles/trainingPriors','wb'), protocol=cPickle.HIGHEST_PROTOCOL)
cPickle.dump(probs,open('/home/paul/thesis/data/pickles/trainingProbs','wb'), protocol=cPickle.HIGHEST_PROTOCOL)
exit()

