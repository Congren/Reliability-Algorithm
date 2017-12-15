# encoding: utf-8

import string
import math
from sys import argv
from decimal import Decimal
def formDictFromText(text):
	a = {}
	for line in text:
		list = line.split()
		for word in list:
			fixed_word = word.translate(string.punctuation).lower()
			if len(fixed_word) > 0:
				if fixed_word in a:
					a[fixed_word] += 1
				else:
					a[fixed_word] = 1
	return a;
def formDictFromInput(text):
	a = {}
	list = text.split()
	for word in list:
		fixed_word = word.translate(string.punctuation).lower()
		if len(fixed_word) > 0:
			if fixed_word in a:
				a[fixed_word] += 1
			else:
				a[fixed_word] = 1
	return a;


def formDictFromFile(textFile):
	return formDictFromText(open(textFile, 'r', encoding='utf-8'))



def getWordCountFromDict(d):
	dWordCount = 0.0

	for word in d.keys():
		dWordCount += d[word]

	return dWordCount



def getEntropyFromDict(d):
	entropy = 0.0
	dWordCount = getWordCountFromDict(d)
	for word in d.keys():

		entropy += -(d[word] / dWordCount) * math.log(d[word] / dWordCount, 2)

	return entropy


def getJSDAgainst(a, b):
	abJSD = 0.0

	aWordCount = getWordCountFromDict(a);
	bWordCount = getWordCountFromDict(b);

	aEntropy = getEntropyFromDict(a);
	bEntropy = getEntropyFromDict(b);

	for word in (set(a).union(set(b))):
		ptot = 0
		if word in a:
			ptot += (a[word]/aWordCount) / 2.0
		if word in b:
			ptot += (b[word]/bWordCount) / 2.0
		abJSD += -ptot * math.log(ptot, 2)

	abJSD -= 0.5 * (aEntropy + bEntropy)

	return abJSD

	
def interpretScore(total):
	modifier = 2;
	return abs(10 - (pow(total * 100, modifier) / 2))


def mainPolitic(textf):
	democratf = "DemocratPlatform.txt"
	republicanf = "RepublicanPlatform.txt"
	#print "Political Flow: \"DemocratFile\", \"RepublicanFile\", \"StringToEvaluate\""
	prompt = '> '

	#print "DemocratFile: %s \nRepublicanFile: %s \nText: %s" % (democratf, republicanf, textf);

	demDict = formDictFromFile(democratf);
	repDict = formDictFromFile(republicanf);
	textDict = formDictFromInput(textf);

	#print demDict
	#print getWordCountFromDict(demDict)
	#print getEntropyFromDict(demDict)
	#print getEntropyFromDict(repDict)
	#print getEntropyFromDict(textDict)
	#print getWordCountFromDict(textDict)
	comA = getJSDAgainst(textDict, demDict);
	comB =	getJSDAgainst(textDict, repDict);

	score = comA - comB
	if score < 0:
		score *= -1

	#print "Score: %f" % score
	
	return "%f" % round(interpretScore(score),2)
