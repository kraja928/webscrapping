import pandas as pd
import requests
from bs4 import BeautifulSoup
page = requests.get('https://forecast.weather.gov/MapClick.php?lat=38.9598&lon=-77.3545')
soup = BeautifulSoup(page.content, 'html.parser')
#print(soup.find_all('a'))
week = soup.find(id='seven-day-forecast-body')
#print(week)
items = week.find_all(class_='tombstone-container')
#print(items)
#print(items[1].find(class_='period-name').get_text())
#print(items[1].find(class_='short-desc').get_text())
#print(items[1].find(class_='temp').get_text())

period_names = [item.find(class_='period-name').get_text() for item in items]
#print(period_names)
short_descriptions = [item.find(class_='short-desc').get_text() for item in items]
#print(short_descriptions)
temperatures =[item.find(class_='temp').get_text() for item in items]
#print(temperatures)
weather_stuff = pd.DataFrame(
      {
            'period': period_names,
            'short_descriptions': short_descriptions,
            'temperatures': temperatures
      })
weather_stuff.to_csv('weather.csv')