from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from collections import defaultdict

import pandas as pd
from bs4 import BeautifulSoup as bs
import re, os, time

PATH = "C:\Program Files (x86)\chromedriver.exe"
link = "https://www.ymgrad.com/admits_rejects/"
driver = ""

def saveDFToStorage(df):
	if not  os.path.exists("output"):
		# Create a new directory
		os.makedirs("output")
	output_path="output/universityData.csv"

	#Append if exists
	df.to_csv(output_path, mode='a', header=not os.path.exists(output_path))
	print("\nSave Successful!\n")

def launchBrowser():
	chrome_options = Options()
	chrome_options.add_argument("disable-infobars");
	driver = webdriver.Chrome(executable_path=PATH, chrome_options=chrome_options)  
	driver.get(link)

	#Comment below three lines to search for the whole website
	# elements = WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.XPATH, "//*[@class='form-input w-full text-dark']")))
	# elements[0].click()
	# elements[0].send_keys(searchFor,)

	time.sleep(4)
	cols = ["decision","name","location","university","program","months","papers","gre","toefl","applied_on","decision_date"]

	dict1 = defaultdict(list)
	
	#Ignore first div as it is the navigation bar thanks to the bogus HTML coder
	init_elem = driver.find_elements(By.XPATH,"//div[contains(@id,'decision')]")[1:2]
	decision_divs = set(init_elem)

	try:
		SCROLL_PAUSE_TIME = 2
		last_height = driver.execute_script("return document.body.scrollHeight")
		iters = 1000
		# iters = 10
		while iters>0:
		# while True:
			driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
			time.sleep(SCROLL_PAUSE_TIME)
			new_height = driver.execute_script("return document.body.scrollHeight")
			iters -= 1
			if new_height == last_height: continue
			last_height = new_height
			decision_divs.update(driver.find_elements(By.XPATH,"//div[contains(@id,'decision')]")[1:])
	except:
		print("\n\n\nError occurred while scrolling!\n\n\n") 

	try:
		print("Length is :", len(decision_divs))
		for div in decision_divs:
			# print("\n\nNew DIV: ", div)
			outerHTML = div.get_attribute("outerHTML")	
			soup = bs(outerHTML, "html.parser")
		
			decision = soup.select_one('div.ribbon').text
			name = soup.select_one('a[href^="/profile/"] span:first-child').text.strip()
			location = soup.select_one('a[href^="/profile/"] span:nth-of-type(2)').text
			university = soup.select_one('a[href^="/university/"] span').text
			program = soup.select_one('span.admits_rejects__exam_scores___').text
			
			match = re.search(r'(\d+)&nbsp;months', outerHTML)
			months = match.group(1) if match else "N/A"
			
			match = re.search(r'(\d+) research papers', outerHTML)
			papers = match.group(1) if match else "N/A"
			
			gre_match = re.search(r'GRE.*?(\d+V),\s*(\d+Q),\s*([\d\.]+)AWA', outerHTML)
			gre = "V{} Q{} AWA{}".format(gre_match.group(1), gre_match.group(2), gre_match.group(3)) if gre_match else "N/A"
			
			toefl_match = re.search(r'GRE.*?(\d+R),\s*(\d+S),\s*(\d+L),\s*([\d\.]+)W', outerHTML)
			toefl = "R{} S{} L{} W{}".format(toefl_match.group(1), toefl_match.group(2), toefl_match.group(3), toefl_match.group(4)) if toefl_match else "N/A"
			
			match = re.search(r'Applied on:\s*(\w+\s+\d+,\s+\d{4})', outerHTML)
			applied_on = match.group(1) if match else "N/A"
			
			match = re.search(r'Decision Date:\s*(\w+\s+\d+,\s+\d{4})', outerHTML)
			decision_date = match.group(1) if match else "N/A"
			
			dict1["decision"].append(decision)
			dict1["name"].append(name)
			dict1["location"].append(location)
			dict1["university"].append(university)
			dict1["program"].append(program)
			dict1["months"].append(months)
			dict1["papers"].append(papers)
			dict1["gre"].append(gre)
			dict1["toefl"].append(toefl)
			dict1["applied_on"].append(applied_on)
			dict1["decision_date"].append(decision_date)
			# print("\nname is :", name)
	except:
		print("Locha jhala hya dict madhe", dict1)
	finally:
		df = pd.DataFrame(dict1, columns=cols)
		saveDFToStorage(df)

	print("Done!!")
	while(True):
		pass    

launchBrowser()

