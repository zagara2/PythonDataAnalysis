'''
Created on Mar 31, 2016

@author: Mickey
'''
import urllib2

def fileToList(quakeurl):
    ''' 
    This function will read earthquake data from a URL and return a list of strings. 
    Each string is in the format: magnitude, followed by a blank, 
    a dash and another blank, and then followed by the place of the earthquake.
    '''
    quakefile = urllib2.urlopen(quakeurl)
    final_list = []
    for line in quakefile:
        quakedatalist = line.split("$")
        magnitude = quakedatalist[0]
        otherstuff = quakedatalist[1]
        kmindex = otherstuff.find("km")
        dashindex = otherstuff.find("-")
        if kmindex > dashindex:
            kiloms = otherstuff[dashindex+1:kmindex+2]
        if dashindex > kmindex:
            kiloms = otherstuff[0:kmindex+2]
        kiloms = kiloms.strip()
        restofString = otherstuff[kmindex+3:]
        newstring = magnitude + " - " + kiloms + " " +restofString
        otherstuffstring = "".join(otherstuff)#gets used in the lines below
        if not "km" in otherstuff: #correcting for special cases, like the lines about the quakes in the Ascension Islands
            newstring = magnitude + " - " + otherstuffstring
        final_list.append(newstring.strip())
    return final_list

def fileToListBaseloc(quakeurl):
    ''' 
    This function will read earthquake data from a URL and return a list of strings. 
    Each string is the base location of a given earthquake.
    '''
    quakefile = urllib2.urlopen(quakeurl)
    final_list = []
    for line in quakefile:
        quakedatalist = line.split("$")
        locinfo = quakedatalist[1]
        splitoncomma = locinfo.split(",")
        baseloc = splitoncomma[-1]
        final_list.append(baseloc.strip())
    return final_list

def question1(quakeurl):
    '''
    Returns which base location occurs the most often in the file, and how many times it occurs.
    '''
    
    #create a dictionary mapping a base location to an integer representing how many times the base location occurs
    quakelist = fileToListBaseloc(quakeurl)
    baselocCount = {}
    for item in quakelist:
        if item not in baselocCount:
            baselocCount[item] = 1
        else:
            baselocCount[item] += 1
    
    #getting relevant info for answer
    info = baselocCount.items()
    tosort = [(t[1],t[0]) for t in info]
    info = sorted(tosort)
    info.reverse()
    answertuple = info[0]
    maxbaseloc = answertuple[1]
    numquakes = str(answertuple[0])
    answerstring = "The maximum base location with earthquakes is " + maxbaseloc + ". It had " + numquakes + " earthquakes."
    return answerstring

def question2(quakeurl):
    '''
    Calculates the highest average magnitude for whole locations that appear five or more times in the file. 
    Returns this average and also the location.
    '''
    
    #creates a dict mapping each location to a list of all its magnitudes
    quakelist = fileToList(quakeurl)
    magsforEachLoc = {} 
    for item in quakelist:
        periodindex = item.find(".")
        magnitude = item[0:periodindex+2].strip()
        wholelocation = item[periodindex+5:].strip()
        if wholelocation not in magsforEachLoc: 
            magsforEachLoc[wholelocation] = [float(magnitude)]
        else:
            magsforEachLoc[wholelocation].append(float(magnitude))
       
    #creates a dict mapping each location with 5 or more quakes to its average magnitude 
    dictofAverages = {}
    for (k,v) in magsforEachLoc.items():
        if len(v)>=5:
            dictofAverages[k] = sum(v)/len(v) #don't need if-else statement to check if k is already in dict, because no duplicate values for k 
    
    #getting relevant info for answer
    info = dictofAverages.items()
    tosort = [(t[1],t[0]) for t in info]
    info = sorted(tosort)
    info.reverse()
    answertuple = info[0]
    highestAvgMag = str(answertuple[0])
    answerloc = answertuple[1]
    answerstring = "The highest average magnitude with 5 or more quakes is " + highestAvgMag + ", which occurred at location: " + answerloc +"."
    return answerstring

def question3(quakeurl):
    '''
    Returns the Magnitude that occurs the most often and how many times it occurs 
    and in how many unique whole locations.
    '''
    
    #create a dictionary mapping each magnitude (as a string) to a list of all its locations
    quakelist = fileToList(quakeurl)
    locsforEachMag = {}
    for item in quakelist:
        periodindex = item.find(".")
        magnitude = item[0:periodindex+2].strip()
        wholelocation = item[periodindex+5:].strip()
        if magnitude not in locsforEachMag: 
            locsforEachMag[magnitude] = [wholelocation]
        else:
            locsforEachMag[magnitude].append(wholelocation)
    
    #create a dictionary mapping each magnitude to the number of times it occurs
    #then get relevant info for answer
    numOccurrences = {}
    for (k, v) in locsforEachMag.items():
        numOccurrences[k] = len(v) #don't need if-else statement to check if k is already in dict, because no duplicate values for k
    info = numOccurrences.items()
    tosort = [(t[1],t[0]) for t in info]
    info = sorted(tosort)
    info.reverse()
    answertuple = info[0]
    highestOcurrences = str(answertuple[0])
    mostPopularMag = answertuple[1]
        
    #create a dictionary mapping each magnitude to its number of unique locations
    #then get relevant info for answer (num of unique locs at key corresponding to most frequent mag)
    numUniqueLocs = {}
    for (k, v) in locsforEachMag.items():
        numUniqueLocs[k] = len(set(v)) #don't need if-else statement to check if k is already in dict, because no duplicate values for k
    relevantNum = str(numUniqueLocs.get(mostPopularMag))
    answerstring = "The magnitude that occurs the most often is " + mostPopularMag +". It occurs "+ highestOcurrences+" times in "+relevantNum+" unique locations."
    return answerstring
 
if __name__ == '__main__':
    #datafile = "http://www.cs.duke.edu/courses/spring16/compsci101/data/earthquakeDataMarch15-2016-one-month.txt"
    datafile = "http://www.cs.duke.edu/courses/spring16/compsci101/data/earthquakeSmall2.txt"
    print question1(datafile)
    print
    print question2(datafile)
    print 
    print question3(datafile)