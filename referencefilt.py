from sys import argv
import nltk #Requirement
from nltk.tokenize import word_tokenize
from decimal import Decimal
#nltk.download('punkt')
#nltk.download('averaged_perceptron_tagger')

import time
import datetime
from datetime import date
from datetime import timedelta

import requests
import json

#import sets
#from sets import Set

#Takes in a title, returns only keywords
def extractKeyTitle(title):
    tokens = nltk.word_tokenize(title)
    tagged = nltk.pos_tag(tokens)

    output = "";
    for elem in tagged:
        #print elem
        #print elem[1][0]
        if elem[1][0] == 'N' or elem[1][0] == 'V' or (elem[1][0] == 'C' and elem[1][1] == 'D'):
            output += elem[0] + " "

    return output


def dateToStringYYYYmmdd(d):
    x = "";
    x += str(d.year)

    if(d.month < 10):
        x += "0"
    x += str(d.month)

    if(d.day < 10):
        x += "0"
    x += str(d.day)

    return x


def stringToDate(strDate):
    year = int(strDate[4:])
    month = int(strDate[:2])
    day = int(strDate[2:4])
    #print("%i | %i | %i" % (day, month, year))
    return date(year, month, day)


def getUpperDateLimit(d):
    return d + timedelta(days=5)


def getLowerDateLimit(d):
    return d - timedelta(days=5)


def getLowerDateFromToday(d):
    return (date.today() - d).days


def getGoogleResultsJSON(title, d):
    engOne = "https://www.googleapis.com/customsearch/v1?key=AIzaSyCZvkvFWJhWve0f85-DnxOjAaGdS1fjHfg&cx=010700765340652524205:stzoqu1t-oo&q="
    engOne += title + "&sort=date:r:" + dateToStringYYYYmmdd(getLowerDateLimit(d)) + ":" + dateToStringYYYYmmdd(getUpperDateLimit(d))
    #print engOne

    response = requests.get(engOne)
    print
    #print response.status_code
    #print response.content

    data = response.json()
    #print(type(data))
    #print len(data["items"])


    return data


def extractSourcesToSet(jsonData):
    sourceList = []
    cleanSourceList = []

    if "items" not in jsonData:
        return cleanSourceList

    for elem in jsonData["items"]:
        sourceList.append(elem["link"])
        #print elem["title"]
        #print elem["link"]

    for source in sourceList:
        candidate = source.split("//")[1].split("/")[0]
        if candidate not in cleanSourceList:
            cleanSourceList.append(source.split("//")[1].split("/")[0])
        #print source.split("//")[1].split("/")[0]

    #for source in cleanSourceList:
    #    print source

    return cleanSourceList


def calRelScore(sourceList):
    rIndex = dict()
    rIndex["www.nytimes.com"] = 9
    rIndex["www.cnn.com"] = 8
    rIndex["www.foxnews.com"] = 7
    rIndex["www.huffingtonpost.com"] = 6
    rIndex["www.washingtonpost.com"] = 5

    maxScore = 0.0
    for val in rIndex.values():
        maxScore += val

    attainedScore = 0.0
    for source in sourceList:
        if source in rIndex.keys():
            attainedScore += rIndex[source]

    attainedScore = attainedScore / maxScore * 10

    return attainedScore

#Main?
def mainRef(title, date):
    #print "Filter Flow: \"Title\", \"MMddYYYY\""
    #prompt = '> '
    #print "Title: %s \nDate: %s" % (title, date);
    d = stringToDate(date)
    jsonDataFromSearch = getGoogleResultsJSON(extractKeyTitle(title), d)
    sourceList = extractSourcesToSet(jsonDataFromSearch)

    return [title, d, round(calRelScore(sourceList),2)]


#d = stringToDate("""11052017""")
#print(d)
#print(getUpperDateLimit(d))
#print(getLowerDateFromToday(getLowerDateLimit(d)))
