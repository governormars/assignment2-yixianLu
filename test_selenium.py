# """
# Modify this file
# """
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys

# """
# Refer to https://selenium-python.readthedocs.io/locating-elements.html
# for more information on how to locate elements
# """

# url = "https://cs.ualberta.ca"

# path = "./chromedriver"

# def test_401_result():
#     driver = webdriver.Chrome(executable_path=path)
#     driver.get(url)
#     #Fill me in

#     driver.quit()

# def test_empty_result():
#     # Fill me in
#     pass

"""
Modify this file
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

"""
Refer to https://selenium-python.readthedocs.io/locating-elements.html
for more information on how to locate elements
"""

url = "https://cs.ualberta.ca"


def test_401_result():
    driver = webdriver.Chrome()
    driver.get(url)
    #Fill me in

    driver.quit()

def test_empty_result():
    # Fill me in
    pass
