import random
import sys
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, ElementClickInterceptedException, TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from getpass import getpass
import os
import datetime


def timecount(seconds):
    while seconds:
        min, sec = divmod(seconds, 60)
        count = 'Timer: {:d}min:{:d}sec'.format(min, sec)
        print(count, end='\r')
        sleep(1)
        seconds -= 1


def doengagement(username, password, hashtag, limit):
    driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
    driver.set_window_position(800, 0)
    driver.set_window_size(200, 800)
    driver.get("https://www.instagram.com/accounts/login/?source=auth_switcher")
    print("Opening instagram.com")
    timecount(2)
    
    
    timecount(2)
    userLogin = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[1]/div/label/input")
    userHashtag = str(hashtag)
    userLogin.send_keys(username)
    print("Handling Username.")
    passLogin = driver.find_element_by_name('password')
    passLogin.send_keys(password)
    print("Handling Password.")
    submit = driver.find_element_by_tag_name('form')
    submit.submit()
    print("Accessing Instagram.")
    timecount(5) 
    driver.get("https://instagram.com/explore/tags/" + userHashtag)
    print("Opening Hashtag #" + userHashtag + ".")
    print("https://instagram.com/explore/tags/" + userHashtag)
    sleep(10)
    driver.find_element_by_xpath("//a[contains(@href, '/p/')]").click()
    print("Starting Engagement.\n")
    timecount(3)
    print("---------------------------------------------------------")
    
    engagements = 0
    
    engLimit = int(limit)
    
    while engagements != engLimit:
        if engagements < engLimit:
            sleep(2)
            if driver.find_element_by_xpath('/html/body/div[6]/div[2]/div/article/header/div[2]/div[1]/div[2]/button').text=='Following':
                engDisplay = engagements + 1
                print("Starting Engagement: " + str(engDisplay) + "/" + limit)
                print("#########################################################")
                print("Already Followed.")
                driver.find_element_by_class_name("coreSpriteRightPaginationArrow").click()
                sleep(2)
            
            
            else:
                driver.find_element_by_xpath('/html/body/div[6]/div[2]/div/article/header/div[2]/div[1]/div[2]/button').click()
                sleep(2)
                engDisplay = engagements + 1
                print("Starting Engagement: " + str(engDisplay) + "/" + limit)
                print("#########################################################")
                print("Followed.")
                driver.find_element_by_class_name("coreSpriteRightPaginationArrow").click()
                sleep(2)
                engagements += 1
            
    else:
        print("\nEngagement Function Complete.")
        timecount(1)
        print("Closing Browser.")
        driver.close()



print("#########################################################")
print("#########################################################")
insta_username = input("Username: ")
insta_password = getpass("Password: ")


insta_hashtag = input("Hashtagh: ")
insta_limit = input("Limit: ")


doengagement(insta_username, insta_password, insta_hashtag, insta_limit)