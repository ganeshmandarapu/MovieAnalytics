from selenium import webdriver
import json
import os
import csv
import urllib2
from selenium.common.exceptions import TimeoutException

data = []
urls = []
urldata = []

with open('movie_budget_info.csv','rb') as csvfile:
	spamreader = csv.reader(csvfile,delimiter=',')
	for row in spamreader:
		data.append(row)

for x in range(1,len(data)):
	title = urllib2.quote(data[x][2])
	urls.append("http://www.imdb.com/find?ref_=nv_sr_fn&q={}&s=tt".format(title))

chromedriver = "/Users/sai teja/Downloads/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
browser = webdriver.Chrome(chromedriver)
#browser.get("http://www.the-numbers.com/movie/budgets/all")

for url in range(3000,4000):
	try:
		print(url)
		browser.get(urls[url])
		if len(browser.find_elements_by_xpath("//table/tbody/tr"))>0 and len(browser.find_elements_by_xpath("//table/tbody/tr")[0].find_elements_by_tag_name("td"))>1 :
			mov_tit = browser.find_elements_by_xpath("//table/tbody/tr")[0].find_elements_by_tag_name("td")[1].find_element_by_tag_name("a").text.encode('utf-8')
			mov_url = browser.find_elements_by_xpath("//table/tbody/tr")[0].find_elements_by_tag_name("td")[1].find_element_by_tag_name("a").get_attribute('href')
			urldata.append([mov_tit,mov_url])
	except TimeoutException:
		pass
	
browser.quit()

with open('movie_url_info4.csv','wb') as csvfile:
	writer = csv.writer(csvfile)
	writer.writerows(urldata)