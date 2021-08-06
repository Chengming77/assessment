
# -*- coding:utf8 -*-

import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path=r"C:\Program Files\Google\Chrome\Application\chromedriver.exe")
driver.get(r'https://olympics.com/tokyo-2020/zh/news/videos/%E4%B8%BD%E8%8E%8E-%E5%8D%A1%E6%9E%97%E9%A1%BF-%E6%88%91%E5%AF%B9%E4%BA%8E%E4%BC%9F%E5%A4%A7%E7%9A%84%E5%AE%9A%E4%B9%89')

driver.find_element_by_id("kw").send_keys(u"古力娜扎")

driver.find_element_by_id("su").click()

time.sleep(5)

driver.find_element_by_id("1").find_element_by_tag_name("a").click()

driver.find_element_by_id("kw").send_keys(u"中华民国")

