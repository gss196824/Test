from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from robot.libraries.BuiltIn import timestr_to_secs,secs_to_timestr
import time

def wait_until_element_found(retry, retry_interval, driver, locator, param):
    timeout = timestr_to_secs(retry)
    retry_interval = timestr_to_secs(retry_interval)
    maxtime = time.time() + timeout

    while True:
        try:
            element = getattr(driver,locator)(param)
            return element
        except NoSuchElementException:
            print("not found, retry..")
            if time.time() > maxtime > 0:
                raise AssertionError(f"Element located by {locator}({param}) failed after {retry} timeout ")
            time.sleep(retry_interval)
