import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

response=requests.get("https://www.flipkart.com/search?q=mobile+phones+under+20000&as=on&as-show=on&otracker=AS_Query_HistoryAutoSuggest_1_3_na_na_na&otracker1=AS_Query_HistoryAutoSuggest_1_3_na_na_na&as-pos=1&as-type=HISTORY&suggestionId=mobile+phones+under+20000&requestId=ec2e710d-56cd-45d3-92ea-463e15896cb2&as-searchtext=mob")
print("Response Status |"+str(response.status_code))


my_dict={"Name":[],"Price":[],"specification":[],"Rating":[]}
text=response.text
soup=BeautifulSoup(text)
#soup=soup.findAll("script")[7]
for data in soup.findAll("div",class_='_3pLy-c row'):
        my_dict["Name"].append(str(data.find('div', attrs={'class':'_4rR01T'}).text))
        my_dict["Price"].append(str(data.find('div', attrs={'class':'_30jeq3 _1_WHN1'}).text))
        my_dict["specification"].append(str(data.find('div', attrs={'class':'fMghEO'}).text))
        my_dict["Rating"].append(str(data.find('div', attrs={'class':'_3LWZlK'}).text))
df=pd.DataFrame({"Name":my_dict["Name"], "Price": my_dict["Price"], "Specification": my_dict["specification"], "Rating":my_dict["Rating"] })
print(df)
df.to_csv("flipkart.csv")