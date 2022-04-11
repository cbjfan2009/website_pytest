from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pytest


# Chrome driver path
s = Service('C:\\Program Files (x86)\\chromedriver.exe')

# create webdriver object
driver = webdriver.Chrome(service=s)

# fetch browser instance
driver.get('https://rcspeedestimator.herokuapp.com/')


# text_field id's = motorKV, battVolt, pinion, spur, fgr, wheelradius, submit-value=calculate
motorkV = driver.find_element(By.ID, 'motorkV')
motorkV.send_keys('2400')

battVolt = driver.find_element(By.ID, 'battVolt')
battVolt.send_keys('16.8')

pinion = driver.find_element(By.ID, 'pinion')
pinion.send_keys('18')

spur = driver.find_element(By.ID, 'spur')
spur.send_keys('50')

fgr = driver.find_element(By.ID, 'fgr')
fgr.send_keys('3.92')

wheelradius = driver.find_element(By.ID, 'wheelradius')
wheelradius.send_keys('2.75')

'''The following 2 lines automatically click submit on the form

submit_button = driver.find_element_by_xpath('/html/body/div[2]/div[1]/form/input[7]')
submit_button.click()'''

time.sleep(5)


@pytest.fixture
def input_value():
    input = '3.92'
    return input

@pytest.fixture
def text_field():
    field = fgr
    return field


def test_textInput(text_field, input_value):
    assert text_field.get_attribute("value") == input_value

#test_textInput(fgr, '3.92')  #this test doesn't work.  Can't figure out why the attribute value isn't finding the text'''
