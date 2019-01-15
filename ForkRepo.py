from selenium import webdriver
import os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import selenium.webdriver.support.ui as ui
import time


def forking(repoUrl):
    chromedriver = "/Users/megharana/Downloads/chromedriver"
    os.environ["webdriver.chrome.driver"] = chromedriver
    driver = webdriver.Chrome(chromedriver)
    driver.get(
        "https://id.atlassian.com/login?continue=https%3A%2F%2Fid.atlassian.com%2Fopenid%2Fv2%2Fop%3Fopenid.return_to%3Dhttps%3A%2F%2Fbitbucket.org%2Fsocialauth%2Fcomplete%2Fatlassianid%2F%3Fjanrain_nonce%253D2019-01-06T16%25253A01%25253A27Z1yngNl%26openid.sreg.optional%3Dfullname%2Cnickname%2Cemail%26openid.ns%3Dhttp%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%26openid.ns.sreg%3Dhttp%3A%2F%2Fopenid.net%2Fextensions%2Fsreg%2F1.1%26openid.crowdid.application%3Dbitbucket%26openid.assoc_handle%3D13687545%26openid.ns.crowdid%3Dhttps%3A%2F%2Fdeveloper.atlassian.com%2Fdisplay%2FCROWDDEV%2FCrowdID%252BOpenID%252Bextensions%2523CrowdIDOpenIDextensions-login-page-parameters%26openid.identity%3Dhttp%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select%26openid.realm%3Dhttps%3A%2F%2Fbitbucket.org%26openid.claimed_id%3Dhttp%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select%26openid.mode%3Dcheckid_setup&prompt=&application=bitbucket&tenant=&email=&errorCode="
    )

    loginUser = driver.find_element_by_id('username')
    loginUser.send_keys('megharanatiger@gmail.com' + Keys.RETURN)
    driver.find_element_by_id('login-submit').click()

    driver.implicitly_wait(50)  # seconds

    loginpswd = driver.find_element_by_id('password')

    loginpswd.send_keys(Keys.TAB)  # tab over to not-visible element

    loginpswd.send_keys('sandysomi@123' + Keys.RETURN)
    driver.find_element_by_id('login-submit').click()
    wait = ui.WebDriverWait(driver, 1)
    wait.until(lambda driver: driver.find_elements_by_id('atlwdg-blanket'))
    driver.get(repoUrl)
    forkUrl = repoUrl[0:-12] + "/fork"
    driver.get(forkUrl)

    driver.find_element_by_xpath(
        '//button[contains(text(), "Fork repository")]').click()

    driver.quit()
