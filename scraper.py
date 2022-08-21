
# selenium-related
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time


# set options as you wish
option = Options()
option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")
     
browser = webdriver.Chrome("C:\WebDriver\chromedriver.exe", options=option)

browser.get("http://facebook.com")
browser.maximize_window()
wait = WebDriverWait(browser, 30)
email_field = wait.until(EC.visibility_of_element_located((By.NAME, 'email')))
email_field.send_keys('EMAIL')
pass_field = wait.until(EC.visibility_of_element_located((By.NAME, 'pass')))
pass_field.send_keys('PASS')
pass_field.send_keys(Keys.RETURN)

time.sleep(5)

browser.get('https://www.facebook.com/pythonlang/') # once logged in, free to open up any target page

time.sleep(5)

class Scraper():
    def scrapedata(self):
        posts = browser.find_elements(By.CLASS_NAME, 'g4tp4svg mfclru0v om3e55n1 p8bdhjjv')
        reactions = 0
        post_list = []
        for post in posts:
            text = post.find_element(By.CLASS_NAME, 'm8h3af8h l7ghb35v kjdc1dyq kmwttqpk gh25dzvf n3t5jt4f').text
            time = post.find_element(By.CLASS_NAME, 'qi72231t nu7423ey n3hqoq4p r86q59rh b3qcqh3k fq87ekyn bdao358l fsf7x5fv rse6dlih s5oniofx m8h3af8h l7ghb35v kjdc1dyq kmwttqpk srn514ro oxkhqvkx rl78xhln nch0832m cr00lzj9 rn8ck1ys s3jn8y49 icdlwmnq jxuftiz4 cxfqmxzd tes86rjd').get_attribute("textContent")
            reactions = post.find_element(By.CSS_SELECTOR, 'span.ltmttdrg.gjzvkazv').get_attribute("textContent")
            items = {
                'text': text,
                'time': time,
                'reactions': reactions
            }
            post_list.append(items)
        return post_list



