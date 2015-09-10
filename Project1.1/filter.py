import re

def answer0():
	#filter out records according to the 5 rules
	topics = "^(Media:|Special:|Talk:|User:|User_talk:|Project:|Project_talk:|File:|File_talk:|MediaWiki:|MediaWiki_talk:|Template:|Template_talk:|Help:|Help_talk:|Category:|Category_talk:|Portal:|Wikipedia:|Wikipedia_talk:)"
	fileTypes = "(\.jpg|\.gif|\.png|\.JPG|\.GIF|\.PNG|\.txt|\.ico)$"
	boilerplate = "^(404_error/|Main_Page|Hypertext_Transfer_Protocol|Search)$"

	f = open("pagecounts-20150801-000000","r")
	for line in f:
		attributes = line.split(" ")
		if (attributes[0] == "en" and (re.search(topics, attributes[1]) == None) 
			and (re.search("^[a-z]", attributes[1]) == None)
			and (re.search(fileTypes, attributes[1]) == None) 
			and (re.search(boilerplate, attributes[1]) == None)):
			print(attributes[1] + '\t' + attributes[2])
	f.close()

#Q1: how many lines (items) were originally present in the input file
def answer1():
	#go through the original file line by line
	f = open("pagecounts-20150801-000000","r")
	lineCount = 0
	for line in f:
		lineCount += 1
	print lineCount
	f.close()




#Q2: what was the total number of requests before filtering
def answer2():
	#sum up numbers of all requests in original file
	f = open("pagecounts-20150801-000000","r")
	requestCount = 0
	for line in f:
		attributes = line.split(" ")
		requestCount += int(attributes[2])
	print requestCount
	f.close()




#Q3: how many lines emerged after applying all the filters
def answer3():
	#simply count all lines in "output"
	f = open("output", "r")
	lineCount = 0
	for line in f:
		lineCount += 1
	print lineCount
	f.close()




#Q4: what was the most popular article in the filtered output
def answer4():
	#that is to go through each line to find the file 
	#with the largest number of accesses
	f = open("output", "r")
	maxRead = 0
	article = ""
	for line in f:
		attributes = line.split("\t")
		if int(attributes[1]) > maxRead:
			maxRead = int(attributes[1])
			article = attributes[0]
	print article
	f.close()




#Q5: how many views did the most popular article get
def answer5():
	#same as question4, record the number of access
	f = open("output", "r")
	maxRead = 0
	for line in f:
		attributes = line.split("\t")
		if int(attributes[1]) > maxRead:
			maxRead = int(attributes[1])
	print maxRead
	f.close()




#Q6: what is the count of the most popular movie in the filtered output
def answer6():
	#first, remain all records whose name contains "(film)" 
	#and then choose the one with the largest number of accesses
	f = open("output", "r")
	maxRead = 0
	for line in f:
		attributes = line.split("\t")
		if (re.search("\(film\)",attributes[0]) != None 
			and int(attributes[1]) > maxRead):
			maxRead = int(attributes[1])
	print maxRead
	f.close()	




#Q7: how many articles have more than 2500 views in the filtered output
def answer7():
	#select records with accesses > 2500
	f = open("output", "r")
	numArticle = 0
	for line in f:
		attributes = line.split("\t")
		if int(attributes[1]) > 2500:
			numArticle += 1
	print numArticle
	f.close()




#Q8: how many views are there in the filtered dataset for all "episode lists"
def answer8():
	#find those ones start with "List_of" and end with "episodes"
	#and sum up the accesses
	f = open("output", "r")
	totView = 0
	for line in f:
		attributes = line.split("\t")
		if (re.search("^List_of",attributes[0]) != None 
			and re.search("episodes$", attributes[0])):
			totView += int(attributes[1])
	print totView
	f.close()	




#Q9: what is most popular in this hour, "(2014_film)" or "(2015_film)" articles
def answer9():
	#count accesses for both 2014 films and 2015 films
	#and compare the numbers
	f = open("output", "r")
	film2014 = 0
	film2015 = 0
	for line in f:
		attributes = line.split("\t")
		if re.search("\(2014_film\)",attributes[0]) != None:
			film2014 += int(attributes[1])
		if re.search("\(2015_film\)",attributes[0]) != None:
			film2015 += int(attributes[1])
	if film2014 > film2015:
		print ("2014")
	else:
		print ("2015")
	f.close()	

