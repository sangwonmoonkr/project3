from selenium import webdriver

header = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5)\
			AppleWebKit 537.36 (KHTML, like Gecko) Chrome",
			"Accept":"text/html,application/xhtml+xml,application/xml;\
			q=0.9,imgwebp,*/*;q=0.8"}


chrome_driver = "C:/Users/sangwon/Desktop/chromedriver_win32/chromedriver" # Your Chrome Driver path
driver = webdriver.Chrome(chrome_driver)

driver.get(url="https://www.instagram.com/bar_dossi")