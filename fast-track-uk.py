# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 10:43:45 2019

@author: admin
"""

# import libraries
import urllib.request
from bs4 import BeautifulSoup
import csv


# specify the url
urlpage =  'http://www.fasttrack.co.uk/league-tables/tech-track-100/league-table/' 
print(urlpage)
# query the website and return the html to the variable 'page'
page = urllib.request.urlopen(urlpage)
print(page)
# parse the html using beautiful soup and store in variable 'soup'
soup = BeautifulSoup(page, 'html.parser')
print(soup)
# find results within table
table = soup.find('table', attrs={'class': 'tableSorter2'})
results = table.find_all('tr')
print('Number of results', len(results))
results

# create and write headers to a list 
rows = []
rows.append(['Rank', 'Company Name', 'Webpage', 'Description', 'Location',
             'Year end', 'Annual sales rise over 3 years', 'Sales £000s', 'Staff', 'Comments'])

type(rows)
type(results)
# loop over results
for result in results:
    # find all columns per result
    data = result.find_all('td')
    data
    #data[0].getText()
    # check that columns have data 
    if len(data) == 0: 
        continue
    
    # write columns to variables
    rank = data[0].getText()
    company = data[1].getText()
    location = data[2].getText()
    yearend = data[3].getText()
    salesrise = data[4].getText()
    sales = data[5].getText()
    staff = data[6].getText()
    comments = data[7].getText()
    
    # print('Company is', company)
    # Company is WonderblyPersonalised children's books
    # print('Sales', sales)
    # Sales *25,860
    
    # extract description from the name
    companyname = data[1].find('span', attrs={'class':'company-name'}).getText()
    companyname
    data[1].getText()
    description = companyname.replace(companyname, '')
    description
   
    # remove unwanted characters
    sales = sales.strip('*').strip('†').replace(',','')
    
    # go to link and extract company website
    #url = data[1].find('a').get('href')
    #page = urllib.request.urlopen(url)
    # parse the html using beautiful soup and store in variable 'soup'
    #soup = BeautifulSoup(page, 'html.parser')
    # find the last result in the table and get the link
    try:
        tableRow = soup.find('table').find_all('tr')[-1]
        webpage = tableRow.find('a').get('href')
    except:
        webpage = None
    
    # write each result to rows
    rows.append([rank, companyname, webpage, description, location, yearend, salesrise, sales, staff, comments])
print(rows)
type(rows)

    
## Create csv and write rows to output file
with open('TrackHello.csv','w', newline='') as f_output:
    csv_output = csv.writer(f_output)
    csv_output.writerows(rows)