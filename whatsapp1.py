from selenium import webdriver
import time
message=input("ENTER THE MESSAGE YOU WANT TO SEND\n")
driver=webdriver.Chrome("C:/Users/this pc/Desktop/chromewebdriver/chromedriver.exe") 
driver.get('https://web.whatsapp.com/')
time.sleep(30)



#ENTER YOUR CONTACTS IN THIS LIST
contacts=['a','b','c','d','e','f']
for i in contacts:
	driver.find_element_by_class_name('eiCXe').send_keys(i)
	driver.find_element_by_class_name('X7YrQ').click()
	time.sleep(5)
	driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]").send_keys(message)
	driver.find_element_by_class_name('_3M-N-').click()
	time.sleep(5)
driver.close()
