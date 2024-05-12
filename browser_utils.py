from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import user_data
import webpage_data


def get_chrome_browser(
):
    """get a new Chrome browser (driver) on which to operate
       using the chromedriver path provided in user_data

    :return: browser object for executing commands
    """

    browser = webdriver.Chrome(
        executable_path=user_data.CHROMEDRIVER_EXE_PATH
    )

    return browser


def login(
        browser: webdriver
):
    """performs login with credentials from user_data.py

    :param browser: webdriver object
    :return:
    """
    # go to the welcome page
    browser.get(
        webpage_data.URLS["WELCOME_PAGE"]
    )

    # open the login pop-up
    browser.find_element_by_xpath(
        webpage_data.XPATHS["LOGIN_BUTTON"]
    ).click()

    # wait for the login pop-up to appear
    wait_for_element(
        browser,
        webpage_data.XPATHS["LOGIN_DIALOGUE"],
        1
    )

    # enter credentials
    browser.find_element_by_xpath(
        webpage_data.XPATHS["LOGIN_USERNAME_FIELD"]
    ).send_keys(
        user_data.USERNAME
    )
    browser.find_element_by_xpath(
        webpage_data.XPATHS["LOGIN_PASSWORD_FIELD"]
    ).send_keys(
        user_data.PASSWORD
    )

    # submit the form
    browser.find_element_by_xpath(
        webpage_data.XPATHS["LOGIN_SUBMIT_BUTTON"]
    ).click()

    # confirm login
    try:
        wait_for_element(
            browser,
            webpage_data.XPATHS["LOGOUT_BUTTON"],
            5
        )
    except Exception as e:
        raise Exception("LOGIN ERROR: Please check credentials")

def wait_for_element(
        browser: webdriver,
        xpath: str,
        timeout: int
):
    """wait for an element to become available

    :param browser: webdriver object on which to act
    :param xpath: xpath of the target element
    :param timeout: wait duration in seconds
    :return:
    """
    delay = timeout
    WebDriverWait(
        browser,
        delay
    ).until(
        EC.presence_of_element_located((
            By.XPATH,
            xpath
        ))
    )

def go_to_sport(
    browser: webdriver,
    sport_name: str
):
    """navigate to reservations page and select a sport.

    :param browser: webdriver object on which to act
    :param sport_name: sport for which to search
    :return:
    """

    # go to reservations page
    browser.find_element_by_xpath(
        webpage_data.XPATHS["RESERVATIONS_BUTTON"]
    ).click()

    # navigate to sport programs listings
    wait_for_element(
        browser,
        webpage_data.XPATHS["RESERVATIONS_ACTIVITIES"],
        5
    )
    browser.find_element_by_xpath(
        webpage_data.XPATHS["RESERVATIONS_ACTIVITIES"]
    ).click()
    browser.find_element_by_xpath(
        webpage_data.XPATHS["RESERVATIONS_SPORTS"]
    ).click()

    # find sport listing
    wait_for_element(
        browser,
        '//*[contains(text(), "%s")]' % sport_name,
        5
    )
    browser.find_element_by_xpath(
        '//*[contains(text(), "%s")]' % sport_name
    ).click()
