import requests
import os
from pprint import pprint


year = '2023'
month = '06'
day = '05'

api = "cf4e76c3690d4f7eaa0e162699e9ea33"
title = "Tesla"
domains = "wsj.com"

url = f"https://newsapi.org/v2/everything?q={title}&from={year}-{month}-{day}&domains={domains}&sortBy=publishedAt&apiKey={api}"

response = requests.get(url)
data = response.json()


articles = data.get('articles')
print(articles)
def calculate_days_between_dates(date1, date2):
    year1, month1, day1 = map(int, date1.split("-"))
    year2, month2, day2 = map(int, date2.split("-"))

    # Calculate the total number of days in each year
    days_in_year1 = 365 * year1 + year1 // 4 - year1 // 100 + year1 // 400
    days_in_year2 = 365 * year2 + year2 // 4 - year2 // 100 + year2 // 400

    # Calculate the total number of days in each month
    days_in_month1 = sum([31, 28 + (year1 % 4 == 0 and (year1 % 100 != 0 or year1 % 400 == 0)), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][:month1 - 1])
    days_in_month2 = sum([31, 28 + (year2 % 4 == 0 and (year2 % 100 != 0 or year2 % 400 == 0)), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][:month2 - 1])

    # Calculate the total number of days in each day
    days1 = days_in_year1 + days_in_month1 + day1
    days2 = days_in_year2 + days_in_month2 + day2

    # Calculate the difference in days
    difference = abs(days1 - days2)

    return difference

# Example usage
startdate = f"{year}-{month}-{day}"
now = "2023-07-05"
days_between = calculate_days_between_dates(startdate, now)

for i in range(days_between):
        
    url = f"https://newsapi.org/v2/everything?q={title}&from={year}-{month}-{day}&domains={domains}&sortBy=publishedAt&apiKey={api}"

    response = requests.get(url)
    data = response.json()


    articles = data.get('articles')
    for i in range(len(articles)):
        print(articles[i]['title'])
    if (month == '04' or  month =='06' or month == '09' or month =='11') and day == '30':
        day = "01"
        month = "0" + str((int(month) + 1))
    elif (month == "01" or month == "03" or month == "05" or month == '07' or month == "08" or month == "10" or month == "12") and day == "31":
        day = "01"
        month = "0"  + str((int(month) + 1))
    elif month == "2" and day == "28":
        month = "03"
        day = "01"
    else:
        if int(day) > 9:
            day = str(int(day) + 1)
        else:
            day = '0' + str(int(day) + 1)
    print(f'the date is {year}, {month}, {day}')
        
        

