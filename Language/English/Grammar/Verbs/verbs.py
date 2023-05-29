import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import csv

selector_list: list[dict] = [
    dict(
        heading = '//*[@id="hs_cos_wrapper_post_body"]/h3[1]',
        table = '//*[@id="hs_cos_wrapper_post_body"]/table[1]'
    ),
    dict(
        heading = '//*[@id="hs_cos_wrapper_post_body"]/h3[2]',
        table = '//*[@id="hs_cos_wrapper_post_body"]/table[2]'
    ),
    dict(
        heading = '//*[@id="hs_cos_wrapper_post_body"]/h3[3]',
        table = '//*[@id="hs_cos_wrapper_post_body"]/table[3]',
    )
]

driver = webdriver.Chrome()
driver.get("https://blog.prepscholar.com/verbs-list")
# driver.implicitly_wait(30)

for selector in selector_list:
#hs_cos_wrapper_post_body > h3:nth-child(32)
    name = driver.find_element(By.XPATH, selector.get("heading"))
    table = driver.find_element(By.XPATH, selector.get("table"))


    with open(name.text+'.csv', mode='w') as csvfile:
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

driver.quit()