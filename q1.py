from selenium import webdriver
from selenium.webdriver.common.by import By
import json

PATH = "C:\Program Files\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.mpf.mp.br/ac/institucional/procuradores")

person=[]
#innitialize empty dict , populate in following lines
person.append({
	'fullname':driver.find_element(By.XPATH,'/html/body/div[3]/div[1]/div/div[2]/div[2]/div/div[4]/div/div/div/div[1]/span/b').text,
	'careerInfoDesignation':driver.find_element(By.XPATH,'/html/body/div[3]/div[1]/div/div[2]/div[2]/div/div[4]/div/div/div/div[2] ').text
	})
person.append({
	'fullname':driver.find_element(By.XPATH,'/html/body/div[3]/div[1]/div/div[2]/div[2]/div/div[4]/div/div/div/div[4]/span/b').text,
	'careerInfoDesignation':'Procurador Regional Eleitoral (PRE)'#xpath ending with text() giving errors
	})
person.append({
	'fullname':driver.find_element(By.XPATH,'/html/body/div[3]/div[1]/div/div[2]/div[2]/div/div[4]/div/div/div/div[6]/b').text,
	'careerInfoDesignation':'Procurador Regional dos Direitos do Cidadão'#used copyOuterHTML
	})
person.append({
	'fullname':driver.find_element(By.XPATH,'/html/body/div[3]/div[1]/div/div[2]/div[2]/div/div[4]/div/div/div/div[8]/span/b').text,
	'careerInfoDesignation':driver.find_element(By.XPATH,'/html/body/div[3]/div[1]/div/div[2]/div[2]/div/div[4]/div/div/div/div[9]').text
	})
person.append({
	'fullname':driver.find_element(By.XPATH,'/html/body/div[3]/div[1]/div/div[2]/div[2]/div/div[4]/div/div/div/div[11]/span/b').text,
	'careerInfoDesignation':'Procurador da República'
	})

jx=json.dumps(person, indent=4)
with open('output_q1.json','w') as f:
	f.write(jx)
	f.close()