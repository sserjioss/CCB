import time
from selenium import webdriver

driver = webdriver.Chrome()

driver.get("http://10.11.0.102/login")   #Открытие браузера нужной страницы


email_field = driver.find_element_by_xpath("//input[@id='mat-input-4']") # Выбераем поле в которое будим вводить текст
email_field.send_keys("sadmin@mail.com") #Вводим текст или подставляем имя функции

password_field = driver.find_element_by_xpath("//input[@id='mat-input-5']")

password_field.send_keys("sadmin")

next_button = driver.find_element_by_xpath("//form[@name='signinForm']//button[@type='submit']")
next_button.click()

assert "Admin Panel" or "Cloud Browser" in driver.page_source

time.sleep(1)

sign_out_field = driver.find_element_by_xpath("//div[contains(text(),'Sign Out')]")

sign_out_field.click()

#driver.quit()

#next_button = driver.find_element_by_xpath("//*[@id="home"]/div/app-login/div/form/button/div[1]") # Выбираем кнопку (По id) по которой должны кликнуть
#next_button.click() # команда нажатия кнопки



