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

'''# find the resulting speed from calculation that is displayed upon clicking 'calculate'
calculated_speed = driver.find_element(By.CLASS_NAME, 'calculated').get_attribute('innerText')'''



'''The following 2 lines automatically click submit on the form  -- when I use this and click submit, then I get
staleElementReferenceException.

submit_button = driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/form/input[7]')
submit_button.click()'''

calculated_speed = driver.find_element(By.CLASS_NAME, 'calculated').get_attribute('innerText')


time.sleep(2)


'''reminder: text_field id's = motorKV, battVolt, pinion, spur, fgr, wheelradius, submit-value=calculate

parameterized tests to check text_field entry'''

@pytest.mark.parametrize('text_field, input_value', [(motorkV, '2400'), (battVolt, '16.8'), (pinion, '18'), (spur, '50'),
                                                     (fgr, '3.92'), (wheelradius, '2.75')])
def test_text_input(text_field, input_value):
    assert text_field.get_attribute("value") == input_value

@pytest.fixture
def cal_output():
    return calculated_speed

def test_calculated_speed_is_blank(cal_output):
    assert cal_output == ""
