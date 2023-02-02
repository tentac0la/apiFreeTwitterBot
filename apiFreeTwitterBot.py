
import time
import random

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager



#Add additional tweets to this list. Triple-single quote is only employed to prevent escapes.
tweetList = ['''...I dunno, I have a problem with every single thing I'm hearing right now.''',
			'''I don't know who gave you that idea, but Fixers are anything but noble or heroic. The only scent you'll smell is the miserable stink of wage slaves.''']

tweet = random.choice(tweetList)
print('Tweeting the Following:')
print(tweet)

#Selects the web driver, gets the site, and tells the user.
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://twitter.com/i/flow/login")
time.sleep(1)

#For the below username and password, 
#It may be best to save these as local vars rather than hardcode.
loginElement = driver.find_element_by_xpath("//input[@name='text']")
loginElement.send_keys("username_goes_here_but_local_var_recommended")
loginElement.send_keys(Keys.ENTER)
time.sleep(1)
passElement = driver.find_element_by_xpath("//input[@name='password']")
passElement.send_keys("password_goes_here_but_local_var_recommended")
passElement.send_keys(Keys.ENTER)
time.sleep(3)


#driver.find_element_by_class_name('public-DraftStyleDefault-block').click()
tweetElement = driver.find_element_by_class_name('public-DraftStyleDefault-block')
ActionChains(driver)\
		.click(tweetElement)\
        .send_keys(tweet)\
        .key_down(Keys.CONTROL)\
        .send_keys(Keys.ENTER)\
        .perform()

time.sleep(3)