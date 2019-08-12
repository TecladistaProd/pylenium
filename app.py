import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

options = Options()
# options.headless = True
options.headless = False
driver = webdriver.Firefox(options=options)

driver.get("http://www.google.com")
driver.fullscreen_window()


def googleSearch(search_term):
    input_search = driver.find_element_by_css_selector('[name=q]')
    input_search.clear()
    for i in range(len(search_term)):
        input_search.send_keys(search_term[i])
        time.sleep(.095)
    input_search.send_keys(Keys.RETURN)
    return time.sleep(2)


googleSearch("youtube mario maker 3k kaizo")

driver.find_element_by_css_selector('#search a:first-child').click()
try:
    time.sleep(7)
    el = driver.find_element_by_css_selector(
        '.ytp-fullscreen-button.ytp-button')
    el.click()

    # .click()
    # time.sleep(0.7)
    # driver.find_element_by_css_selector('.ytp-play-button.ytp-button')

    time.sleep(13)
    driver.save_screenshot("page.png")
except:
    print("error")
finally:
    driver.close()
    driver.quit()
