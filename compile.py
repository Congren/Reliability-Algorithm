import datetime
from politicfilt import *
from emotionfilt import *
from referencefilt import *
import newspaper
from newspaper import Article
import csv
def getArticles():
	now = datetime.datetime.now()
	date = str(now.month) + str(now.day) + str(now.year)
	bbc_paper = newspaper.build('http://bbc.co.uk', memoize_articles=False)
	nypost_paper = newspaper.build('http://nypost.com', memoize_articles=False)
	espn_paper = newspaper.build('http://espn.com', memoize_articles=False)
	huffington_paper = newspaper.build('http://huffingtonpost.com', memoize_articles=False)
	print ("built")
	papers = [bbc_paper, nypost_paper, espn_paper, huffington_paper]
	print (len(papers))
	for paper in papers:
		counter = 0
		compiled = [["title", "date", "source", "description", "emotional", "political", "consensus", "author", "pic", "created_at", "update_at"]]
		for article in paper.articles:
			print ("getting article")
			article.download()
			print ("downloaded")
			parsed = article.parse()
			print ("parsed")
			url = article.url or "doesn't exist"
			title = article.title or "doesn't exist"
			description = article.text or "doesn't exist"
			authors = article.authors or ["doesn't exist"]
			image = article.top_image or "https://cdn.cjr.org/wp-content/themes/cjr2017/_resources2015/img/category_circles/circle_business_of_news.png"
			print ("title: " + title)
			print (description)
			refScore = mainRef(title, date)
			emotionalScore = mainEmote(description)
			politicalScore = mainPolitic(description)
			compiled.append([refScore[0], refScore[1], url, description, emotionalScore, politicalScore, refScore[2], authors[0], image, date.today(), date.today()])
			counter += 1
			if counter == 5:
				fileName = "output%s.csv" % paper.brand
				print (compiled)
				with open(fileName, "w", encoding="utf-8") as f:
	 				writer = csv.writer(f)
	 				writer.writerows(compiled)
	 				break
	return compiled
getArticles()
