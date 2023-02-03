import time
import random
import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

twuser = os.environ['twuser']
twpass = os.environ['twpass']


tweetList = ['''...I dunno, I have a problem with every single thing I'm hearing right now.'''
            ,'''I don't know who gave you that idea, but Fixers are anything but noble or heroic. The only scent you'll smell is the miserable stink of wage slaves.'''
            ,'''If you please... call me Ishmael.'''
            ,'''Haaa, I can't believe you people. Aren't proper introductions the first step to being a member of society? Call me Ishmael, if you please.'''
            ,'''I wonder, on that hellish voyage... Was I really the only survivor?'''
            ,'''Are you the manager? I look forward to working with you, if that's the case.'''
            ,'''We could also grab some E.G.O if we're lucky, so that's three rats with one stone.'''
            ,'''He wouldn't get it. I doubt he's pondered on anything ever.'''
            ,'''I'm amazed at how you can sing such bold-faced high praise not too long after calling them a 'miserably writhing wretch'.'''
            ,'''If I were you, I wouldn't have taken part in this. Being a fallen Wing and everything, I doubt your employment ended on pleasant terms.'''
            ,'''That's right... If that bastard is really dead... I might not having have nothing left to chase after.'''
            ,'''Flitting from Office to Office, obsessively taking requests and exploring the Outskirts... Maybe I was hoping that I'd be wrong.'''
            ,'''I heard you glued our bodies back together from pieces. I look forward to working with you.'''
            ]

tweet = random.choice(tweetList)
print('Tweeting the Following:')
print(tweet)

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://twitter.com/i/flow/login")
time.sleep(1)

loginElement = driver.find_element_by_xpath("//input[@name='text']")
loginElement.send_keys(twuser)
loginElement.send_keys(Keys.ENTER)
time.sleep(1)
passElement = driver.find_element_by_xpath("//input[@name='password']")
passElement.send_keys(twpass)
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
