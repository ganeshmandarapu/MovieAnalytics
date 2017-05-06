from selenium import webdriver
import json
import os
import csv

data=[["id","release_date","name","production","domestic","overall"]]
chromedriver = "/Users/sai teja/Downloads/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
browser = webdriver.Chrome(chromedriver)
browser.get("http://www.the-numbers.com/movie/budgets/all")
Row_count = browser.find_elements_by_xpath("//table/tbody/tr")
for x in range(0,len(Row_count)):
	if x%2==1:
		print(x)
		all_data=Row_count[x].find_elements_by_tag_name("td")
		temp = []
		temp.append(all_data[0].text.encode('utf-8'))
		temp.append(all_data[1].text.encode('utf-8'))
		temp.append(all_data[2].text.encode('utf-8'))
		temp.append(all_data[3].text.encode('utf-8'))
		temp.append(all_data[4].text.encode('utf-8'))
		temp.append(all_data[5].text.encode('utf-8'))
		data.append(temp)
with open('movie_budget_info.csv','wb') as csvfile:
	writer = csv.writer(csvfile)
	writer.writerows(data)
browser.quit()