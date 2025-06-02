#Harry Fisher
#Web scrapper V 7.4
#WIP


"""
This is a program to go through the link provided find a table sort through the data to take out what i
need it will then... in the future auto put it into a database for now it just prints the insert statments
"""


#right now i am using pandas because i can get it to work, later i would like to be able to do it with the xml file
#but its a bit complecated so ill work it out later
import pandas as pd

#the requests library is the standard for making HTTP requests in Python
import requests

#Beautiful Soup is a Python package for parsing HTML and XML documents in other works its used for web scrapeing
from bs4 import BeautifulSoup


#i set up a class called webScraper purely to pass the local variable objects through the methods without having to make global vairiables
#im assuming this is bad practice or incredibly inefficient but it works... 
class webScraper:
        
    #this is the actual part of the program that gets the table 
    def scrapeTable(self):
        #this is the actual part of the program that gets the xml file
        response = requests.get("https://en.wikipedia.org/wiki/Greatest_Hits_(Queen_album)")
        soup = BeautifulSoup(response.text, 'html.parser')
        #this is the part that looks through and gets the table
        self.findTable = soup.findAll('table', {'class':"tracklist"})


    def makeDataFrame(self):
        self.df=pd.read_html(str(self.findTable))
        self.df=pd.DataFrame(self.df[0])
    

    #this is here to sort throught the data and format it in the way i want 
    def sortDataFrame(self):
        #this line of code removes everything after and including the ( this is done because on the page after the title there is a bunch of junk in brackets
        self.df['Titles'] = self.df['Title'].str.split('(').str[0]
        #this line of code removes the quotation marks from around the title of the song
        self.df['Titles'] = [counter.replace('"','') for counter in self.df['Titles']]
        #this line of code removes any extra space from the start and end of the title
        self.df['Titles'] = [counter.strip() for counter in self.df['Titles']]

  
  #this is a temp test method it runs through the lists and prints them in the form of an insert statment
    def printDataFrame(self):
        for counter in range(len(self.df['Titles'])):
            print("INSERT INTO songs(title, duration, artist, genre_code")
            print(F"VALUES ('{self.df['Titles'][counter]}', '{self.df['Length'][counter]}', '{self.df['Writer(s)'][counter]}', 1);")


#assigning w to the webScraper class then calling the methods 
w = webScraper()
w.scrapeTable()
w.makeDataFrame()
w.sortDataFrame()
w.printDataFrame()