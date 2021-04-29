
from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
	return render(request, 'home.html')

def count(request):
	fulltext = request.GET['fulltext']

	wordlist = fulltext.split()

	worddictionary = {}

	for word in wordlist:
		if word in worddictionary:
			#Increase
			worddictionary[word] += 1
		else:
			#Add to the dictionary
			worddictionary[word] = 1

    #this is pretty much telling it to look at an index and then what order
	sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)

	#then we'll paste the variable beside worddictionary so that it calls on it
	return render(request, 'count.html', {'fulltext':fulltext, 'count':len(wordlist), 'sortedwords':sortedwords})


def about(request):
	return render(request, 'about.html')
