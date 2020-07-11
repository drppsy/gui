import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("http://xdclass.net")
print(driver.title)
sleep(2)

#将鼠标移动至定位到的元素
menu_ele = driver.find_element_by_xpath("//*[@id='app']/div/div[2]/div[2]/div[1]/ul/li[1]")
sleep(2)
ActionChains(driver).move_to_element(menu_ele).perform()

#选择子菜单
sub_menu_ele = driver.find_element_by_xpath("//*[@id='app']/div/div[2]/div[2]/div[2]/div[1]/div[2]/a[1]")
sleep(2)
sub_menu_ele.click()
sleep(2)
driver.close()