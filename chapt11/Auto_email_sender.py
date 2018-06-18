from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

browser = webdriver.Firefox()
browser.get("https://login.yahoo.co.jp")
email_elm = browser.find_element_by_id("username")

#email_elm.send_keys("email_address")
email_elm.send_keys("hrd_stad@yahoo.co.jp")
email_elm.submit()

password_elm = browser.find_element_by_id("passwd")
#password_elm.send_keys("mypassword")
password_elm.send_keys("k2furs93")
password_elm.submit()

new_email = browser.find_element_by_id("main-btn-new")
new_email.submit()

receiver_elm = browser.find_element_by_id("to")
receiver_elm.send_keys("reciever email address")

subject_elm = browser.find_element_by_id("subject")
receiver_elm.send_keys("test")

content_elm = browser.find_element_by_id("rtetext")
content_elm.send_keys("test")

actions = ActionChains(browser)
actions.key_down(Keys.CONTROL)
actions.key_down(Keys.ENTER)