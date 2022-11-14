# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import json
# from googletrans import Translator

# PATH = "C:\Program Files\chromedriver.exe"
# driver = webdriver.Chrome(PATH)

# driver.get("https://www.mpf.mp.br/ac/institucional/procuradores")
# # print(driver.title)
# # driver.quit()
# tx=Translator()

# # /html/body/div[3]/div[1]/div/div[2]/div[2]/div/div[4]/div/div/div
# # #parent-fieldname-text-472eb2a769e641dda43e04b348addaf7                                //*[@id="parent-fieldname-text-472eb2a769e641dda43e04b348addaf7"]

# # /html/body/div[3]/div[1]/div/div[2]/div[2]/div/div[4]/div/div/div/div[1]/span/b        //*[@id="parent-fieldname-text-472eb2a769e641dda43e04b348addaf7"]/div[1]/span/b
# # /html/body/div[3]/div[1]/div/div[2]/div[2]/div/div[4]/div/div/div/div[2]               //*[@id="parent-fieldname-text-472eb2a769e641dda43e04b348addaf7"]/div[2]
# #                                                                                        //*[@id="parent-fieldname-text-472eb2a769e641dda43e04b348addaf7"]/div[3]
# person={}

# print(driver.find_element(By.XPATH,'/html/body/div[3]/div[1]/div/div[2]/div[2]/div/div[4]/div/div/div/div[1]/span/b').text)
# print(driver.find_element(By.XPATH,'/html/body/div[3]/div[1]/div/div[2]/div[2]/div/div[4]/div/div/div/div[2] ').text)
# person['no1']={
# 	'fullname':driver.find_element(By.XPATH,'/html/body/div[3]/div[1]/div/div[2]/div[2]/div/div[4]/div/div/div/div[1]/span/b').text,
# 	'careerInfoDesignation':driver.find_element(By.XPATH,'/html/body/div[3]/div[1]/div/div[2]/div[2]/div/div[4]/div/div/div/div[2] ').text
# 	}
# #tx.translate(tword,dest="en")
# # /html/body/div[3]/div[1]/div/div[2]/div[2]/div/div[4]/div/div/div/div[4]/span/b        //*[@id="parent-fieldname-text-472eb2a769e641dda43e04b348addaf7"]/div[4]/span/b
# # /html/body/div[3]/div[1]/div/div[2]/div[2]/div/div[4]/div/div/div/div[4]/span/text()   //*[@id="parent-fieldname-text-472eb2a769e641dda43e04b348addaf7"]/div[4]/span/text()
# #                                                                                        //*[@id="parent-fieldname-text-472eb2a769e641dda43e04b348addaf7"]/div[5]
# person['no2']={
# 	'fullname':driver.find_element(By.XPATH,'/html/body/div[3]/div[1]/div/div[2]/div[2]/div/div[4]/div/div/div/div[4]/span/b').text,
# 	'careerInfoDesignation':'Procurador Regional Eleitoral (PRE)'
# 	}
# # /html/body/div[3]/div[1]/div/div[2]/div[2]/div/div[4]/div/div/div/div[6]/b             //*[@id="parent-fieldname-text-472eb2a769e641dda43e04b348addaf7"]/div[6]/b
# # /html/body/div[3]/div[1]/div/div[2]/div[2]/div/div[4]/div/div/div/div[6]/text()        //*[@id="parent-fieldname-text-472eb2a769e641dda43e04b348addaf7"]/div[6]/text()
# #                                                                                        //*[@id="parent-fieldname-text-472eb2a769e641dda43e04b348addaf7"]/div[7]
# person['no3']={
# 	'fullname':driver.find_element(By.XPATH,'/html/body/div[3]/div[1]/div/div[2]/div[2]/div/div[4]/div/div/div/div[6]/b').text,
# 	'careerInfoDesignation':'Procurador Regional dos Direitos do Cidadão'
# 	}
# # /html/body/div[3]/div[1]/div/div[2]/div[2]/div/div[4]/div/div/div/div[8]/span/b        //*[@id="parent-fieldname-text-472eb2a769e641dda43e04b348addaf7"]/div[8]/span/b
# # /html/body/div[3]/div[1]/div/div[2]/div[2]/div/div[4]/div/div/div/div[9]               //*[@id="parent-fieldname-text-472eb2a769e641dda43e04b348addaf7"]/div[9]
# #                                                                                        //*[@id="parent-fieldname-text-472eb2a769e641dda43e04b348addaf7"]/div[10]
# person['no4']={
# 	'fullname':driver.find_element(By.XPATH,'/html/body/div[3]/div[1]/div/div[2]/div[2]/div/div[4]/div/div/div/div[8]/span/b').text,
# 	'careerInfoDesignation':driver.find_element(By.XPATH,'/html/body/div[3]/div[1]/div/div[2]/div[2]/div/div[4]/div/div/div/div[9]').text
# 	}
# # /html/body/div[3]/div[1]/div/div[2]/div[2]/div/div[4]/div/div/div/div[11]/span/b/text()//*[@id="parent-fieldname-text-472eb2a769e641dda43e04b348addaf7"]/div[11]/span/b/text()
# # /html/body/div[3]/div[1]/div/div[2]/div[2]/div/div[4]/div/div/div/div[11]/span/text()  //*[@id="parent-fieldname-text-472eb2a769e641dda43e04b348addaf7"]/div[11]/span/text()
# person['no5']={
# 	'fullname':driver.find_element(By.XPATH,'/html/body/div[3]/div[1]/div/div[2]/div[2]/div/div[4]/div/div/div/div[11]/span/b').text,
# 	'careerInfoDesignation':'Procurador da República'
# 	}
# # 
# # ox=tx.translate('gerente de sistemas',dest="en")
# # print(ox)
# # generate_output={
# # 	[{
# # 	"fullname":(driver.find_element(By.XPATH,'*[@id="parent-fieldname-text-472eb2a769e641dda43e04b348addaf7"]/div[1]/span/b')).text,
# # 	"careerInfoDesignation":tx.translate(driver.find_element(By.XPATH,'//*[@id="parent-fieldname-text-472eb2a769e641dda43e04b348addaf7"]/div[2]').text,dest="en")
# # 	},
# # 	{
# # 	"fullname":(driver.find_element(By.XPATH,'*[@id="parent-fieldname-text-472eb2a769e641dda43e04b348addaf7"]/div[4]/span/b')).text,
# # 	"careerInfoDesignation":tx.translate(driver.find_element(By.XPATH,'*[@id="parent-fieldname-text-472eb2a769e641dda43e04b348addaf7"]/div[4]/span/text()').text,dest="en")
# # 	},
# # 	{
# # 	"fullname":(driver.find_element(By.XPATH,'*[@id="parent-fieldname-text-472eb2a769e641dda43e04b348addaf7"]/div[1]/span/b')).text,
# # 	"careerInfoDesignation":tx.translate(driver.find_element(By.XPATH,'//*[@id="parent-fieldname-text-472eb2a769e641dda43e04b348addaf7"]/div[2]').text,dest="en")
# # 	},
# # 	{
# # 	"fullname":(driver.find_element(By.XPATH,'*[@id="parent-fieldname-text-472eb2a769e641dda43e04b348addaf7"]/div[1]/span/b')).text,
# # 	"careerInfoDesignation":tx.translate(driver.find_element(By.XPATH,'//*[@id="parent-fieldname-text-472eb2a769e641dda43e04b348addaf7"]/div[2]').text,dest="en")
# # 	},
# # 	{
# # 	"fullname":(driver.find_element(By.XPATH,'*[@id="parent-fieldname-text-472eb2a769e641dda43e04b348addaf7"]/div[1]/span/b')).text,
# # 	"careerInfoDesignation":tx.translate(driver.find_element(By.XPATH,'//*[@id="parent-fieldname-text-472eb2a769e641dda43e04b348addaf7"]/div[2]').text,dest="en")
# # 	}]
# # }



# # j=json.dumps(generate_output)
# # with open('output_q1.json','w') as f:
# # 	f.write(j)
# # 	f.close()

# # g_out={
# # "attorneys":
# # [
# # 	{
# # 	"name":"tom",
# # 	"post":"delivery"
# # 	},
# # 	{
# # 	"name":"jay",
# # 	"post":"manager"
# # 	}
# # ]
# # }
# print(person)
# jx=json.dumps(person, indent=4)
# print(jx)


from googletrans import Translator, LANGUAGES

tx=Translator(to_lang="en")

# print(tx.detect("Procurador Regional dos Direitos do Cidadao"))
t=tx.translate('Procurador Regional dos Direitos do Cidadão')
print(t.text)