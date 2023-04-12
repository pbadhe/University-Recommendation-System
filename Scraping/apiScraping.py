import requests
import json, urllib

url = 'https://www.ymgrad.com/api/get_decisions/'
headers = '''Accept: application/json, text/plain, */*
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjgxMjU2NzM0LCJqdGkiOiJlMmRlNmEyMDdkODA0ZmMwYjVkODQ3NjkwZjliZDQzMiIsInVzZXJfaWQiOjI0OTU2MX0.o6MrxBvxVu1vnbIHSPpmIaf3uwPFvHwdJyWUrWBxT3Y
Connection: keep-alive
Content-Length: 239
Content-Type: application/json
Cookie: _gid=GA1.2.1211365175.1681235392; twk_idm_key=jyFuAmQx8kw8g_fG8bUA1; sessionid=zvx7r3kws718su4nnxicnmsk9j35ab7y; _ga=GA1.1.283536451.1681235392; _ga_PLNXCPLD5S=GS1.1.1681235392.1.1.1681243295.0.0.0; csrftoken=spa9zLLmc0SgyeHt8wh4Tb4RdzKZd2OOoHr8IP0dzxEgxCqZuGmiC59LppXr8mMx; TawkConnectionTime=0; twk_uuid_5eb45a21a1bad90e54a2b203=%7B%22uuid%22%3A%221.1hH0Cjtv6yCMV3WwtnfWeC7SeNGOqtJEIW4fX4leP0mklyJkf5EFB3PmXArQ76E1Xwai09mINkbFXgwQHYvrGZ6sUf0S7tLqLpGjoo9xkEU67eaOOVF%22%2C%22version%22%3A3%2C%22domain%22%3A%22ymgrad.com%22%2C%22ts%22%3A1681248188484%7D
Host: www.ymgrad.com
Origin: https://www.ymgrad.com
Referer: https://www.ymgrad.com/admits_rejects/
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36
X-CSRFToken: spa9zLLmc0SgyeHt8wh4Tb4RdzKZd2OOoHr8IP0dzxEgxCqZuGmiC59LppXr8mMx
sec-ch-ua: "Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Windows"
'''

def getHeaders(headerString):
	return dict(header.split(': ') for header in headerString.split('\n') if header)

def changeContentLength(headerDict, pageNo):
	curr = int(headerDict["Content-Length"])
	temp = 0
	if 10 <= pageNo <= 99:
		temp += 1
	elif 100 <= pageNo <= 999: 
		temp += 2
	elif 1000 <= pageNo <= 9999:
		temp += 3
	headerDict["Content-Length"] = str(curr+temp)
	print(headerDict["Content-Length"], type(headerDict["Content-Length"]))
	return headerDict

def getPayload(pageNo):
	return {"uni_slug":None,"major":None,"decision_type":"","page":pageNo,"user":"danny_shah","country":None,"no_gre_gmat":0,"is_undergrad":1,"is_masters":1,"is_phd":1,"spring":1,"summer":1,"fall":1,"with_funding":0,"cgpa_range_ll":0,"cgpa_range_ul":100}

def saveToStorage(lst, fName, writeOrAppend):
	with open('output/' + fName + '.json', writeOrAppend, encoding='utf-8') as f:
		json.dump(lst, f, ensure_ascii=False, indent=4)

def updateHeaders(session, pageNo):
	session.headers.update(changeContentLength(getHeaders(headers), pageNo))
	session.headers.pop('User-Agent', None)
	session.headers.pop('Accept-Encoding', None)
	return session

def process(startPage, apiCalls, outputFileName):
	finalDecisions = []
	f = open('output/' + outputFileName + '.json', 'a')
	try:
		session = requests.Session()
		updateHeaders(session, startPage)

		for pageNo in range(startPage, apiCalls+1):
			if pageNo in (10, 100, 1000):
				updateHeaders(session, pageNo)

			responseJson = session.post(url, json=getPayload(pageNo)).json()
			print("Page: ",responseJson["page"], " iter: ",pageNo)
			finalDecisions += responseJson["decisions"]
			json.dump(responseJson["decisions"], f, ensure_ascii=False, indent=4)

	except Exception as ex:
		print("Error occured while saving APIs ", ex)
	finally:
		f.close()
		saveToStorage(finalDecisions, outputFileName+"_backup", "w")

'''NOTE: 
1. The Authorization tokens will expire every 15 minutes. Fetch the new token after logging in by inspecting get_decisions/ API.
2. Look at the last iteration, continue the startPage number thereafter. 
'''

startPage = 1 
noOfAPICalls = 1884
outputFileName = "decisions"
process(startPage, noOfAPICalls, outputFileName)