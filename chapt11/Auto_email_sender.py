from selenium import webdriver

browser = webdriver.Firefox()
browser.get("https://login.yahoo.co.jp/config/login?.src=ym&.done=https%3A%2F%2Fmail.yahoo.co.jp%2F")
email_elm = browser.find_element_by_id("username")
email_address = input("Input sender email address:")
email_elm.send_keys(email_address)
email_elm.submit()
password_elm = browser.find_element_by_id("passwd")
mypassword = input("Input password:")
password_elm.send_keys(mypassword)
password_elm.submit()
new_email = browser.find_element_by_id("main-btn-new")
new_email.submit()
