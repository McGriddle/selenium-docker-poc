#!/usr/bin/python

from selenium import webdriver


options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
capabilities = options.to_capabilities()
driver = webdriver.Remote(
   command_executor='http://0.0.0.0:4444/wd/hub',
   desired_capabilities=capabilities)
driver.maximize_window()

driver.get("http://www.python.org")