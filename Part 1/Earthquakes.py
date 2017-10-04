'''
Created on Feb 8, 2016

@author: Mickey

The comments describing what the functions do are written inside the functions. 
Just click the plus sign to the left of each function!
'''
import urllib2
import random

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
        kiloms = otherstuff[dashindex+1:kmindex+2]
        kiloms = kiloms.strip()
        restofString = otherstuff[kmindex+3:]
        newstring = magnitude + " - " + kiloms + " " +restofString
        otherstuffstring = "".join(otherstuff)#gets used in the lines below
        if not "km" in otherstuff: #correcting for special cases, like the lines about the quakes in the Ascension Islands
            newstring = magnitude + " - " + otherstuffstring
        final_list.append(newstring.strip())
    return final_list

def printQuakes(quakelist, numquakestrings):
    '''
    This function is given a formatted list of strings of earthquakes  
    and a number. If the number is -1, then it
    prints each earthquake string in the list, one per line. 
    If the number is 1 or more, then it prints only that many earthquake strings, 
    starting with the first one in the list. 
    If the number is larger than the number of earthquake strings then it prints 
    all the earthquake strings. 
    '''
    if numquakestrings == -1:
        for x in quakelist:
            print x
    if numquakestrings >= 1 and not numquakestrings > len(quakelist):
        for x in range(numquakestrings):
            print quakelist[x]
    if numquakestrings > len(quakelist):
        for x in quakelist:
            print x

            
def bigQuakes(magnitudetoBeat, quakelist):
    '''
    This function is given a decimal number and 
    a formatted list of earthquake strings. 
    It returns a list of earthquake strings whose earthquakes have magnitude 
    equal or greater than the parameter number.
    '''
    listofbigquakes = []
    for x in quakelist:
        magnitude = x[0:3]
        floatmagnitude = float(magnitude)
        if floatmagnitude >= magnitudetoBeat:
            listofbigquakes.append(x)
    return listofbigquakes

def locationQuakes(location, quakelist):
    '''
    This function is given a String representing a place, 
    and a list of formatted earthquake strings. 
    The function returns a list of earthquake strings whose earthquakes 
    were in this place. For example, if place is "Alaska", then 
    the function returns all the earthquake strings that have Alaska 
    in their location.
    '''
    listofquakesinlocation = []
    for x in quakelist:
        stringlist = x.split(",")
        place = stringlist[-1].strip()
        if "," not in x: #correcting for special cases, like the lines about the quakes in the Ascension Islands
            dashindex = x.find("-")
            place = x[dashindex+2:]
        if place.lower() == location.lower():
            listofquakesinlocation.append(x)
    
    return listofquakesinlocation
            
def question1(quakeurl):
    '''
    This function returns the answer to question 1. It calls other functions 
    created above.
    '''
    quakelist = fileToList(quakeurl)
    greatestmag = 0 
    for x in quakelist:
        magnitude = x[0:3]
        floatmagnitude = float(magnitude)
        if floatmagnitude > greatestmag:
            greatestmag = floatmagnitude
    bigquakeinfo = bigQuakes(greatestmag, quakelist)
    bigquakeinfoString = ' '.join(bigquakeinfo)
    return bigquakeinfoString

def question2(quakeurl):
    '''
    This function returns the answer to question 2. It calls other functions created
    above.
    '''
    quakelist = fileToList(quakeurl)
    allAlaskaQuakes = locationQuakes("Alaska", quakelist)
    if allAlaskaQuakes == []:
        print "No earthquakes in Alaska!"#take out? formatted right?
        return printQuakes(allAlaskaQuakes, 10)
    else:
        return printQuakes(allAlaskaQuakes, 10)
    

def question3(quakeurl):
    '''
    This function returns the answer to question 3. It calls other functions
    created above.
    '''
    quakelist = fileToList(quakeurl)
    allNZQuakes = locationQuakes("New Zealand", quakelist)
    numNZquakes = len(allNZQuakes)
    return  numNZquakes 

def question4(quakeurl):
    '''
    This function returns the answer to question 4
    '''
    quakelist = fileToList(quakeurl)
    allCaliQuakes = locationQuakes("California", quakelist)
    bigQuakesCali = bigQuakes(2.1, allCaliQuakes)
    #since bigquakes does >=, and the nums in these files have 1 decimal,
    #should we start at 2.1 here?
    numBigQuakesCali = len(bigQuakesCali)
    allCAQuakes = locationQuakes("CA", quakelist)#correcting for when California is written as CA
    bigQuakesCA = bigQuakes(2.1, allCAQuakes)
    numBigQuakesCA = len(bigQuakesCA)
    ultimate_sum = numBigQuakesCA + numBigQuakesCali
    return ultimate_sum 

def question5(quakeurl):
    '''
    This function returns the answer to question 5
    '''
    quakelist = fileToList(quakeurl)
    allCaliQuakes = locationQuakes("California", quakelist)
    bigQuakesCali = bigQuakes(1.0, allCaliQuakes)
    allCAQuakes = locationQuakes("CA", quakelist)#correcting for when California is written as CA
    bigQuakesCA = bigQuakes(1.0, allCAQuakes)
    bigquaketotal_list = bigQuakesCA + bigQuakesCali
    random.shuffle(bigquaketotal_list)
    if bigquaketotal_list == []:
        print "No earthquakes found!"#take out? formatted right?
        return printQuakes(bigquaketotal_list, 10)
    else:
        return printQuakes(bigquaketotal_list, 10)

def question6(quakeurl):
    '''
    This function returns the answer to question 6
    '''
    quakelist = fileToList(quakeurl)
    allOklaQuakes = locationQuakes("Oklahoma", quakelist)
    bigQuakesOkla = bigQuakes(3.1, allOklaQuakes)
    if bigQuakesOkla == []:
        print "No earthquakes found!"#take out? formatted right?
        return printQuakes(bigQuakesOkla, 10)
    else:
        return printQuakes(bigQuakesOkla, 10)
    

def question7(quakeurl):
    '''
    This function returns the answer to question 7
    '''
    quakelist = fileToList(quakeurl)
    allIndoQuakes = locationQuakes("Indonesia", quakelist)
    greatestmag = 0 
    for x in allIndoQuakes:
        magnitude = x[0:3]
        floatmagnitude = float(magnitude)
        if floatmagnitude > greatestmag:
            greatestmag = floatmagnitude
    bigquakeinfo = bigQuakes(greatestmag, allIndoQuakes)
    bigquakeinfoString = ' '.join(bigquakeinfo)
    if bigquakeinfo == []:
        print "No earthquakes in Indonesia!"#take out? formatted right?
        return bigquakeinfoString#will it print a blank line below the print statement if you print the function?
    else:
        return bigquakeinfoString  
        
    
if __name__ == '__main__':
    datafile = "http://www.cs.duke.edu/courses/spring16/compsci101/data/earthquakeDataFeb-1-2016-past30days.txt"
    #datafile = "http://www.cs.duke.edu/courses/spring16/compsci101/data/earthquakeDataSmall.txt"
    print "The largest magnitude earthquake in the file is:" 
    print question1(datafile)
    print 
    print "The first 10 earthquakes in the file in Alaska are:"
    question2(datafile)#style points? if some print and some don't bc some utilize printQuakes?
    print 
    print "There were this many earthquakes in New Zealand:"
    print question3(datafile)
    print
    print "This many earthquakes happened in California that were larger than 2.0:"
    print question4(datafile)
    print
    print "Here are ten random earthquakes that happened in California of magnitude 1.0 or larger:"
    question5(datafile) 
    print
    print "Here are the first 10 earthquakes in the file that have magnitude larger than 3.0 that happened in Oklahoma:"
    question6(datafile)
    print 
    print "The largest magnitude earthquake that happened in Indonesia is:"
    print question7(datafile)
   

        
        