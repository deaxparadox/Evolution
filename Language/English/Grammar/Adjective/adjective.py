import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import csv

selector_list: list[dict] = [
    dict(
        table = '//*[@id="__layout"]/div/div[2]/div/div[2]/main/div/section[2]/div/table'
    ),
]

driver = webdriver.Chrome()
driver.get("https://grammar.yourdictionary.com/parts-of-speech/adjectives/list-of-adjective-words.html")
# driver.implicitly_wait(30)

driver.set_page_load_timeout(10)

for selector in selector_list:
#hs_cos_wrapper_post_body > h3:nth-child(32)
    # name = driver.find_element(By.XPATH, selector.get("heading"))
    print(selector.get("table"))
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, selector.get("table")))
        )

        table = driver.find_element(By.XPATH, selector.get("table"))


        with open('common_adjective.csv', mode='w') as csvfile:
            writer = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)

            t_rows = table.find_elements(By.TAG_NAME, "tr")
            for rows in t_rows:
                td = rows.find_elements(By.TAG_NAME, "td")
                row = []
                for d in td:
                    print(d.text, end="\t")
                    row.append(d.text)
                print()
                writer.writerow(row)

    finally:
        driver.quit()
    

driver.quit()