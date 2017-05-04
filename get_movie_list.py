from selenium import webdriver
import json
import os

data=[["id","release_date","name","production","domestic","overall"]]
chromedriver = "/Users/sai teja/Downloads/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
browser = webdriver.Chrome(chromedriver)
browser.get("http://www.the-numbers.com/movie/budgets/all")
Row_count = browser.find_elements_by_xpath("//table/tbody/tr");
for x in range(0,2):
	if x%2==1:
		all_data=Row_count[x].find_elements_by_tag_name("td")
		temp = []
		temp.append(all_data[0].text)
		temp.append(all_data[1].text)
		temp.append(all_data[2].text)
		temp.append(all_data[3].text)
		temp.append(all_data[4].text)
		temp.append(all_data[5].text)
		data.append(temp)
browser.quit()