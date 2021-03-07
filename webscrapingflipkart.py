from bs4 import BeautifulSoup
import requests
import pandas as pd


import requests 
URL = "https://www.flipkart.com/search?q=mobiles&as=on&as-show=on&otracker=AS_Query_TrendingAutoSuggest_2_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_2_0_na_na_na&as-pos=2&as-type=TRENDING&suggestionId=mobiles&requestId=2203194c-3727-401c-806c-0b92d21c660e"
r = requests.get(URL) 
#print(r.content)  #It is the raw HTML content.

soup = BeautifulSoup(r.content, 'html.parser')  #HTML parser used here to retrive data in meaningful format
# print(soup.prettify()) 
desc =[]     #list created to append details here
results = soup.find_all('div',class_='_4rR01T')   #identify the div and class to extract from web
# print(results)
for result in results:
 desc.append(result.text)

price =[]   #list created to append details here
results = soup.find_all('div',class_='_30jeq3 _1_WHN1')  #identify the div and class to extract from web
# print(results)
for result in results:
 price.append(result.text)   

# print(len(desc))     #to ensure entry are same  in numbers
# print(len(price))  #to ensure entry are same  in numbers
df = {'description': desc,'price': price}  #created dictionary to store values 
data = pd.DataFrame(data=df)  #importing pandas above to display in a proper pattern

# print(data) #to check the details
data.to_csv('details.csv')  #saving file to your exiting directory in csv format

