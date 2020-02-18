#!/usr/bin/env python3
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
import os
import requests
import argparse
from random import randint
from selenium.common.exceptions import WebDriverException
from bs4 import BeautifulSoup

def return_random_sentence():
    print("Generating Random Sentence")
    try:
        chrome_options = Options()  
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(executable_path = '/usr/bin/chromedriver', options = chrome_options)
        driver.get('https://randomwordgenerator.com/sentence.php')
        generate_button = driver.find_element_by_xpath('/html/body/div[2]/div/div[3]/div/div/div[1]/form/table/tbody/tr[2]/td/input[2]')
        generate_button.click()

        random_sentence = driver.find_element_by_xpath('//*[@id="result"]/li/div/span').text.strip()
        driver.close()
        print(random_sentence)
        return random_sentence
    except WebDriverException as e:
        print(e)
        return 1 

def return_random_sentences():
    try:
        chrome_options = Options()  
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(executable_path = '/usr/bin/chromedriver', options = chrome_options)
        driver.get('https://www.thewordfinder.com/random-sentence-generator/')
        page = driver.execute_script('return document.documentElement.outerHTML')
        driver.quit()
        # page = requests.get(
        #     'https://www.thewordfinder.com/random-sentence-generator/')
        soup = BeautifulSoup(page, 'lxml')
        ul = soup.find('div', id="main")
        print(ul)
        sentences = ul.find(
            'div', {'class': 'sentence-results-container'})
        print(sentences)
    except WebDriverException as e:  # results-container > div > div.form-group > ul
        print(e)
        return 1


def Facebook(usr,pwd,desc,speed):
    print("Posting to Facebook")
    # if usr:
    try:
        chrome_options = Options()  
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(executable_path = '/usr/bin/chromedriver', options = chrome_options)

        #<--- code to login --->
        driver.get('https://en-gb.facebook.com/login')
        usr_box = driver.find_element_by_id('email')
        usr_box.send_keys(usr)
        pwd_box = driver.find_element_by_id('pass')
        pwd_box.send_keys(pwd)
        login_button = driver.find_element_by_id('loginbutton')
        login_button.submit()
        #<--- / code to login --->
        #Wait until login
        sleep(speed)

        #<--- code to remove opaque screen --->
        remover = driver.find_element_by_tag_name('body').click()
        sleep(speed)
        driver.get('https://www.facebook.com/')
        sleep(speed)
        # driver.find_element_by_xpath('//*[@id="js_2"]/div/div/div[1]/div[1]/h1/a/span')
        #<--- / code to remove opaque screen --->
        #WALL
        give = driver.find_element_by_xpath("//*[@name='xhpc_message']")
        # give = driver.find_element_by_xpath('//*[@id="js_1m"]/div[1]/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div')
        #Wait for wall
        sleep(speed)

        #WRITE POST
        give.send_keys(desc)
        sleep(speed)

        #POST
        # post = driver.find_element_by_xpath('//*[@id="js_1m"]/div[2]/div[3]/div[2]/button')
        post = driver.find_element_by_css_selector('button[data-testid="react-composer-post-button"]')
        post.click()
        #wait for post to be made
        sleep(speed*1.5)
        driver.close()
        return 0
    except WebDriverException as e:
        print(e)
        return 1

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-U','--username', required=True)
    parser.add_argument('-P','--password', required=True)
    args = parser.parse_args()

    while True:
        sleep_time = randint(60,300)
        # random_sentence = return_random_sentence()
        random_sentences = return_random_sentences()
        if random_sentence == 1:
            print("error retreiving random sentence.  Trying Again")
            continue
        # return_value = Facebook(args.username, args.password, random_sentence, 10)
        # if return_value == 1:
        #     print("error posting to facebook trying again")
        #     continue
        print("Sleeping for {} seconds".format(sleep_time))
        sleep(sleep_time)
