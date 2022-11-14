from selenium import webdriver
from selenium.webdriver.common.by import By

PATH = "C:\Program Files\chromedriver.exe"
browser = webdriver.Chrome(PATH)
browser.get("https://www.iomfsa.im/enforcement/disqualified-directors/")

list=[]
list2=[]
# i=1
# while i<16:
# #print((browser.find_elements(By.XPATH("/html/body/div[3]/div/div/section[1]/label/text()"))).text)
# 	print((browser.find_element(By.TAG_NAME, 'p').text))
# 	i=i+1;

list=browser.find_elements(By.CLASS_NAME, 'accordion-item')
for px in list:
	list2.append(px.text)
# 	name=browser.find_element(By.XPATH,'/html/body/div[3]/div/div/section[1]/div/p[1]')
#	print(browser.find_element(By.CSS_SELECTOR,"section[aria-label='John Trevor Roche Baines'] p:nth-child(1)").text)
# 	address=browser.find_element(By.XPATH,'/html/body/div[3]/div/div/section[1]/div/p[2]')
# 	dob=browser.find_element(By.XPATH,'/html/body/div[3]/div/div/section[1]/div/p[3]')
# 	periodofdisq=browser.find_element(By.XPATH,'/html/body/div[3]/div/div/section[1]/div/p[4]')
# 	datesofdisq=browser.find_element(By.XPATH,'/html/body/div[3]/div/div/section[1]/div/p[5]')
# 	i=i+1

# print(name.text, address.text,dob.text,periodofdisq.text,datesofdisq.text)
# list2=browser.find_elements(By.CLASS_NAME,"rte")
# print(len(list2))
# print(list2[1])

# print(browser.find_element(By.XPATH,"//section[@aria-label='John Trevor Roche Baines']//p[1]").text)
# print(list2)
import json
j=json.dumps(list2, indent=4)
with open('output_q2.json','w') as f:
	f.write(j)
	f.close()