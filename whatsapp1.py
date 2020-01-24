from selenium import webdriver
import time
driver=webdriver.Chrome("C:/Users/this pc/Desktop/chromewebdriver/chromedriver.exe") 
driver.get('https://web.whatsapp.com/')
time.sleep(30)




contacts=['monish','sudeep','akhiless','haarika','howle','chakra']
for i in contacts:
	driver.find_element_by_class_name('eiCXe').send_keys(i)
	driver.find_element_by_class_name('X7YrQ').click()
	time.sleep(5)
	driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]").send_keys('hello')
	driver.find_element_by_class_name('_3M-N-').click()
	time.sleep(5)
driver.close()