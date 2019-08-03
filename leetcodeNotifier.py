import requests
import time
from bs4 import BeautifulSoup
from win10toast import ToastNotifier

startTime = time.time()
toaster = ToastNotifier()

while True:

	page = requests.get('https://leetcode.com/grishaster80/')
	soup = BeautifulSoup(page.text, 'html.parser')
	recent_submissions = soup.find_all('a',class_='list-group-item')
	todaySubmissions=[]
	todaySubmissionsCount = 0 
	words = ['day','days','month','months','week','weeks']
	for submission in recent_submissions:
		cur = str(submission)
		if cur.find("Accepted") != -1:
			if any(word in cur for word in words):
				pass
			else:
				todaySubmissions.append(submission)
	currentCount = len(todaySubmissions)

	if currentCount < 5:
		toaster.show_toast("LeetCode",
                   "U need to solve "+str(5-currentCount)+" more problems today",
                   duration=7)			
	print(currentCount)

	time.sleep(3600 - ((time.time() - startTime) % 3600))		