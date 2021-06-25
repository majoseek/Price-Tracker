from selenium import webdriver
PATH = "./chromedriver.exe"
URL = "https://www.g2a.com/category/games-c189"
driver = webdriver.Chrome(PATH)
driver.get(URL)
game_list = driver.find_element_by_xpath(
    '//*[@id="de982c28-e63a-4bd7-b60d-1e5e0a335bc2"]/section/div/div[2]/section/div/ul/li[1]/div[2]/h3/a')
val = game_list.get_attribute("title")
print("GAME TITLE:", val)
