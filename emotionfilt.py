from __future__ import print_function
import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 import Features, EntitiesOptions, KeywordsOptions, EmotionOptions
from decimal import Decimal
from sys import argv
import string

def analyseEmotions(input):
	natural_language_understanding = NaturalLanguageUnderstandingV1(
		version='2017-02-27',
		username='dc251dd4-05d5-4980-b624-0eb6af20fa1b',
		password='Tjex12qXIXv1')

	#response = natural_language_understanding.analyze(
	#	text=input,
	#	features=Features(entities=EntitiesOptions(), keywords=KeywordsOptions(), emotion=EmotionOptions()))

	response = natural_language_understanding.analyze(
		text=input,
		features=Features(emotion=EmotionOptions()))
	#print(json.dumps(response, indent=2));
	#print ""
		
	anger = response["emotion"]["document"]["emotion"]["anger"]
	joy = response["emotion"]["document"]["emotion"]["joy"]
	sadness = response["emotion"]["document"]["emotion"]["sadness"]
	fear = response["emotion"]["document"]["emotion"]["fear"]
	disgust = response["emotion"]["document"]["emotion"]["disgust"]
	total = anger + joy + sadness + fear + disgust
	
	#print ("Anger: %f" % (anger));
	#print ("Joy: %f" % (joy));
	#print ("Sadness: %f" % (sadness));
	#print ("Fear: %f" % (fear));
	#print ("Disgust: %f" % (disgust));
	#print ("total: %f" % (total));
	
	return total
	

def interpretScore(total):
	modifier = 3;
	return 10 - (pow(total, modifier) / 2)
	
def mainEmote(textf):
	
	if textf == False:
		return 0.0
	#print("Emotion Filter: <input text file>")
	prompt = '> '
	
	#textFile = open(textf, 'r')
	#print(textFile.read())
	score = analyseEmotions(textf)
	# textFile.close()
	
	return "%f" % round(interpretScore(score),2)
	#return interpretScore(score)
#open(textFile, 'r')
#analyseEmotions(" You have given yourself 4 years but the commuters have given you guys more than 11 years from 2006 to 2017. 3 Transport Ministers - Raymond Lim, Lui Tuck Yew and Khaw Boon Wan. You need more time You are halfway thru yes. By the time you are thru in another 2 years will be the next GE. What wayang you going to say at that time ?")